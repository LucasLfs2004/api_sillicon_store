import uuid
from fastapi import HTTPException, APIRouter, Form, Depends
from database.connection import mysql_connection
import json
from models.ship import ship_info_patch, ship_info_post
from dependencies import token
router = APIRouter()


@router.get('/ship-value/{region}', tags=['Prazo de entrega'])
async def set_ship_cart(region: str):
    try:
        cursor = mysql_connection.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM ship_value WHERE region = %s", (region,))
        data = cursor.fetchone()

        return data
    except Exception as e:
        return e


@router.post('/ship-info', tags=['User'])
async def set_ship_info(ship: ship_info_post, current_user: int = Depends(token.get_current_user)):
    try:
        cursor = mysql_connection.cursor(dictionary=True)
        id = int.from_bytes(
            uuid.uuid4().bytes[:4], byteorder="big") % (2 ** 32)
        cursor.execute('INSERT INTO ship_info (id, id_person, name, phone_number, district, cidade, estado, receiver, street, cep, complement, number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (
            id, current_user, ship.name, ship.phone_number, ship.district, ship.city, ship.state, ship.receiver, ship.street, ship.cep, ship.complement, ship.number))
        mysql_connection.commit()

        if ship.principal_ship:
            cursor.execute(
                'UPDATE person SET principal_ship_id = %s WHERE id = %s', (id, current_user))
            mysql_connection.commit()
        cursor.close()
        return True

    except Exception as e:
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.patch('/ship-info', tags=['User'])
async def set_ship_info(ship: ship_info_patch, current_user: int = Depends(token.get_current_user)):
    try:
        cursor = mysql_connection.cursor(dictionary=True)
        cursor.execute('UPDATE ship_info SET name = %s, phone_number = %s, district = %s, cidade = %s, estado = %s, receiver = %s, street = %s, cep = %s, complement = %s, number = %s WHERE id = %s and id_person = %s', (
            ship.name, ship.phone_number, ship.district, ship.city, ship.state, ship.receiver, ship.street, ship.cep, ship.complement, ship.number, ship.id, current_user))
        mysql_connection.commit()

        if ship.principal_ship:
            cursor.execute(
                'UPDATE person SET principal_ship_id = %s WHERE id = %s', (ship.id, current_user))
            mysql_connection.commit()
        cursor.close()
        return True

    except Exception as e:
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.delete('/ship-info/{id_ship}', tags=['User'])
async def set_ship_info(id_ship: str, current_user: int = Depends(token.get_current_user)):
    try:
        cursor = mysql_connection.cursor(dictionary=True)
        cursor.execute('DELETE FROM ship_info WHERE id = %s', (id_ship,))
        mysql_connection.commit()
        cursor.close()
        return True

    except Exception as e:
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))
