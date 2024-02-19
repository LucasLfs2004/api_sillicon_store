import uuid
from fastapi import HTTPException, APIRouter, Form, Depends
from database.connection import mysql_connection
import json
from models.models import new_cart, update_cart, apply_discount, ship_cart, id_model
from dependencies import token
from requests.cart import select_complete_cart
from functions.cart import organize_response_cart

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
