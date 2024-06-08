import jwt
import datetime
import secrets
from fastapi import Depends, HTTPException, status
# from routers.person import oauth2_scheme
from typing import Optional
from fastapi.security import OAuth2PasswordBearer
from models.models import UserToken
from database.connection import mysql_connection

SECRET_KEY = secrets.token_hex(32)
ALGORITHM = 'HS256'

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

SECRET_KEY = '09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7'
ALGORITHM = 'HS256'


def generate_jwt_token(payload):
    # Defina o tempo de expiração do token, por exemplo, 1 hora a partir do momento atual.
    expiration = datetime.datetime.utcnow() + datetime.timedelta(hours=240)

    # Crie o payload do token com os dados do usuário
    token_payload = {
        'exp': expiration,
        # Aqui você pode adicionar outras informações sobre o usuário, como ID, nome, etc.
        **payload
    }

    # Gere o token utilizando a função jwt.encode()
    token = jwt.encode(token_payload, SECRET_KEY, algorithm=ALGORITHM)

    return token


def verify_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # id: str = payload.get("user_id")
        # token_data = UserToken(user_id=id)
        return payload
    except jwt.ExpiredSignatureError:
        # Token expirado
        raise HTTPException(status_code=401, detail=str('Token is expired'))
        # return {'error': 'Token de acesso expirado', 'status_code': 401}
    except Exception as e:
        print('error on verify_access_token')
        return e


def get_current_user(token: str = Depends(oauth2_scheme)):
    # credentials_exception = HTTPException(status_code=status.HTTP__UNAUTHORIZED,
    #                                       detail=f"Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})

    token = verify_access_token(token)

    # user = db.query(models.User).filter(models.User.id == token.id).first()
    return token['user_id']


def get_current_seller(token: str = Depends(oauth2_scheme)):
    # credentials_exception = HTTPException(status_code=status.HTTP__UNAUTHORIZED,
    #                                       detail=f"Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})

    token = verify_access_token(token)

    # user = db.query(models.User).filter(models.User.id == token.id).first()
    return token


def is_admin(token: str = Depends(oauth2_scheme)):
    token = verify_access_token(token)

    id_person = token['seller_id']

    cursor = mysql_connection.cursor()
    cursor.execute('SELECT admin FROM seller WHERE id = %s', (id_person,))
    data = cursor.fetchone()

    if data['admin'] == 1:
        return {'admin': True,
                'seller_id': id_person
                }
    else:
        raise HTTPException(status_code=401, detail=str('Unautorized'))
