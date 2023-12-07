from fastapi import APIRouter, HTTPException
from models.models import new_category
from database.connection import mysql_connection
import uuid
import time
import os
from fastapi import HTTPException, APIRouter, UploadFile, File, Form

router = APIRouter()

upload_folder = "public/brand"


@router.get("/brand", tags=["Marca"])
def get_brand():
    try:
        cursor = mysql_connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM BRAND")
        inserted_data = cursor.fetchall()

        # # Fechar o cursor e retornar o ID do produto
        cursor.close()
        return inserted_data
    except Exception as e:
        # Em caso de erro, cancelar a transação e retornar uma resposta de erro
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/brand", tags=['Marca'])
def create_brand(name: str = Form(), brand_logo: UploadFile = File(None), brand_logo_black: UploadFile = File(None)):
    try:
        cursor = mysql_connection.cursor(dictionary=True)
        id = int.from_bytes(
            uuid.uuid4().bytes[:4], byteorder="big") % (2 ** 30)
        if brand_logo is not None:
            filename_brand_logo = str(time.time()) + \
                brand_logo.filename.replace(' ', '_')
            file_path = os.path.join(upload_folder, filename_brand_logo)
            with open(file_path, "wb") as f:
                f.write(brand_logo.file.read())
            print(filename_brand_logo)
        if brand_logo_black is not None:
            filename_brand_logo_black = str(
                time.time()) + brand_logo_black.filename.replace(' ', '_')
            file_path = os.path.join(upload_folder, filename_brand_logo_black)
            with open(file_path, "wb") as f:
                f.write(brand_logo_black.file.read())
            print(filename_brand_logo_black)

        if brand_logo is not None and brand_logo_black is not None:
            cursor.execute(
                "INSERT INTO BRAND (id, name, brand_logo, brand_logo_black) VALUES (%s, %s, %s, %s)",
                (id, name, str('public/brand/' + filename_brand_logo),
                 str('public/brand/' + filename_brand_logo_black))
            )
        elif brand_logo is None and brand_logo_black is not None:
            cursor.execute(
                "INSERT INTO BRAND (id, name, brand_logo_black) VALUES (%s, %s, %s)",
                (id, name, str('public/brand/' + filename_brand_logo_black))
            )
        elif brand_logo is not None and brand_logo_black is None:
            cursor.execute(
                "INSERT INTO BRAND (id, name, brand_logo) VALUES (%s, %s, %s)",
                (id, name, str('public/brand/' + filename_brand_logo))
            )
        else:
            cursor.execute(
                "INSERT INTO BRAND (id, name) VALUES (%s, %s)",
                (id, name,)
            )

        mysql_connection.commit()

        # Realizar consulta para obter os dados inseridos
        cursor.execute("SELECT * FROM brand WHERE ID = %s", (id,))
        inserted_data = cursor.fetchone()

        # # Fechar o cursor e retornar o ID do produto
        cursor.close()
        return {"new_category:": inserted_data}
    except Exception as e:
        # Em caso de erro, cancelar a transação e retornar uma resposta de erro
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.patch("/brand", tags=["Marca"])
def update_brand(old_name: str = Form(), name: str = Form(None), brand_logo: UploadFile = File(None), brand_logo_black: UploadFile = File(None)):
    try:
        cursor = mysql_connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM BRAND WHERE NAME = %s", (old_name,))
        old_brand = cursor.fetchone()

        new_brand = {}

        if name is not None:
            new_brand["name"] = name
        else:
            new_brand["name"] = old_name

        if brand_logo is not None:
            filename_brand_logo = str(time.time()) + \
                brand_logo.filename.replace(' ', '_')
            file_path = os.path.join(upload_folder, filename_brand_logo)
            with open(file_path, "wb") as f:
                f.write(brand_logo.file.read())
            print(filename_brand_logo)
            new_brand["brand_logo"] = str(
                'public/brand/' + filename_brand_logo)
        else:
            new_brand["brand_logo"] = old_brand["brand_logo"]

        if brand_logo_black is not None:
            filename_brand_logo_black = str(
                time.time()) + brand_logo_black.filename.replace(' ', '_')
            file_path = os.path.join(upload_folder, filename_brand_logo_black)
            with open(file_path, "wb") as f:
                f.write(brand_logo_black.file.read())
            print(filename_brand_logo_black)
            new_brand["brand_logo_black"] = str(
                'public/brand/' + filename_brand_logo_black)
        else:
            new_brand["brand_logo_black"] = old_brand["brand_logo_black"]

        cursor.execute(
            "UPDATE BRAND SET name = %s, brand_logo = %s, brand_logo_black = %s WHERE name = %s",
            (new_brand["name"], new_brand["brand_logo"],
             new_brand["brand_logo_black"], old_name)
        )
        mysql_connection.commit()

        print("Tudo certo até aqui, iniciando a exclusão das imagens antigas")

        # Removendo imagens antigas da api
        if brand_logo is not None:
            filename_logo = os.path.join(old_brand["brand_logo"])
            os.remove(filename_logo)
        if brand_logo_black is not None:
            filename_logo_black = os.path.join(old_brand["brand_logo_black"])
            os.remove(filename_logo_black)

        cursor.execute("SELECT * FROM BRAND WHERE NAME = %s", (name,))
        brand_updated = cursor.fetchone()
        cursor.close()
        return brand_updated

    except Exception as e:
        print(e)
        return e


@router.put("/brand", tags=["Marca"])
def update_brand(old_name: str = Form(), name: str = Form(), brand_logo: UploadFile = File(), brand_logo_black: UploadFile = File()):
    try:
        cursor = mysql_connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM BRAND WHERE NAME = %s", (old_name,))
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
            "UPDATE BRAND SET name = %s, brand_logo = %s, brand_logo_black = %s WHERE name = %s",
            (name, str("public/brand/" + filename_brand_logo),
             str("public/brand/" + filename_brand_logo_black), old_name)
        )
        mysql_connection.commit()

        print("Tudo certo até aqui, iniciando a exclusão das imagens antigas")

        # Removendo imagens antigas da api
        filename_logo = os.path.join(old_brand["brand_logo"])
        os.remove(filename_logo)
        filename_logo_black = os.path.join(old_brand["brand_logo_black"])
        os.remove(filename_logo_black)
        mysql_connection.commit()

        cursor.execute("SELECT * FROM BRAND WHERE NAME = %s", (name,))
        brand_updated = cursor.fetchone()
        cursor.close()
        return brand_updated

    except Exception as e:
        print(e)
        return e


@router.delete("/brand", tags=["Marca"])
def delete_brand(name: str = Form()):
    try:
        cursor = mysql_connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM BRAND WHERE NAME = %s", (name,))
        data = cursor.fetchone()

        cursor.execute("DELETE FROM BRAND WHERE NAME LIKE %s", (name,))

        filename_logo = os.path.join(data["brand_logo"])

        os.remove(filename_logo)
        filename_logo_black = os.path.join(data["brand_logo_black"])
        os.remove(filename_logo_black)
        mysql_connection.commit()

        # # Fechar o cursor e retornar o ID do produto
        cursor.close()
        return True
    except Exception as e:
        # Em caso de erro, cancelar a transação e retornar uma resposta de erro
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))
