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
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()


@router.get("/banner/all", tags=["Admin", "Banner"])
async def get_banners():
    try:
        cursor = mysql_connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM banner")
        inserted_data = cursor.fetchall()

        # # Fechar o cursor e retornar o ID do produto
        cursor.close()
        return inserted_data
    except Exception as e:
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()


@router.post("/banner", tags=['Admin', 'Banner'])
async def create_banner(link_redirect: str = Form(), image_web: UploadFile = File(), image_mobile: UploadFile = File(), current_user: int = Depends(token.is_admin)):
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


@ router.patch("/banner", tags=["Admin", "Banner"])
async def update_brand(id: str = Form(), link_redirect: str = Form(None), image_web: UploadFile = File(None), image_mobile: UploadFile = File(None), active: str = Form(None), current_user: int = Depends(token.is_admin)):
    try:
        cursor = mysql_connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM banner WHERE id = %s", (id,))
        old_banner = cursor.fetchone()

        new_banner = {}

        print(old_banner['link'])
        print(link_redirect)
        if link_redirect is not None:
            new_banner["link"] = link_redirect
        else:
            new_banner["link"] = old_banner['link']

        print('passei pelo primeiro if')

        if active is not None:
            new_banner["active"] = True
        else:
            new_banner["active"] = old_banner['active']

        if image_web is not None:
            filename_image_web = str(time.time()) + \
                image_web.filename.replace(' ', '_')
            file_path = os.path.join(upload_folder, filename_image_web)
            with open(file_path, "wb") as f:
                f.write(image_web.file.read())
            print(filename_image_web)
            new_banner["img_banner_web"] = str(filename_image_web)
        else:
            new_banner["img_banner_web"] = old_banner["img_banner_web"]

        if image_mobile is not None:
            filename_image_mobile = str(
                time.time()) + image_mobile.filename.replace(' ', '_')
            file_path = os.path.join(upload_folder, filename_image_mobile)
            with open(file_path, "wb") as f:
                f.write(image_mobile.file.read())
            print(filename_image_mobile)
            new_banner["img_banner_mobile"] = str(filename_image_mobile)
        else:
            new_banner["img_banner_mobile"] = old_banner["img_banner_mobile"]

        cursor.execute(
            "UPDATE banner SET link = %s, img_banner_web = %s, img_banner_mobile = %s, active = %s WHERE id = %s",
            (new_banner["link"], new_banner["img_banner_web"],
             new_banner["img_banner_mobile"], new_banner["active"], id)
        )
        mysql_connection.commit()

        print("Tudo certo até aqui, iniciando a exclusão das imagens antigas")

        # Removendo imagens antigas da api
        if image_web is not None:
            filename_banner_web = os.path.join(
                upload_folder + '/' + old_banner["img_banner_web"])
            os.remove(filename_banner_web)
        if image_mobile is not None:
            filename_banner_mobile = os.path.join(
                update_brand + '/' + old_banner["img_banner_mobile"])
            os.remove(filename_banner_mobile)

        cursor.close()
        return True

    except Exception as e:
        # Em caso de erro, cancelar a transação e retornar uma resposta de erro
        mysql_connection.rollback()
        print(e)
        raise HTTPException(status_code=500, detail=str(e))


@ router.patch("/banner/active", tags=["Admin", "Banner"])
async def handle_active_banner(id: str):
    try:
        cursor = mysql_connection.cursor(dictionary=True)

        cursor.execute("SELECT active FROM banner WHERE id = %s", (id,))
        banner_data = cursor.fetchone()

        if banner_data['active'] == 0:
            cursor.execute(
                'UPDATE banner SET active = %s WHERE id = %s', (1, id))
        else:
            cursor.execute(
                'UPDATE banner SET active = %s WHERE id = %s', (0, id))

        mysql_connection.commit()
        return True

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))


@ router.delete("/banner/{id}", tags=["Admin", "Banner"])
async def delete_banner(id: str, current_user: int = Depends(token.is_admin)):
    try:
        cursor = mysql_connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM banner WHERE id = %s", (id,))
        data = cursor.fetchone()

        cursor.execute("DELETE FROM banner WHERE id = %s", (id,))

        if data['img_banner_web'] is not None:
            filename_logo = os.path.join(
                upload_folder + "/" + data["img_banner_web"])
            os.remove(filename_logo)

        if data['img_banner_mobile'] is not None:
            filename_logo_black = os.path.join(
                upload_folder + "/" + data["img_banner_mobile"])
            os.remove(filename_logo_black)
        mysql_connection.commit()

        # # Fechar o cursor e retornar o ID do produto
        cursor.close()
        return True
    except Exception as e:
        # Em caso de erro, cancelar a transação e retornar uma resposta de erro
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))
