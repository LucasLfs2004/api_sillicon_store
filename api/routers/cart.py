import os
import uuid
from fastapi import HTTPException, APIRouter, UploadFile, File, Form
from dependencies.const import current_GMT
from typing import List
from database.connection import mysql_connection
import time
import json
from models.models import new_cart, update_cart

router = APIRouter()


@router.get("/cart/{id_person}", tags=['Carrinho'])
async def get_cart_user(id_person: str):
    try:
        cursor = mysql_connection.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM cart_user WHERE ID_person = %s", (id_person,))
        data = cursor.fetchall()

        return data
    except Exception as e:
        return e


@router.post("/cart", tags=['Carrinho'])
async def add_to_cart(new_cart: new_cart):
    filenames = []
    # time_stamp = calendar.timegm(current_GMT)
    cart = {
        'id': int.from_bytes(uuid.uuid4().bytes[:4], byteorder="big") % (2 ** 32),
        'id_person': new_cart.id_person,
        'id_product': new_cart.id_product,
        'amount': new_cart.amount,
    }
    try:
        # Conectar ao banco de dados
        cursor = mysql_connection.cursor(dictionary=True)

        cursor.execute("INSERT INTO cart_user (id, id_person, id_product, amount) VALUES (%s, %s, %s, %s)",
                       (cart['id'], cart['id_person'], cart["id_product"], cart['amount']))
        mysql_connection.commit()

        # Realizar consulta para obter os dados inseridos
        cursor.execute('select * from cart_user where id = %s',
                       (cart['id'],))
        product_data = cursor.fetchone()
        return product_data
    except Exception as e:
        # Em caso de erro, cancelar a transação e retornar uma resposta de erro
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()


@router.patch("/cart", tags=["Carrinho"])
async def patch_cart(cart: update_cart):
    try:
        cursor = mysql_connection.cursor(dictionary=True)
        cursor.execute(
            "UPDATE cart_user SET amount = %s WHERE id = %s", (cart.id, cart.amount))
        mysql_connection.commit
        return True
    except Exception as e:
        return e
    finally:
        cursor.close()


@router.delete("/cart", tags=["Carrinho"])
async def delete_description(id: str = Form()):
    try:
        cursor = mysql_connection.cursor(dictionary=True)
        cursor.execute(
            "DELETE FROM cart_user WHERE id = %s", (id,))
        mysql_connection.commit()
        return True
    except Exception as e:
        return e
    finally:
        cursor.close()
