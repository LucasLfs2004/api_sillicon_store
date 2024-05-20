from fastapi import APIRouter, HTTPException
from database.connection import mysql_connection
import uuid
import time
import os
from fastapi import HTTPException, APIRouter, UploadFile, File, Form
from models.models import new_comment

router = APIRouter()


@router.get("/comment/{id_product}", tags=["Comentários de produto"])
def get_comments(id_product: str):
    try:
        cursor = mysql_connection.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM comment WHERE id_product LIKE %s", (id_product,))
        inserted_data = cursor.fetchall()

        # # Fechar o cursor e retornar o ID do produto
        cursor.close()
        return inserted_data
    except Exception as e:
        # Em caso de erro, cancelar a transação e retornar uma resposta de erro
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/comment", tags=['Comentários de produto'])
def post_comment(comment: new_comment):
    try:
        cursor = mysql_connection.cursor(dictionary=True)
        id = str(uuid.uuid4())

        cursor.execute(
            "INSERT INTO comment (id_comment, id_product, title_text, comment_text, rating_value ) VALUES (%s, %s, %s, %s, %s)",
            (id, comment.id_product, comment.title, comment.comment, comment.rating)
        )

        mysql_connection.commit()

        cursor.execute("SELECT * FROM comment WHERE id_comment = %s", (id,))
        inserted_data = cursor.fetchone()

        cursor.close()
        return inserted_data
    except Exception as e:
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/comment", tags=["Comentários de produto"])
def delete_comment(id_comment: str = Form()):
    try:
        cursor = mysql_connection.cursor(dictionary=True)
        cursor.execute(
            "DELETE FROM COMMENT WHERE id_comment = %s", (id_comment,))
        mysql_connection.commit()
        cursor.close()

        return True

    except Exception as e:
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))
