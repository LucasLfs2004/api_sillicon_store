from fastapi import HTTPException, APIRouter, UploadFile, File, Form, Depends
from models.models import new_category
from dependencies import token
from database.connection import mysql_connection
import uuid
import time
import os

router = APIRouter()

upload_folder = "public/category"
os.makedirs(upload_folder, exist_ok=True)


@router.get("/category", tags=["Categoria"])
async def get_categorys():
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
async def create_category(name: str = Form(), path_img: UploadFile = File(None), current_user: int = Depends(token.is_admin)):
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
        cursor.execute("SELECT * FROM category WHERE NAME = %s",
                       (name,))
        inserted_data = cursor.fetchone()

        # # Fechar o cursor e retornar o ID do produto
        cursor.close()
        return inserted_data

    except Exception as e:
        # Em caso de erro, cancelar a transação e retornar uma resposta de erro
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.patch("/category", tags=["Categoria"])
async def update_category(id: str = Form(), name: str = Form(None), path_img: UploadFile = File(None), current_user: int = Depends(token.is_admin)):
    try:
        cursor = mysql_connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM CATEGORY WHERE id = %s", (id,))
        old_category = cursor.fetchone()

        new_category = {}

        if name is not None:
            new_category["name"] = name
        else:
            new_category['name'] = old_category['name']

        if path_img is not None:
            filename_path_img = str(time.time()) + \
                path_img.filename.replace(' ', '_')
            file_path = os.path.join(upload_folder, filename_path_img)
            with open(file_path, "wb") as f:
                f.write(path_img.file.read())
            print(filename_path_img)
            new_category["path_img"] = filename_path_img

            if old_category['path_img'] is not None:
                filename_img = os.path.join(
                    upload_folder + "/" + old_category['path_img'])
                print(filename_img)
                os.remove(filename_img)

        else:
            new_category["path_img"] = old_category["path_img"]

        cursor.execute(
            "UPDATE CATEGORY SET name = %s, path_img = %s WHERE id = %s",
            (new_category["name"], new_category["path_img"], id)
        )
        mysql_connection.commit()

        print("Tudo certo até aqui, iniciando a exclusão das imagens antigas")
        cursor.close()
        return True

    except Exception as e:
        print(e)
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/category/{id}", tags=["Categoria"])
async def delete_category(id: str, current_user: int = Depends(token.is_admin)):
    try:
        cursor = mysql_connection.cursor(dictionary=True)
        print("Executando select")
        cursor.execute("SELECT * FROM CATEGORY WHERE id = %s",
                       (id,))
        category_delete = cursor.fetchone()
        print("executando DELETE")
        cursor.execute("DELETE FROM CATEGORY WHERE id LIKE %s", (id,)),
        mysql_connection.commit()

        print(category_delete)
        if category_delete["path_img"] is not None:
            filename_logo = os.path.join(
                upload_folder + "/" + category_delete["brand_logo"])
            os.remove(filename_logo)

        cursor.close()
        print(True)
        return True

    except Exception as e:
        cursor.close()
        print(e)
        return e
