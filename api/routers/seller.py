from fastapi import APIRouter
from database.connection import mysql_connection
from fastapi import HTTPException, Form, status, Depends
import json
from dependencies import token
from requests.seller import get_seller_data
from functions.product import organize_images_from_products
from models.seller import offer_product

router = APIRouter()


# @router.get("/seller", tags=['User'])
# def get_persons():
#     cursor = mysql_connection.cursor(dictionary=True)
#     cursor.execute(get_persons_query)
#     person = cursor.fetchall()
#     cursor.close()
#     return person


@router.get("/seller/me", tags=['Seller'])
async def get_data_user(current_user: int = Depends(token.get_current_user)):
    try:
        print(current_user)
        cursor = mysql_connection.cursor(dictionary=True)
        cursor.execute(get_seller_data, (current_user,))
        profile_data = cursor.fetchone()
        cursor.close()
        data = json.loads(profile_data['seller'])

        for product in data['products_from_seller']:
            images = organize_images_from_products(product=product)
            product['images'] = images
        return data

    except Exception as e:
        print(e)
        return e


@router.post("/seller/product/offer", tags=['Seller'])
async def change_value_product(infos: offer_product, current_user: int = Depends(token.get_current_user)):
    try:
        cursor = mysql_connection.cursor(dictionary=True)
        cursor.execute(
            'UPDATE value_product SET price_now = %s WHERE id_product = %s', (infos.new_price, infos.id_product))
        mysql_connection.commit()
        return True

    except Exception as e:
        print(e)
        return e
