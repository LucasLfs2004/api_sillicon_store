import os
import calendar
import uuid
from fastapi import HTTPException, APIRouter, UploadFile, File, Form
from dependencies.const import current_GMT
from typing import List
from database.connection import mysql_connection
import time
import json
from models.models import new_description

router = APIRouter()

upload_folder = "public/product"
os.makedirs(upload_folder, exist_ok=True)


@router.get("/product", tags=['Produtos'])
def get_products():
    try:
        cursor = mysql_connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM PRODUCT",)
        data = cursor.fetchall()
        return data
    except Exception as e:
        return e


@router.get("/product/id/{product_id}", tags=['Produtos'])
def search_product(product_id: str):
    try:
        cursor = mysql_connection.cursor(dictionary=True)

        cursor.execute("""SELECT JSON_OBJECT(
                            'id', product.id,
                            'name', product.name,
                            'stock', product.stock,
                            'warranty', product.warranty,
                            'model', product.model,
                            'featured', product.featured,
                            'active', product.active,
                            'brand', brand.name,
                            'category', category.name,
                            'value', JSON_OBJECT(
                                'price_now', value_product.price_now,
                                'common_price', value_product.common_price,
                                'portions', value_product.portions,
                                'fees_monthly', value_product.fees_monthly,
                                'fees_credit', value_product.fees_credit
                            ),
                            'rating', JSON_OBJECT(
                                'amount_rating', rating.amount,
                                'rating_value', rating.rating
                            ),
                            'images', JSON_ARRAYAGG(
                                image.path
                            )
                        ) AS product
                        FROM product
                        LEFT JOIN category ON product.category_id = category.id
                        LEFT JOIN brand ON product.brand_id = brand.id
                        LEFT JOIN value_product ON product.id = value_product.id_product
                        LEFT JOIN rating ON product.id = rating.id_product
                        LEFT JOIN image ON product.id = image.id_product
                        WHERE product.id = %s
                        GROUP BY
                            product.id,
                            product.name,
                            product.stock,
                            product.warranty,
                            product.model,
                            product.featured,
                            product.active,
                            brand.name,
                            category.name,
                            value_product.price_now,
                            value_product.common_price,
                            value_product.portions,
                            value_product.fees_monthly,
                            value_product.fees_credit,
                            rating.amount,
                            rating.rating;""",
                       (product_id,))
        data = cursor.fetchone()
        return json.loads(data["product"])
    except Exception as e:
        return e


@router.get("/product/name/{product_name}", tags=['Produtos'])
def search_product(product_name: str):
    try:
        cursor = mysql_connection.cursor(dictionary=True)

        search = str("%" + product_name + "%")

        cursor.execute("""SELECT JSON_OBJECT(
                            'id', product.id,
                            'name', product.name,
                            'stock', product.stock,
                            'warranty', product.warranty,
                            'model', product.model,
                            'featured', product.featured,
                            'active', product.active,
                            'brand', brand.name,
                            'category', category.name,
                            'value', JSON_OBJECT(
                                'price_now', value_product.price_now,
                                'common_price', value_product.common_price,
                                'portions', value_product.portions,
                                'fees_monthly', value_product.fees_monthly,
                                'fees_credit', value_product.fees_credit
                            ),
                            'rating', JSON_OBJECT(
                                'amount_rating', rating.amount,
                                'rating_value', rating.rating
                            ),
                            'images', JSON_ARRAYAGG(
                                image.path
                            )
                        ) AS product
                        FROM product
                        LEFT JOIN category ON product.category_id = category.id
                        LEFT JOIN brand ON product.brand_id = brand.id
                        LEFT JOIN value_product ON product.id = value_product.id_product
                        LEFT JOIN rating ON product.id = rating.id_product
                        LEFT JOIN image ON product.id = image.id_product
                        WHERE product.name LIKE %s OR product.model LIKE %s
                        GROUP BY
                            product.id,
                            product.name,
                            product.stock,
                            product.warranty,
                            product.model,
                            product.featured,
                            product.active,
                            brand.name,
                            category.name,
                            value_product.price_now,
                            value_product.common_price,
                            value_product.portions,
                            value_product.fees_monthly,
                            value_product.fees_credit,
                            rating.amount,
                            rating.rating;""",
                       (search, search))
        data = cursor.fetchall()
        products = []

        for product in data:
            products.append(json.loads(product["product"]))

        return products
    except Exception as e:
        return e


