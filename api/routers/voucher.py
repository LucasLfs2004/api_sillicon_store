from fastapi import APIRouter, HTTPException, Depends, Form
from database.connection import mysql_connection
import uuid
from models.voucher import new_voucher
from dependencies.token import is_admin


router = APIRouter()


# current_user: int = Depends(is_admin)

@router.get("/voucher", tags=["Admin"])
def get_vouchers_of_discounts():
    try:
        cursor = mysql_connection.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM discount_list")
        inserted_data = cursor.fetchall()

        cursor.close()
        return inserted_data
    except Exception as e:
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/voucher", tags=['Comentários de produto'])
def post_comment(voucher: new_voucher):
    try:
        cursor = mysql_connection.cursor(dictionary=True)
        cursor.execute(
            "INSERT INTO discount_list (code, id_product, title_text, comment_text, rating_value ) VALUES (%s, %s, %s, %s, %s)",
            (id, comment.id_product, comment.title, comment.comment, comment.rating)
        )

        mysql_connection.commit()

        # Realizar consulta para obter os dados inseridos
        cursor.execute("SELECT * FROM comment WHERE id_comment = %s", (id,))
        inserted_data = cursor.fetchone()

        # # Fechar o cursor e retornar o ID do produto
        cursor.close()
        return inserted_data
    except Exception as e:
        # Em caso de erro, cancelar a transação e retornar uma resposta de erro
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/comment", tags=["Comentários de produto"])
def delete_comment(id_comment: str = Form()):
    try:
        cursor = mysql_connection.cursor(dictionary=True)
        cursor.execute(
            "DELETE FROM COMMENT WHERE id_comment = %s", (id_comment,))
        mysql_connection.commit()

        return True

    except Exception as e:
        return e

    finally:
        cursor.close()
