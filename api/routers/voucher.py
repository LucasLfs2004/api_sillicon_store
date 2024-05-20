from fastapi import APIRouter, HTTPException, Depends, Form
from database.connection import mysql_connection
import uuid
from models.voucher import new_voucher
from dependencies.token import is_admin


router = APIRouter()


# current_user: int = Depends(is_admin)

@router.get("/voucher", tags=['Cupom de desconto', "Admin"])
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


@router.post("/voucher", tags=['Cupom de desconto', 'Admin'])
def post_discount(voucher: new_voucher):
    try:
        cursor = mysql_connection.cursor(dictionary=True)
        cursor.execute(
            "INSERT INTO discount_list (code, discount, expire_at, min_value ) VALUES (%s, %s, FROM_UNIXTIME(%s), %s)",
            (voucher.code, voucher.discount,
             voucher.expiration, voucher.min_value)
        )

        mysql_connection.commit()

        # Realizar consulta para obter os dados inseridos
        cursor.execute("SELECT * FROM discount_list WHERE code = %s",
                       (voucher.code,))
        inserted_data = cursor.fetchone()

        # # Fechar o cursor e retornar o ID do produto
        cursor.close()
        return inserted_data
    except Exception as e:
        # Em caso de erro, cancelar a transação e retornar uma resposta de erro
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/voucher/{code}", tags=["Cupom de desconto", 'Admin'])
def delete_discount(code: str):
    try:
        cursor = mysql_connection.cursor(dictionary=True)
        cursor.execute(
            "DELETE FROM discount_list WHERE code = %s", (code,))
        mysql_connection.commit()

        return True
    except Exception as e:
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        cursor.close()