@router.post("/product", tags=['Produtos'])
async def create_product(owner: str = Form(), name: str = Form(), brand_id: str = Form(), category_id: str = Form(),
                         price: str = Form(), portions: str = Form(), fees_monthly: str = Form(), fees_credit: str = Form(), stock: str = Form(), featured: str = Form(), warranty: str = Form(), model: str = Form(None), files: List[UploadFile] = File(...)):
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
        cursor.execute(
            "INSERT INTO value_product (id, id_product, common_price, portions, fees_monthly, fees_credit) VALUES (%s, %s, %s, %s, %s, %s)",
            (str(uuid.uuid4()), product['id'], float(price), int(portions), float(fees_monthly), float(fees_credit)))

        # Fechar o cursor e retornar o ID do produto
        for file in files:
            filename = str(time.time()) + file.filename.replace(' ', '_')
            filenames.append(filename)
            file_path = os.path.join(upload_folder, filename)
            with open(file_path, "wb") as f:
                f.write(file.file.read())
            cursor.execute(
                "INSERT INTO image (id, id_product, path) VALUES (%s, %s, %s)",
                (str(uuid.uuid4()), product['id'],
                 str("public/product" + filename))
            )
        # print(filenames)

        cursor.execute(
            "INSERT INTO rating (id, id_product, amount, rating) VALUES (%s, %s, %s, %s)",
            (product['id'], product['id'], int(0), int(0))
        )
        mysql_connection.commit()

        print("Entrando no select gigante")

        # Realizar consulta para obter os dados inseridos
        cursor.execute("""SELECT JSON_OBJECT(
                            'id', product.id,
                            'name', product.name,
                            'stock', product.stock,
                            'warranty', product.warranty,
                            'model', product.model,
                            'featured', product.featured,
                            'active', product.active,
                            'brand', brand.name,
                            'category', category.name,
                            'value', JSON_OBJECT(
                                'price_now', value_product.price_now,
                                'common_price', value_product.common_price,
                                'portions', value_product.portions,
                                'fees_monthly', value_product.fees_monthly,
                                'fees_credit', value_product.fees_credit
                            ),
                            'rating', JSON_OBJECT(
                                'amount_rating', rating.amount,
                                'rating_value', rating.rating
                            ),
                            'images', JSON_ARRAYAGG(
                                image.path
                            )
                        ) AS product
                        FROM product
                        LEFT JOIN category ON product.category_id = category.id
                        LEFT JOIN brand ON product.brand_id = brand.id
                        LEFT JOIN value_product ON product.id = value_product.id_product
                        LEFT JOIN rating ON product.id = rating.id_product
                        LEFT JOIN image ON product.id = image.id_product
                        WHERE product.id = %s
                        GROUP BY
                            product.id,
                            product.name,
                            product.stock,
                            product.warranty,
                            product.model,
                            product.featured,
                            product.active,
                            brand.name,
                            category.name,
                            value_product.price_now,
                            value_product.common_price,
                            value_product.portions,
                            value_product.fees_monthly,
                            value_product.fees_credit,
                            rating.amount,
                            rating.rating;""",
                       (product['id'],))
        product_data = cursor.fetchall()
        cursor.close()
        return json.loads(product_data['product'])
    except Exception as e:
        # Em caso de erro, cancelar a transação e retornar uma resposta de erro
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()


@router.delete('/product', tags=['Produtos'])
def delete_product(id_product: str = Form()):
    try:
        cursor = mysql_connection.cursor(dictionary=True)

        cursor.execute(
            "SELECT image.path FROM image WHERE image.id_product LIKE %s", (
                id_product,)
        )
        data = cursor.fetchall()
        print(data)
        cursor.execute("DELETE FROM product where id LIKE %s", (id_product,))
        mysql_connection.commit()

        for filename in data:
            filename_img = os.path.join(filename["path"])
            print(filename)
            print(filename_img)
            os.remove(filename_img)

        return True
    except Exception as e:
        return e


@router.delete("/product/image", tags=["Produtos"])
def delete_image(id_image: str = Form()):
    try:
        cursor = mysql_connection.cursor(dictionary=True)
        cursor.execute("DELETE FROM IMAGE WHERE id = %s", (id_image,))
        mysql_connection.commit()
        return True
    except Exception as e:
        return e
    finally:
        cursor.close()


@router.post("/product/image", tags=["Produtos"])
def upload_images(id_product: str = Form(), files: List[UploadFile] = File()):
    try:
        cursor = mysql_connection.cursor(dictionary=True)
        filenames = []

        for file in files:
            filename = str(time.time()) + file.filename.replace(' ', '_')
            file_path = os.path.join(upload_folder, filename)
            filenames.append(str("public/product/" + filename))
            with open(file_path, "wb") as f:
                f.write(file.file.read())
            cursor.execute(
                "INSERT INTO image (id, id_product, path) VALUES (%s, %s, %s)",
                (str(uuid.uuid4()), id_product,
                 str("public/product/" + filename))
            )
            mysql_connection.commit()
        return filenames
    except Exception as e:
        return e
    finally:
        cursor.close()


@router.post("/product/description", tags=["Produtos"])
def create_description(description: new_description):
    try:
        cursor = mysql_connection.cursor(dictionary=True)

        cursor.execute(
            "INSERT INTO description_product (id_product, description_html) values (%s, %s)", (description.id_product, description.description))
        mysql_connection.commit()
        return True
    except Exception as e:
        return e
    finally:
        cursor.close()


@router.patch("/product/description", tags=["Produtos"])
def create_description(description: new_description):
    try:
        cursor = mysql_connection.cursor(dictionary=True)

        cursor.execute(
            "UPDATE description_product SET description_html = %s WHERE id_product = %s", (description.description, description.id_product))
        mysql_connection.commit()
        return True
    except Exception as e:
        return e
    finally:
        cursor.close()


@router.delete("/product/description", tags=["Produtos"])
def delete_description(id_product: str = Form()):
    try:
        cursor = mysql_connection.cursor(dictionary=True)
        cursor.execute(
            "DELETE FROM description_product WHERE id_product = %s", (id_product))
        mysql_connection.commit()
        return True
    except Exception as e:
        return e
    finally:
        cursor.close()
