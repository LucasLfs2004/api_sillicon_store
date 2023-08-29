from fastapi import APIRouter
import os
import calendar
import uuid
from fastapi import HTTPException, UploadFile, File, Form
from dependencies.const import current_GMT
from typing import List
from database.connection import mysql_connection
import time
from models.models import new_category


router = APIRouter()

upload_folder = "public"
os.makedirs(upload_folder, exist_ok=True)


@router.post("/product")
async def create_product(owner: str = Form(), name: str = Form(), description: str = Form(), brand: str = Form(), category: str = Form(),
                         price: str = Form(), stock: str = Form(), featured: str = Form(), files: List[UploadFile] = File(...)):
    filenames = []
    time_stamp = calendar.timegm(current_GMT)
    product = {
        'id': str(uuid.uuid4()),
        'owner': owner,
        'active': bool(featured),
        'featured': True,
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
    try:
        # Conectar ao banco de dados
        cursor = mysql_connection.cursor(dictionary=True)

        # Executar a inserção na tabela produtos
        cursor.execute(
            "INSERT INTO PRODUCT (id, owner, name, description, brand, price, stock, active, created_at, updated_at, category, featured) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (product['id'], product['owner'], product['name'], product['description'], product['brand'], product['price'], product['stock'],
             product['active'], product['created_at'], product['updated_at'], product['category'], product['featured'])
        )
        # Fechar o cursor e retornar o ID do produto
        for file in files:
            filename = str(time.time()) + file.filename.replace(' ', '_')
            filenames.append(filename)
            file_path = os.path.join(upload_folder, filename)
            with open(file_path, "wb") as f:
                f.write(file.file.read())
            cursor.execute(
                "INSERT INTO image (id, path) VALUES (%s, %s)",
                (product['id'], str("public/" + filename))
            )
        print(filenames)

        cursor.execute(
            "INSERT INTO rating (id, amount, rating) VALUES (%s, %s, %s)",
            (product['id'], int(0), int(0))
        )
        mysql_connection.commit()

        # Realizar consulta para obter os dados inseridos
        cursor.execute("""
									SELECT
											product.id AS id,
											product.name AS product_name,
											product.description AS product_description,
											product.brand AS product_brand,
											product.price AS product_price,
											product.stock AS product_stock,
											product.category AS product_category,
											JSON_ARRAYAGG(
													JSON_OBJECT(
															'img_path', image.path
													)
											) AS images,
											JSON_ARRAYAGG(
													JSON_OBJECT(
															'amount', rating.amount,
															'rating', rating.rating
													)
											) AS rating
									FROM
											product
									LEFT JOIN
											image ON product.id = image.id
									LEFT JOIN
											rating ON product.id = rating.id
									WHERE
											product.id = %s
									GROUP BY
											product.id;
											""", (product['id'],)
        )
        product_data = cursor.fetchone()
        cursor.close()
        return {"new_product:": product_data}
    except Exception as e:
        # Em caso de erro, cancelar a transação e retornar uma resposta de erro
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()


@router.get('/products')
def get_products():
    cursor = mysql_connection.cursor(dictionary=True)
    cursor.execute("""
									SELECT
											product.id AS id,
											product.name AS product_name,
											product.description AS product_description,
											product.brand AS product_brand,
											product.price AS product_price,
											product.stock AS product_stock,
											product.category AS product_category,
											JSON_ARRAYAGG(
													JSON_OBJECT(
															'image_url', image.path
													)
											) AS images
									FROM
											product
									LEFT JOIN
											image ON product.id = image.id
									GROUP BY
											product.id;
									""")
    product = cursor.fetchall()
    cursor.close()
    return product


@router.post("/add-category")
def create_category(category: new_category):
    try:
        cursor = mysql_connection.cursor(dictionary=True)
        category.id = str(uuid.uuid4())
        cursor.execute(
            "INSERT INTO CATEGORY (id, name) VALUES (%s, %s)",
            (category.id, category.name)
        )
        mysql_connection.commit()

        # Realizar consulta para obter os dados inseridos
        cursor.execute("SELECT * FROM category WHERE ID = %s", (category.id,))
        inserted_data = cursor.fetchone()

        # Fechar o cursor e retornar o ID do produto
        cursor.close()
        return {"new_category:": inserted_data}
    except Exception as e:
        # Em caso de erro, cancelar a transação e retornar uma resposta de erro
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))
