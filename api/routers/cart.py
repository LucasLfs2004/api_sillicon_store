import uuid
from fastapi import HTTPException, APIRouter, Form, Depends
from api.database.connection import mysql_connection
import json
from api.models.models import new_cart, update_cart, apply_discount, ship_cart, id_model, new_cart_item
from api.dependencies import token
from api.requests.cart import select_complete_cart
from api.functions.cart import organize_response_cart

router = APIRouter()


@router.get("/cart/{id_person}", tags=['Carrinho'])
async def get_cart_user(id_person: str):
    try:
        cursor = mysql_connection.cursor(dictionary=True)

        cursor.execute(
            select_complete_cart, (id_person,))
        data = cursor.fetchall()

        return data
    except Exception as e:

        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/cart", tags=['User', 'Carrinho'])
async def get_data_user(current_user: int = Depends(token.get_current_user)):
    try:
        print(current_user)
        cursor = mysql_connection.cursor(dictionary=True)
        cursor.execute(select_complete_cart,
                       (current_user,))
        cart = cursor.fetchone()
        print(cart)

        cart = await organize_response_cart(cart=cart, id_person=current_user)

        return cart

    except Exception as e:
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/cart", tags=['Carrinho'])
async def add_to_cart(new_cart: new_cart):
    cart = {
        'id': int.from_bytes(uuid.uuid4().bytes[:4], byteorder="big") % (2 ** 32),
        'id_person': new_cart.id_person,
        'id_product': new_cart.id_product,
        'amount': new_cart.amount,
    }
    try:
        # Conectar ao banco de dados
        cursor = mysql_connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM cart_items WHERE id_person = %s and id_product = %s",
                       (cart['id_person'], cart['id_product']))
        data = cursor.fetchall()

        if (len(data) > 1):
            cursor.execute(
                "DELETE FROM cart_items WHERE id_product = %s", (cart['id_product'],))
            mysql_connection.commit()
        elif (len(data) == 1):
            cursor.execute(
                "UPDATE cart_items SET amount = %s WHERE id = %s", (cart['amount'], data[0]['id']))
            mysql_connection.commit()
        if (len(data) != 1):
            cursor.execute("INSERT INTO cart_items (id, id_person, id_product, amount) VALUES (%s, %s, %s, %s)",
                           (cart['id'], cart['id_person'], cart["id_product"], cart['amount']))
            mysql_connection.commit()

        # Realizar consulta para obter os dados inseridos
        cursor.execute(select_complete_cart,
                       (cart['id_person'],))
        product_data = cursor.fetchone()

        cart = await organize_response_cart(cart=product_data, id_person=new_cart.id_person)

        return cart
    except Exception as e:
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/cart-item", tags=['Carrinho'])
async def add_to_cart(new_cart: new_cart_item, current_user: int = Depends(token.get_current_user)):
    cart = {
        'id': int.from_bytes(uuid.uuid4().bytes[:4], byteorder="big") % (2 ** 32),
        'id_product': new_cart.id_product,
        'amount': new_cart.amount,
    }
    try:
        print(current_user)
        # Conectar ao banco de dados
        cursor = mysql_connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM cart_items WHERE id_person = %s and id_product = %s",
                       (current_user, cart['id_product']))
        data = cursor.fetchall()

        if (len(data) > 1):
            cursor.execute(
                "DELETE FROM cart_items WHERE id_product = %s", (cart['id_product'],))
            mysql_connection.commit()
        elif (len(data) == 1):
            amount = cart['amount'] + data[0]['amount']
            cursor.execute(
                "UPDATE cart_items SET amount = %s WHERE id = %s", (amount, data[0]['id']))
            mysql_connection.commit()
        if (len(data) != 1):
            cursor.execute("INSERT INTO cart_items (id, id_person, id_product, amount) VALUES (%s, %s, %s, %s)",
                           (cart['id'], current_user, cart["id_product"], cart['amount']))
            mysql_connection.commit()

        # Realizar consulta para obter os dados inseridos
        cursor.execute(select_complete_cart,
                       (current_user,))
        product_data = cursor.fetchone()

        cart = await organize_response_cart(cart=product_data, id_person=current_user)

        return cart
    except Exception as e:
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.delete('/cart', tags=['Carrinho'])
async def clear_cart(current_user: int = Depends(token.get_current_user)):
    try:
        cursor = mysql_connection.cursor(dictionary=True)
        cursor.execute(
            "DELETE FROM cart_items WHERE id_person = %s", (current_user,)
        )
        mysql_connection.commit()
        print(current_user)
        cursor.execute(
            'UPDATE cart_user SET discount = 0, discount_value = 0, product_total_value = 0, voucher = NULL, portions = 0, ship_value = 0, cart_total_value = 0, ship_cep = NULL, ship_street = null, ship_deadline = NULL WHERE id_person = %s',
            (current_user,)
        )
        mysql_connection.commit()
        cursor.execute(
            'DELETE FROM portion WHERE id_cart_user = %s', (current_user,)
        )
        mysql_connection.commit()
        return True
    except Exception as e:
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.patch("/cart-item", tags=["Carrinho"])
async def patch_cart(cart_update: update_cart, current_user: int = Depends(token.get_current_user)):
    try:
        cursor = mysql_connection.cursor(dictionary=True)

        cursor.execute(
            "UPDATE cart_items SET amount = %s WHERE id like %s and id_person like %s",
            (cart_update.amount, cart_update.id, current_user))
        mysql_connection.commit()

        return True
    except Exception as e:
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/cart-item/{id}", tags=["Carrinho"])
async def delete_item_from_cart(id: str, current_user: int = Depends(token.get_current_user)):
    try:
        print(current_user)
        cursor = mysql_connection.cursor(dictionary=True)
        cursor.execute(
            "DELETE FROM cart_items WHERE id = %s and id_person = %s",
            (id, current_user))
        mysql_connection.commit()

        cursor.close()
        return True

    except Exception as e:
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/cart-discount", tags=['Carrinho'])
async def apply_discount_in_cart(code: apply_discount, current_user: int = Depends(token.get_current_user)):
    try:
        print(current_user)
        cursor = mysql_connection.cursor(dictionary=True)
        cursor.execute(
            'SELECT * FROM discount_list WHERE code = %s', (code.code,))
        code_data = cursor.fetchone()
        print(code_data)
        # return code_data
        if (code_data is None):
            return "Cupom Inválido"
        else:
            cursor.execute('UPDATE cart_user SET voucher = %s WHERE id_person = %s',
                           (code.code, current_user))
            mysql_connection.commit()
            print('chamando a procedure')
            cursor.execute('CALL atualizar_cart_user(%s)',
                           (current_user,))
            mysql_connection.commit()

        return True

    except Exception as e:
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/cart-discount", tags=['Carrinho'])
async def clear_voucher_discount(current_user: int = Depends(token.get_current_user)):
    try:
        print(current_user)
        cursor = mysql_connection.cursor(dictionary=True)
        cursor.execute(
            'UPDATE cart_user SET voucher = NULL WHERE id_person = %s', (current_user,))
        cursor.execute('CALL atualizar_cart_user(%s)',
                       (current_user,))
        mysql_connection.commit()

        # Realizar consulta para obter os dados inseridos
        return True
    except Exception as e:
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.post('/cart-ship', tags=['Carrinho'])
async def set_ship_cart(ship: ship_cart, current_user: int = Depends(token.get_current_user)):
    try:
        cursor = mysql_connection.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM ship_value WHERE region = %s", (ship.region,))
        data = cursor.fetchone()

        # Update da table cart_user
        cursor.execute("UPDATE cart_user SET ship_value = %s, ship_deadline = %s, ship_cep = %s, ship_street = %s WHERE id_person = %s",
                       (data['value'], data['deadline'], ship.cep, ship.street, current_user))
        mysql_connection.commit()

        # Chamada da procedure
        cursor.execute('CALL atualizar_cart_user(%s)',
                       (current_user,))
        mysql_connection.commit()
        return True
    except Exception as e:
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))
