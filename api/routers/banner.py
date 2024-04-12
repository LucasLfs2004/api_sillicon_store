from fastapi import HTTPException, APIRouter, UploadFile, File, Form, Depends
from dependencies import token
from database.connection import mysql_connection
import uuid
import time
import os

router = APIRouter()

upload_folder = "public/banner"
os.makedirs(upload_folder, exist_ok=True)


@router.get("/banner", tags=["Admin", "Banner"])
async def get_banners():
    try:
        cursor = mysql_connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM banner where active = 1")
        inserted_data = cursor.fetchall()

        # # Fechar o cursor e retornar o ID do produto
        cursor.close()
        return inserted_data
    except Exception as e:
        # Em caso de erro, cancelar a transação e retornar uma resposta de erro
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()


@router.post("/banner", tags=['Admin', 'Banner'])
# , current_user: int = Depends(token.is_admin)):
async def create_banner(link_redirect: str = Form(), image_web: UploadFile = File(), image_mobile: UploadFile = File()):
    try:
        cursor = mysql_connection.cursor(dictionary=True)
        id = int.from_bytes(
            uuid.uuid4().bytes[:4], byteorder="big") % (2 ** 30)

        filename_image_web = str(time.time()) + \
            image_web.filename.replace(' ', '_')
        file_path = os.path.join(upload_folder, filename_image_web)
        with open(file_path, "wb") as f:
            f.write(image_web.file.read())
        print(filename_image_web)
        filename_image_mobile = str(time.time()) + \
            image_mobile.filename.replace(' ', '_')
        file_path = os.path.join(upload_folder, filename_image_mobile)
        with open(file_path, "wb") as f:
            f.write(image_mobile.file.read())
        print(filename_image_mobile)

        cursor.execute(
            "INSERT INTO banner (id, img_banner_web, img_banner_mobile, link) VALUES (%s, %s, %s, %s)",
            (id, filename_image_web, filename_image_mobile, link_redirect)
        )

        mysql_connection.commit()

        # Realizar consulta para obter os dados inseridos
        cursor.execute("SELECT * FROM banner WHERE ID = %s", (id,))
        inserted_data = cursor.fetchone()
        cursor.close()
        # # Fechar o cursor e retornar o ID do produto
        return inserted_data
    except Exception as e:
        # Em caso de erro, cancelar a transação e retornar uma resposta de erro
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()


@ router.patch("/brand", tags=["Marca"])
async def update_brand(id: str = Form(), name: str = Form(None), brand_logo: UploadFile = File(None), brand_logo_black: UploadFile = File(None), current_user: int = Depends(token.is_admin)):
    try:
        cursor = mysql_connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM BRAND WHERE id = %s", (id,))
        old_brand = cursor.fetchone()

        new_brand = {}

        if name is not None:
            new_brand["name"] = name
        else:
            new_brand["name"] = old_brand['name']

        if brand_logo is not None:
            filename_brand_logo = str(time.time()) + \
                brand_logo.filename.replace(' ', '_')
            file_path = os.path.join(upload_folder, filename_brand_logo)
            with open(file_path, "wb") as f:
                f.write(brand_logo.file.read())
            print(filename_brand_logo)
            new_brand["brand_logo"] = str(filename_brand_logo)
        else:
            new_brand["brand_logo"] = old_brand["brand_logo"]

        if brand_logo_black is not None:
            filename_brand_logo_black = str(
                time.time()) + brand_logo_black.filename.replace(' ', '_')
            file_path = os.path.join(upload_folder, filename_brand_logo_black)
            with open(file_path, "wb") as f:
                f.write(brand_logo_black.file.read())
            print(filename_brand_logo_black)
            new_brand["brand_logo_black"] = str(filename_brand_logo_black)
        else:
            new_brand["brand_logo_black"] = old_brand["brand_logo_black"]

        cursor.execute(
            "UPDATE BRAND SET name = %s, brand_logo = %s, brand_logo_black = %s WHERE id = %s",
            (new_brand["name"], new_brand["brand_logo"],
             new_brand["brand_logo_black"], id)
        )
        mysql_connection.commit()

        print("Tudo certo até aqui, iniciando a exclusão das imagens antigas")

        # Removendo imagens antigas da api
        if brand_logo is not None:
            filename_logo = os.path.join(
                upload_folder + '/' + old_brand["brand_logo"])
            os.remove(filename_logo)
        if brand_logo_black is not None:
            filename_logo_black = os.path.join(
                update_brand + '/' + old_brand["brand_logo_black"])
            os.remove(filename_logo_black)

        cursor.execute("SELECT * FROM BRAND WHERE NAME = %s", (name,))
        brand_updated = cursor.fetchone()
        cursor.close()
        return True

    except Exception as e:
        print(e)
        return e


@ router.put("/brand", tags=["Marca"])
async def update_brand(id: str = Form(), name: str = Form(), brand_logo: UploadFile = File(), brand_logo_black: UploadFile = File()):
    try:
        cursor = mysql_connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM BRAND WHERE id = %s", (id,))
        old_brand = cursor.fetchone()

        filename_brand_logo = str(time.time()) + \
            brand_logo.filename.replace(' ', '_')
        file_path = os.path.join(upload_folder, filename_brand_logo)
        with open(file_path, "wb") as f:
            f.write(brand_logo.file.read())
        print(filename_brand_logo)
        filename_brand_logo_black = str(
            time.time()) + brand_logo_black.filename.replace(' ', '_')
        file_path = os.path.join(upload_folder, filename_brand_logo_black)
        with open(file_path, "wb") as f:
            f.write(brand_logo_black.file.read())
        print(filename_brand_logo_black)

        cursor.execute(
            "UPDATE BRAND SET name = %s, brand_logo = %s, brand_logo_black = %s WHERE id = %s",
            (name, filename_brand_logo, filename_brand_logo_black, id)
        )
        mysql_connection.commit()

        print("Tudo certo até aqui, iniciando a exclusão das imagens antigas")

        # Removendo imagens antigas da api
        filename_logo = os.path.join(
            upload_folder + "/" + old_brand["brand_logo"])
        os.remove(filename_logo)
        filename_logo_black = os.path.join(
            upload_folder + "/" + old_brand["brand_logo_black"])
        os.remove(filename_logo_black)
        mysql_connection.commit()

        cursor.execute("SELECT * FROM BRAND WHERE NAME = %s", (name,))
        brand_updated = cursor.fetchone()
        cursor.close()
        return brand_updated

    except Exception as e:
        print(e)
        return e


@ router.delete("/brand/{id}", tags=["Marca"])
async def delete_brand(id: str, current_user: int = Depends(token.is_admin)):
    try:
        cursor = mysql_connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM BRAND WHERE id = %s", (id,))
        data = cursor.fetchone()

        cursor.execute("DELETE FROM BRAND WHERE id LIKE %s", (id,))

        if data['brand_logo'] is not None:
            filename_logo = os.path.join(
                upload_folder + "/" + data["brand_logo"])
            os.remove(filename_logo)

        if data['brand_logo_black'] is not None:
            filename_logo_black = os.path.join(
                upload_folder + "/" + data["brand_logo_black"])
            os.remove(filename_logo_black)
        mysql_connection.commit()

        # # Fechar o cursor e retornar o ID do produto
        cursor.close()
        return True
    except Exception as e:
        # Em caso de erro, cancelar a transação e retornar uma resposta de erro
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))
