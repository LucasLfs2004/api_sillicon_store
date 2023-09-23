from sqlalchemy.orm import Session, aliased
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select, func
import bcrypt
import uuid
import calendar
import time
from fastapi import HTTPException, UploadFile, File
from typing import List
from sql_app.models import Product, Image, Rating
from dependencies.token import generate_jwt_token
import re
import os
import json
from database.connection import mysql_connection


class MyException(HTTPException):
    def __init__(self, detail: str, status_code: int = 400):
        super().__init__(status_code=status_code, detail=detail)


upload_folder = "public"
os.makedirs(upload_folder, exist_ok=True)


def create_new_product(db: Session, product: dict, files: List[UploadFile] = File(...)):
    try:
        filenames = []
        print(product)
        # return product
        db_product = Product(id=product['id'], owner_id=product['owner_id'], name=product['name'], description=product['description'], brand=product['brand'], color=product['color'],
                             price=product['price'], stock=product['stock'], active=product['active'], created_at=product['created_at'], updated_at=product['updated_at'], category=product['category'], featured=True)
        # Executar a inserção na tabela produtos
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        # Fechar o cursor e retornar o ID do produto
        for file in files:
            filename = str(time.time()) + file.filename.replace(' ', '_')
            filenames.append(filename)
            file_path = os.path.join(upload_folder, filename)
            with open(file_path, "wb") as f:
                f.write(file.file.read())
            db_image = Image(
                id=str(uuid.uuid4()), product_id=product['id'], path=str('public/' + filename))
            db.add(db_image)
            db.commit()
        print(filenames)
        db_rating = Rating(id=product['id'], amount=int(0), rating=int(0))
        db.add(db_rating)
        db.commit()

        # Realizar consulta para obter os dados inseridos
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
        raise HTTPException(status_code=500, detail=str(e))


def get_all_products(db: Session):
    try:
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
                                                ) AS images,
                                                rating.rating as rating,
                                                rating.amount as rating_amount
                                        FROM
                                                product
                                        LEFT JOIN
                                                image ON product.id = image.product_id
                                        LEFT JOIN
                                                rating on product.id = rating.id
                                        GROUP BY
                                                product.id;
                                        """)
        products = cursor.fetchall()
        cursor.close()

        for i in range(len(products)):
            image_links_str = products[i]['images']
            image_links_list = json.loads(image_links_str)
            image_urls = [item['image_url'] for item in image_links_list]
            products[i]['images'] = image_urls

        return products
    except IntegrityError as e:
        error_message = str(e)
        print(str(e))
    except Exception as e:
        raise MyException(status_code=500, detail=str(e))


# def get_people(db: Session):
#     return db.query(Person).all()


# def update_person(db: Session, person_id: int, updated_person: Person):
#     person = db.query(Person).filter(Person.id == person_id).first()
#     if person:
#         for key, value in updated_person.dict().items():
#             setattr(person, key, value)
#         db.commit()
#         db.refresh(person)
#     return person


# def delete_person(db: Session, param: str):
#     try:
#         pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
#         if re.match(pattern, param):
#             person = db.query(Person).filter(
#                 Person.email == param).first()
#             if person:
#                 db.delete(person)
#                 db.commit()
#         else:
#             person = db.query(Person).filter(Person.cpf == param).first()
#             if person:
#                 db.delete(person)
#                 db.commit()
#     except Exception as e:
#         raise MyException(status_code=500, detail=str(e))
