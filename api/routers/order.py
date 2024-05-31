from fastapi import HTTPException, APIRouter, Depends
from database.connection import mysql_connection
import json
from dependencies import token
from models.order import purchase_order
from pydantic import BaseModel
from requests.order import select_purchase_order, select_purchase_order_id, select_data_order
from functions.product import organize_images_from_products
from functions.cart import calc_portion_value
from typing import Optional
import uuid

router = APIRouter()


@router.get("/purchase-orders", tags=['Pedidos'])
async def get_limited_products(current_user: int = Depends(token.get_current_user)):
    try:
        cursor = mysql_connection.cursor(dictionary=True)

        cursor.execute(select_purchase_order, (current_user,))
        data = cursor.fetchone()
        data = json.loads(data['purchases'])

        for item in data:
            for product in item['items']:
                images = organize_images_from_products(product=product)
                product['images'] = images

        return data
    except Exception as e:
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()


@router.get("/purchase-orders/{id}", tags=['Pedidos'])
async def get_limited_products(id: str, current_user: int = Depends(token.get_current_user)):
    try:
        cursor = mysql_connection.cursor(dictionary=True)

        cursor.execute(select_purchase_order_id, (id,))
        data = cursor.fetchone()
        data = json.loads(data['purchases'])

        for product in data['items']:
            images = organize_images_from_products(product=product)
            product['images'] = images

        return data
    except Exception as e:
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()


class purchase_order(BaseModel):
    payment_method: str
    often: Optional[int] = 0


def generate_id():
    return int.from_bytes(uuid.uuid4().bytes[:4], byteorder="big") % (2 ** 32)


@router.post("/purchase-orders", tags=['Pedidos'])
async def post_purchase_order(purchase: purchase_order, current_user: int = Depends(token.get_current_user)):
    try:
        print(current_user)
        cursor = mysql_connection.cursor(dictionary=True)
        cursor.execute(select_data_order,
                       (current_user,))
        data = cursor.fetchone()
        cursor.close()
        print(data)
        order = json.loads(data['cart'])

        portion_value = 0

        id_order = generate_id()

        cursor.execute('INSERT INTO purchase_order (id_order, id_customer, status_order, total_value, payment_method, portions_value, often, delivery_street, delivery_city, delivery_cep, delivery_state, delivery_cep, delivery_number, delivery_complement, discount_value, ship_value) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                       (id_order, current_user, 'completed', order['cart_total_value'], purchase.payment_method, portion_value, purchase.often, order['ship']['street'], order['ship']['city'], order['ship']['cep'], order['ship']['ship_number'], order['ship']['complement'], order['discount_value'], order['ship_value']))
        mysql_connection.commit()

        for item in order['items']:
            value_product = 0
            if item['value']['price_now'] is None or item['value']['price_now'] == 0:
                value_product = item['value']['common_price']
            else:
                value_product = item['value']['price_now']

            if purchase.payment_method == 'credit-card':
                value = value_product
                value_product = calc_portion_value(
                    item['value']['fees_monthly'], item['value']['fees_credit'], value, purchase.often)

            cursor.execute('INSERT INTO order_item (id_order_item, id_order, id_product, quantity, price) VALUES (%s, %s, %s, %s, %s)',
                           (generate_id(), id_order, order['id'], order['amount'], value_product))
            mysql_connection.commit()

        cursor.execute(select_purchase_order_id, (id_order,))
        data = cursor.fetchone()
        data = json.loads(data['purchases'])

        for product in data['items']:
            images = organize_images_from_products(product=product)
            product['images'] = images

        return data

    except Exception as e:
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
