from fastapi import APIRouter, HTTPException, Depends
from database.connection import mysql_connection
from models.voucher import new_voucher
from dependencies.token import is_admin

router = APIRouter()

@router.get("/voucher", tags=['Cupom de desconto', "Admin"])
async def get_vouchers_of_discounts(current_user: int = Depends(is_admin)):
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
async def post_discount(voucher: new_voucher, current_user: int = Depends(is_admin)):
    try:
        cursor = mysql_connection.cursor(dictionary=True)
        cursor.execute(
            "INSERT INTO discount_list (code, discount, expire_at, min_value ) VALUES (%s, %s, FROM_UNIXTIME(%s), %s)",
            (voucher.code, voucher.discount,
             voucher.expiration, voucher.min_value)
        )

        mysql_connection.commit()

        cursor.close()
        return True
    except Exception as e:
        # Em caso de erro, cancelar a transação e retornar uma resposta de erro
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/voucher/{code}", tags=["Cupom de desconto", 'Admin'])
async def delete_discount(code: str, current_user: int = Depends(is_admin)):
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
