from fastapi import APIRouter, HTTPException, Depends
from database.connection import mysql_connection
import json
from dependencies import token
from requests.seller import get_seller_data
from functions.product import organize_images_from_products
from models.seller import offer_product, description_product
import uuid

router = APIRouter()


@router.get("/seller/me", tags=['Vendedor'])
async def get_data_user(current_user: int = Depends(token.get_current_user)):
    try:
        cursor = mysql_connection.cursor()
        cursor.execute(get_seller_data, (current_user,))
        profile_data = cursor.fetchone()
        cursor.close()
        data = json.loads(profile_data['seller'])

        for product in data['products_from_seller']:
            images = organize_images_from_products(product=product)
            product['images'] = images
        return data

    except Exception as e:
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.patch("/seller/product/offer", tags=['Vendedor'])
async def change_value_product(infos: offer_product, current_user: int = Depends(token.get_current_seller)):
    try:
        cursor = mysql_connection.cursor()
        cursor.execute(
            'UPDATE value_product SET price_now = %s WHERE id_product = %s', (infos.new_price, infos.id_product))
        mysql_connection.commit()
        return True

    except Exception as e:
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/seller/product/description", tags=['Vendedor'])
async def set_description_product(description: description_product, current_user: int = Depends(token.get_current_seller)):
    try:
        id = int.from_bytes(
            uuid.uuid4().bytes[:4], byteorder="big") % (2 ** 32)
        cursor = mysql_connection.cursor()

        cursor.execute(
            'INSERT INTO description_product (id_description, id_product, description_html) VALUES (%s, %s, %s)', (id, description.id_product, description.description))
        mysql_connection.commit()
        cursor.close()
        return True

    except Exception as e:
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.patch("/seller/product/description", tags=['Vendedor'])
async def patch_description_product(description: description_product, current_user: int = Depends(token.get_current_seller)):
    try:
        cursor = mysql_connection.cursor()
        cursor.execute(
            'UPDATE description_product set description_html = %s WHERE id_product = %s', (description.description, description.id_product))
        mysql_connection.commit()
        cursor.close()
        return True

    except Exception as e:
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))
