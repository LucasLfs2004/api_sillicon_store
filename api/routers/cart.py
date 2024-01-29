import os
import uuid
from fastapi import HTTPException, APIRouter, UploadFile, File, Form, Depends
from dependencies.const import current_GMT
from typing import List
from database.connection import mysql_connection
import time
import json
from models.models import new_cart, update_cart, apply_discount, ship_cart
from dependencies import token
from requests.cart import select_complete_cart

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
        return e


@router.get("/cart", tags=['User'])
async def get_data_user(current_user: int = Depends(token.get_current_user)):
    try:
        print(current_user)
        cursor = mysql_connection.cursor(dictionary=True)
        cursor.execute(select_complete_cart,
                       (current_user,))
        cart = cursor.fetchone()

        cart = await organize_response_cart(cart=cart, id_person=current_user)

        return cart

    except Exception as e:
        return e


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

        print(data)
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


@router.patch("/cart-item", tags=["Carrinho"])
async def patch_cart(cart: update_cart):
    try:
        cursor = mysql_connection.cursor(dictionary=True)

        cursor.execute(
            "UPDATE cart_items SET amount = %s WHERE id like %s",
            (cart.amount, cart.id))
        mysql_connection.commit()

        cursor.execute("SELECT * FROM cart_items WHERE id = %s",
                       (cart.id,))
        cart_item = cursor.fetchone()
        print(cart_item)
        cursor.close()
        return cart_item
    except Exception as e:
        return e


@router.delete("/cart", tags=["Carrinho"])
async def delete_description(id: str = Form()):
    try:
        cursor = mysql_connection.cursor(dictionary=True)
        cursor.execute(
            "DELETE FROM cart_items WHERE id = %s", (id,))
        mysql_connection.commit()
        return True
    except Exception as e:
        return e
    finally:
        cursor.close()


@router.post("/cart-discount", tags=['Carrinho'])
async def apply_discount_in_cart(discount: apply_discount):
    try:
        cursor = mysql_connection.cursor(dictionary=True)
        cursor.execute(
            'SELECT * FROM discount_list WHERE code = %s', (discount.code,))
        code_data = cursor.fetchone()
        # return code_data
        if (code_data is None):
            return "Cupom Inválido"
        else:
            cursor.execute('UPDATE cart_user SET voucher = %s WHERE id_person = %s',
                           (discount.code, discount.id_person))
            mysql_connection.commit()
            print('chamando a procedure')
            cursor.execute('CALL atualizar_cart_user(%s)',
                           (discount.id_person,))
            mysql_connection.commit()
            return 'DEU TUDO CERTO'

    except Exception as e:
        return e


@router.delete("/cart-discount", tags=['Carrinho'])
async def clear_voucher_discount(id_person: str):
    try:
        cursor = mysql_connection.cursor(dictionary=True)
        cursor.execute(
            'UPDATE cart_user SET voucher = NULL WHERE id_person = %s', (id_person,))
        cursor.execute('CALL atualizar_cart_user(%s)',
                       (id_person,))
        mysql_connection.commit()
        mysql_connection.commit()
        return True
    except Exception as e:
        return e


@router.post('/cart-ship', tags=['Carrinho'])
async def set_ship_cart(ship: ship_cart):
    try:

        return True
    except Exception as e:
        return e


async def calc_list_portions(array_cart: dict, id_person: str):
    try:
        cursor = mysql_connection.cursor(dictionary=True)
        cursor.execute(
            "DELETE FROM portion WHERE id_cart_user = %s", (id_person,))
        mysql_connection.commit()
        print('passamos do delete')
        for i in range(array_cart['portions']):
            total_value_items = 0
            for item in array_cart['items']:
                value_item = item['value']['price_now'] if item['value']['price_now'] is not None else item['value']['common_price']
                value_item *= item['amount']
                value_item *= (1 + item['value']['fees_credit'] / 100)
                if i > 0:
                    value_item *= (1 + item['value']
                                   ['fees_monthly'] / 100) ** (i + 1)
                total_value_items += value_item
            often = i + 1
            value_credit = round(total_value_items, 2)
            value_portion = round(total_value_items / (i + 1), 2)
            cursor.execute("INSERT INTO portion (id_cart_user, often, value_credit, value_portion) VALUES (%s, %s, %s, %s)",
                           (id_person, often, value_credit, value_portion))
            mysql_connection.commit()

            cursor.execute('''SELECT JSON_ARRAYAGG(
                                    JSON_OBJECT(
                                        'often', portion.often, 'value_credit', portion.value_credit, 'value_portion', portion.value_portion
                                    )
                                ) AS portions
                            from portion
                            where
                                id_cart_user = %s''', (id_person,))
            portions = cursor.fetchone()
        return json.loads(portions['portions'])
    except Exception as e:
        print(e)


async def organize_response_cart(cart: dict, id_person: str):
    array_cart = json.loads(cart["cart"])

    for item in array_cart['items']:
        item['images'] = sorted(item['images'])

    # Se precisar ordenar a lista de itens pelo nome do produto:
    array_cart['items'] = sorted(
        array_cart['items'], key=lambda x: x['name'])

    array_cart['list_portions'] = await calc_list_portions(array_cart=array_cart, id_person=id_person)

    return array_cart
