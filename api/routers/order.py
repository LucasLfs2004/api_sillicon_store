import os
import uuid
from fastapi import HTTPException, APIRouter, UploadFile, File, Form, Depends
from dependencies.const import current_GMT
from typing import List
from database.connection import mysql_connection
import time
import json
from dependencies import token
from models.product import update_product_model, new_description
from requests.order import select_purchase_order
from functions.product import organize_images_from_products

router = APIRouter()


@router.get("/order/{id}", tags=['Pedidos'])
async def get_limited_products(id: str):
    try:
        cursor = mysql_connection.cursor(dictionary=True)

        cursor.execute(select_purchase_order, (id,))
        data = cursor.fetchone()
        print(data)
        data = json.loads(data['purchase'])

        for product in data['items']:
            images = organize_images_from_products(product=product)
            product['images'] = images

        return data
    except Exception as e:
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
