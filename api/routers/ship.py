import uuid
from fastapi import HTTPException, APIRouter, Depends
from database.connection import mysql_connection
import json
from models.ship import ship_info_patch, ship_info_post
from dependencies import token
from requests.ship import get_ship_info_request
router = APIRouter()


@router.get('/ship-value/{region}', tags=['Prazo de entrega'])
async def set_ship_cart(region: str):
    try:
        cursor = mysql_connection.cursor()
        cursor.execute(
            "SELECT * FROM ship_value WHERE region = %s", (region,))
        data = cursor.fetchone()
        cursor.close()

        return data
    except Exception as e:
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.get('/ship-info', tags=["User", "Informações de entrega"])
async def get_ship_info(current_user: int = Depends(token.get_current_user)):
    try:
        cursor = mysql_connection.cursor()
        cursor.execute(get_ship_info_request, (current_user,))
        data = cursor.fetchone()
        cursor.close()
        return json.loads(data['ship'])
    except Exception as e:
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.post('/ship-info', tags=['User', "Informações de entrega"])
async def set_ship_info(ship: ship_info_post, current_user: int = Depends(token.get_current_user)):
    try:
        cursor = mysql_connection.cursor()
        id = int.from_bytes(
            uuid.uuid4().bytes[:4], byteorder="big") % (2 ** 32)
        cursor.execute('INSERT INTO ship_info (id, id_person, name, phone_number, district, cidade, estado, receiver, street, cep, complement, number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (
            id, current_user, ship.name, ship.phone_number, ship.district, ship.city, ship.state, ship.receiver, ship.street, ship.cep, ship.complement, ship.number))
        mysql_connection.commit()

        if ship.principal_ship:
            cursor.execute(
                'UPDATE person SET principal_ship_id = %s WHERE id = %s', (id, current_user))
            mysql_connection.commit()

        cursor.execute('SELECT * FROM ship_info where id = %s', (id, ))
        data = cursor.fetchone()

        cursor.close()
        return data

    except Exception as e:
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.patch('/ship-info', tags=['User', "Informações de entrega"])
async def set_ship_info(ship: ship_info_patch, current_user: int = Depends(token.get_current_user)):
    try:
        cursor = mysql_connection.cursor()
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


@router.delete('/ship-info/{id_ship}', tags=['User', "Informações de entrega"])
async def set_ship_info(id_ship: str, current_user: int = Depends(token.get_current_user)):
    try:
        cursor = mysql_connection.cursor()
        cursor.execute('DELETE FROM ship_info WHERE id = %s', (id_ship,))
        mysql_connection.commit()
        cursor.close()
        return True

    except Exception as e:
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))
