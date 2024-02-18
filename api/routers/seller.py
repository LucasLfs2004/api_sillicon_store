from fastapi import APIRouter
from database.connection import mysql_connection
from fastapi import HTTPException, Form, status, Depends
from models.models import new_account, effect_login, UserToken
from dependencies.token import generate_jwt_token
import bcrypt
from typing import Optional
import uuid
import jwt
import json
from dependencies import token, formatters
from requests.seller import get_seller_data
from fastapi.security import OAuth2AuthorizationCodeBearer
import secrets

router = APIRouter()


# @router.get("/seller", tags=['User'])
# def get_persons():
#     cursor = mysql_connection.cursor(dictionary=True)
#     cursor.execute(get_persons_query)
#     person = cursor.fetchall()
#     cursor.close()
#     return person


@router.get("/seller/me", tags=['Seller'])
async def get_data_user(current_user: int = Depends(token.get_current_user)):
    try:
        print(current_user)
        cursor = mysql_connection.cursor(dictionary=True)
        cursor.execute(get_seller_data, (current_user,))
        profile_data = cursor.fetchone()
        print(profile_data)
        # profile_data['cpf'] = formatters.format_cpf(profile_data['cpf'])
        cursor.close()
        return json.loads(profile_data['seller'])

    except Exception as e:
        print(e)
        return e
