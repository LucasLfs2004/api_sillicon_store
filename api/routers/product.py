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
from requests.product import get_all_products, get_product_id, search_product_name, get_limit_products, get_limit_products_specific_brand
from functions.product import organize_images_from_products

router = APIRouter()

upload_folder = "public/product"
os.makedirs(upload_folder, exist_ok=True)


@router.get("/product", tags=['Produtos'])
async def get_products():
    try:
        cursor = mysql_connection.cursor(dictionary=True)

        cursor.execute(get_all_products)
        data = cursor.fetchall()
        products = []

        for product in data:
            dict_product = json.loads(product["product"])
            dict_product["images"] = sorted(dict_product["images"])
            products.append(dict_product)

        return products
    except Exception as e:
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/product/{limit}", tags=['Produtos'])
async def get_limited_products(limit: int):
    try:
        cursor = mysql_connection.cursor(dictionary=True)

        cursor.execute(get_limit_products, (limit,))
        data = cursor.fetchone()
        data = json.loads(data['products'])

        for product in data:
            images = organize_images_from_products(product=product)
            product['images'] = images

        return data
    except Exception as e:
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()


@router.get("/product/id/{product_id}", tags=['Produtos'])
async def search_product(product_id: str):
    try:
        cursor = mysql_connection.cursor(dictionary=True)

        cursor.execute(get_product_id, (product_id, ))
        data = cursor.fetchone()
        product = json.loads(data["product"])
        images = organize_images_from_products(product=product)
        product['images'] = images
        return product
    except Exception as e:
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/product/name/{product_name}", tags=['Produtos'])
async def search_product(product_name: str):
    try:
        cursor = mysql_connection.cursor(dictionary=True)

        search = str("%" + product_name + "%")

        cursor.execute(search_product_name,
                       (search, search))
        data = cursor.fetchone()
        data = json.loads(data['products'])

        for product in data:
            images = organize_images_from_products(product=product)
            product['images'] = images

        return data
    except Exception as e:
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/product", tags=['Produtos'])
async def create_product(name: str = Form(), brand_id: str = Form(), category_id: str = Form(),
                         price: str = Form(), portions: str = Form(), fees_monthly: str = Form(), fees_credit: str = Form(), stock: str = Form(), featured: str = Form(), warranty: str = Form(), model: str = Form(None), description: str = Form(None), files: List[UploadFile] = File(...), user=Depends(token.get_current_seller)):
    filenames = []
    product = {
        'id': int.from_bytes(uuid.uuid4().bytes[:4], byteorder="big") % (2 ** 32),
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
        cursor = mysql_connection.cursor(dictionary=True)

        cursor.execute("INSERT INTO product (id, seller_id, name, brand_id, category_id, stock, warranty, active, featured, model) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                       (product['id'], user['seller_id'], product['name'], product['brand_id'], product['category_id'], product['stock'], product['warranty'], product['active'], product['featured'], product['model']))
        mysql_connection.commit()
        cursor.execute(
            "INSERT INTO value_product (id, id_product, common_price, portions, fees_monthly, fees_credit) VALUES (%s, %s, %s, %s, %s, %s)",
            (str(uuid.uuid4()), product['id'], float(price), int(portions), float(fees_monthly), float(fees_credit)))

        # Fechar o cursor e retornar o ID do produto
        for index, file in enumerate(files):
            filename = str(time.time()) + file.filename.replace(' ', '_')
            filenames.append(filename)
            file_path = os.path.join(upload_folder, filename)
            with open(file_path, "wb") as f:
                f.write(file.file.read())
            cursor.execute(
                "INSERT INTO image (id, id_product, path, index_image) VALUES (%s, %s, %s, %s)",
                (str(uuid.uuid4()), product['id'], filename, index)
            )

        cursor.execute(
            "INSERT INTO rating (id, id_product, amount, rating) VALUES (%s, %s, %s, %s)",
            (product['id'], product['id'], int(0), int(0))
        )
        mysql_connection.commit()

        if description is not None:
            cursor.execute('INSERT INTO description_product (id_description, id_product, description_html) VALUES (%s, %s, %s)',
                           (int.from_bytes(uuid.uuid4().bytes[:4], byteorder="big") % (2 ** 32), product['id'], description))
            mysql_connection.commit()

        cursor.close()
        return True
    except Exception as e:
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()


@router.delete('/product/{id_product}', tags=['Produtos'])
async def delete_product(id_product: str, current_user: int = Depends(token.get_current_user)):
    try:
        cursor = mysql_connection.cursor(dictionary=True)

        cursor.execute(
            "SELECT image.path FROM image WHERE image.id_product LIKE %s", (
                id_product,)
        )
        data = cursor.fetchall()
        cursor.execute(
            "DELETE FROM product WHERE product.id = %s", (id_product,))
        mysql_connection.commit()

        for filename in data:
            filename_img = os.path.join(upload_folder + "/" + filename["path"])
            os.remove(filename_img)

        cursor.close()
        return True
    except Exception as e:
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.delete('/product', tags=['Produtos'])
async def delete_product(id_product: str = Form()):
    try:
        cursor = mysql_connection.cursor(dictionary=True)

        cursor.execute(
            "SELECT image.path FROM image WHERE image.id_product LIKE %s", (
                id_product,)
        )
        data = cursor.fetchall()
        cursor.execute("DELETE FROM product where id LIKE %s", (id_product,))
        mysql_connection.commit()

        for filename in data:
            filename_img = os.path.join(filename["path"])
            os.remove(filename_img)

        return True
    except Exception as e:
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.put('/product', tags=['Produtos'])
async def update_product(product: update_product_model, user=Depends(token.get_current_seller)):
    try:
        cursor = mysql_connection.cursor(dictionary=True)
        cursor.execute('UPDATE product SET name = %s, brand_id = %s, category_id = %s, stock = %s, warranty = %s, active = %s, model = %s, featured = %s where id = %s and seller_id = %s',
                       (product.name, product.brand, product.category, product.stock, product.warranty, product.active, product.model, product.featured, product.id, user['seller_id']))
        mysql_connection.commit()

        cursor.execute('UPDATE value_product SET common_price = %s, portions = %s, fees_monthly = %s, fees_credit = %s WHERE id_product = %s',
                       (product.price, product.portions, product.fees_monthly, product.fees_credit, product.id))
        mysql_connection.commit()
        return True
    except Exception as e:
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/product/image", tags=["Produtos"])
async def delete_image(id_image: str = Form()):
    try:
        cursor = mysql_connection.cursor(dictionary=True)
        cursor.execute("DELETE FROM IMAGE WHERE id = %s", (id_image,))
        mysql_connection.commit()
        return True
    except Exception as e:
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()


@router.post("/product/image", tags=["Produtos"])
async def upload_images(id_product: str = Form(), files: List[UploadFile] = File()):
    try:
        cursor = mysql_connection.cursor(dictionary=True)
        filenames = []

        for file in files:
            filename = str(time.time()) + file.filename.replace(' ', '_')
            file_path = os.path.join(upload_folder, filename)
            filenames.append(filename)
            with open(file_path, "wb") as f:
                f.write(file.file.read())
            cursor.execute(
                "INSERT INTO image (id, id_product, path) VALUES (%s, %s, %s)",
                (str(uuid.uuid4()), id_product,
                 filename)
            )
            mysql_connection.commit()
        return filenames
    except Exception as e:
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()


@router.patch("/product/image", tags=["Produtos"])
async def upload_images(id_product: str = Form(), new_files: List[UploadFile] = File(default=[]), files_to_delete: List[str] = Form(default=[]), indexed_files: List[str] = Form(default=[])):
    try:
        entrada = {'NEW_FILES': new_files,
                   "ID_PRODUCT": id_product,
                   'FILES_TO_DELETE': files_to_delete,
                   'FILES_TO_KEEP': indexed_files
                   }

        cursor = mysql_connection.cursor(dictionary=True)

        # Exclusão das imagens
        for filename in files_to_delete:
            cursor.execute("SELECT * FROM IMAGE WHERE path = %s", (filename,))
            filename_db = cursor.fetchone()

            if filename_db is not None:
                cursor.execute(
                    "DELETE FROM image WHERE image.path = %s", (filename,))
                mysql_connection.commit()

                filename_img = os.path.join(upload_folder + "/" + filename)
                os.remove(filename_img)

        ##########################
        mysql_connection.commit()

        # Inserção de novas imagens no Banco
        filenames = []
        for file in new_files:
            filename = str(time.time()) + file.filename.replace(' ', '_')
            filenames.append(filename)
            file_path = os.path.join(upload_folder, filename)
            with open(file_path, "wb") as f:
                f.write(file.file.read())
            cursor.execute(
                "INSERT INTO image (id, id_product, path) VALUES (%s, %s, %s)",
                (str(uuid.uuid4()), id_product, filename)
            )
        ##########################

        mysql_connection.commit()
        for index, item in enumerate(indexed_files):
            cursor.execute(
                'UPDATE image SET index_image = %s WHERE path = %s', (index, item))
        mysql_connection.commit()
        return True
    except Exception as e:
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/product/description", tags=["Produtos"])
async def create_description(description: new_description):
    try:
        cursor = mysql_connection.cursor(dictionary=True)

        cursor.execute(
            "INSERT INTO description_product (id_product, description_html) values (%s, %s)", (description.id_product, description.description))
        mysql_connection.commit()
        return True
    except Exception as e:
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()


@router.patch("/product/description", tags=["Produtos"])
async def create_description(description: new_description):
    try:
        cursor = mysql_connection.cursor(dictionary=True)

        cursor.execute(
            "UPDATE description_product SET description_html = %s WHERE id_product = %s", (description.description, description.id_product))
        mysql_connection.commit()
        return True
    except Exception as e:
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()


@router.delete("/product/description", tags=["Produtos"])
async def delete_description(id_product: str = Form()):
    try:
        cursor = mysql_connection.cursor(dictionary=True)
        cursor.execute(
            "DELETE FROM description_product WHERE id_product = %s", (id_product))
        mysql_connection.commit()
        return True
    except Exception as e:
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()


@router.get("/product/brand/{brand_id}", tags=['Produtos', 'Marca'])
async def get_products_specif_brand(brand_id: str):
    try:
        cursor = mysql_connection.cursor(dictionary=True)
        cursor.execute(
            get_limit_products_specific_brand, (brand_id, 40)
        )
        data = cursor.fetchone()

        data = json.loads(data['products'])

        for product in data:
            images = organize_images_from_products(product=product)
            product['images'] = images

        cursor.execute(
            "select name as brand_name, brand_logo, brand_logo_black from brand where id = %s", (brand_id,))
        brand = cursor.fetchone()

        brand['products'] = data

        return brand
    except Exception as e:
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))
