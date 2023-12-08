from fastapi import APIRouter, HTTPException
from models.models import new_category
from database.connection import mysql_connection
import uuid
import time
import os
from fastapi import HTTPException, APIRouter, UploadFile, File, Form

router = APIRouter()

upload_folder = "public/category"
os.makedirs(upload_folder, exist_ok=True)


@router.get("/category", tags=["Categoria"])
def get_categorys():
    try:
        cursor = mysql_connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM category")
        categorys = cursor.fetchall()

        cursor.close()
        return categorys
    except Exception as e:
        cursor.close()
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/category", tags=['Categoria'])
def create_category(name: str = Form(), path_img: UploadFile = File(None)):
    try:
        cursor = mysql_connection.cursor(dictionary=True)
        id = int.from_bytes(
            uuid.uuid4().bytes[:4], byteorder="big") % (2 ** 30)

        if path_img is not None:
            filename_category = str(time.time()) + \
                path_img.filename.replace(' ', '_')
            file_path = os.path.join(upload_folder, filename_category)
            with open(file_path, "wb") as f:
                f.write(path_img.file.read())
            print(filename_category)
            cursor.execute("INSERT INTO CATEGORY (id, name, path_img) VALUES (%s, %s, %s)",
                           (id, name, str("public/category/" + filename_category,)))
        else:
            cursor.execute("INSERT INTO CATEGORY (id, name) VALUES (%s, %s)",
                           (id, name,))
        mysql_connection.commit()

        # Realizar consulta para obter os dados inseridos
        cursor.execute("SELECT * FROM category WHERE NAME = %s", (name,))
        inserted_data = cursor.fetchone()

        # # Fechar o cursor e retornar o ID do produto
        cursor.close()
        return inserted_data

    except Exception as e:
        # Em caso de erro, cancelar a transação e retornar uma resposta de erro
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.patch("/category", tags=["Categoria"])
def update_category(old_name: str = Form(), name: str = Form(None), path_img: UploadFile = File(None)):
    try:
        cursor = mysql_connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM CATEGORY WHERE NAME = %s", (old_name,))
        old_category = cursor.fetchone()

        new_category = {}

        if name is not None:
            new_category["name"] = name
        else:
            new_category["name"] = old_name

        if path_img is not None:
            filename_path_img = str(time.time()) + \
                path_img.filename.replace(' ', '_')
            file_path = os.path.join(upload_folder, filename_path_img)
            with open(file_path, "wb") as f:
                f.write(path_img.file.read())
            print(filename_path_img)
            new_category["path_img"] = str(
                'public/brand/' + filename_path_img)
        else:
            new_category["path_img"] = old_category["path_img"]

        cursor.execute(
            "UPDATE CATEGORY SET name = %s, path_img = %s WHERE name = %s",
            (new_category["name"], new_category["path_img"], old_name)
        )
        mysql_connection.commit()

        print("Tudo certo até aqui, iniciando a exclusão das imagens antigas")

        # Removendo imagens antigas da api
        if path_img is not None:
            filename_logo = os.path.join(old_category["path_img"])
            os.remove(filename_logo)

        cursor.execute("SELECT * FROM CATEGORY WHERE NAME = %s", (name,))
        category_updated = cursor.fetchone()
        cursor.close()
        return category_updated

    except Exception as e:
        print(e)
        return e


@router.delete("/category", tags=["Categoria"])
def delete_category(name: str = Form()):
    try:
        cursor = mysql_connection.cursor(dictionary=True)
        print("Executando select")
        cursor.execute("SELECT * FROM CATEGORY WHERE NAME = %s",
                       (name,))
        category_delete = cursor.fetchone()
        print("executando DELETE")
        cursor.execute("DELETE FROM CATEGORY WHERE NAME LIKE %s", (name,)),
        mysql_connection.commit()

        print(category_delete)
        if category_delete["path_img"] is not None:
            filename_logo = os.path.join(category_delete["brand_logo"])
            os.remove(filename_logo)

        cursor.close()
        return True

    except Exception as e:
        cursor.close()
        print(e)
        return e
