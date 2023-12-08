import os
import calendar
import uuid
from fastapi import HTTPException, APIRouter, UploadFile, File, Form
from dependencies.const import current_GMT
from typing import List
from database.connection import mysql_connection
import time


router = APIRouter()

upload_folder = "public/product"
os.makedirs(upload_folder, exist_ok=True)


@router.post("/product", tags=['Produtos'])
async def create_product(owner: str = Form(), name: str = Form(), description: str = Form(), brand_id: str = Form(), category_id: str = Form(),
                         price: str = Form(), stock: str = Form(), featured: str = Form(), warranty: str = Form(), model: str = Form(None), files: List[UploadFile] = File(None)):
    filenames = []
    # time_stamp = calendar.timegm(current_GMT)
    product = {
        'id': str(uuid.uuid4()),
        'owner': owner,
        'active': True,
        'featured': bool(featured),
        'name': name,
        'brand_id': brand_id,
        'category_id': category_id,
        'stock': int(stock),
        'warranty': warranty,
        'model': model
    }
    try:
        # Conectar ao banco de dados
        cursor = mysql_connection.cursor(dictionary=True)

        cursor.execute("INSERT INTO product (id, seller_id, name, brand_id, category_id, stock, warranty, active, featured, model) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                       (product['id'], product['owner'], product['name'], product['brand_id'], product['category_id'], product['stock'], product['warranty'], product['active'], product['featured'], product['model']))

        mysql_connection.commit()

        cursor.execute("SELECT * FROM PRODUCT WHERE id = %s", (product["id"]))
        new_product = cursor.fetchone()

        return new_product

    except Exception as e:
        # Em caso de erro, cancelar a transação e retornar uma resposta de erro
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
