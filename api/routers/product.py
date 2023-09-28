
import calendar
import uuid
from fastapi import HTTPException, APIRouter, UploadFile, File, Form, Depends
from dependencies.const import current_GMT
from typing import List
from database.connection import mysql_connection
import time
from sqlalchemy.orm import Session
from sql_app.database import SessionLocal
from sql_queries.crud_product import create_new_product, get_all_products


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/product", tags=['Produtos'])
async def create_product(owner: str = Form(), name: str = Form(), description: str = Form(), brand: str = Form(), category: str = Form(),
                         price: str = Form(), stock: str = Form(), featured: str = Form(), files: List[UploadFile] = File(...), db: Session = Depends(get_db)):

    time_stamp = calendar.timegm(current_GMT)
    product = {
        'id': str(uuid.uuid4()),
        'owner_id': int(owner),
        'active': bool(True),
        'featured': featured,
        'name': name,
        'description': description,
        'brand': brand,
        'category': category,
        'price': float(price),
        'stock': int(stock),
        'color': str('null'),
        'created_at': int(time_stamp),
        'updated_at': int(time_stamp),
    }
    new_product = create_new_product(db, product, files)
    return new_product


@router.get('/products', tags=['Produtos'])
def get_products(db: Session = Depends(get_db)):
    products = get_all_products(db)
    return products

    # cursor = mysql_connection.cursor(dictionary=True)
    # cursor.execute("""
    # 								SELECT
    # 										product.id AS id,
    # 										product.name AS product_name,
    # 										product.description AS product_description,
    # 										product.brand AS product_brand,
    # 										product.price AS product_price,
    # 										product.stock AS product_stock,
    # 										product.category AS product_category,
    # 										JSON_ARRAYAGG(
    # 												JSON_OBJECT(
    # 														'image_url', image.path
    # 												)
    # 										) AS images
    # 								FROM
    # 										product
    # 								LEFT JOIN
    # 										image ON product.id = image.id
    # 								GROUP BY
    # 										product.id;
    # 								""")
    # product = cursor.fetchall()
    # cursor.close()
    # return product
