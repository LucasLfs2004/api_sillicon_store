from database.connection import mysql_connection
from fastapi import HTTPException, Depends, APIRouter
from models.models import new_account, effect_login, UserToken, id_ship
from dependencies.token import generate_jwt_token
import bcrypt
import uuid
import json
from dependencies import token, formatters
from requests.person import get_persons_query, get_person_id_query, get_user_profile
from functions.product import organize_images_from_products

router = APIRouter()


@router.get("/person", tags=['User'])
def get_persons():
    cursor = mysql_connection.cursor(dictionary=True)
    cursor.execute(get_persons_query)
    person = cursor.fetchall()
    cursor.close()
    return person


@router.get("/person/me", tags=['User'])
async def get_data_user(current_user: int = Depends(token.get_current_user)):
    cursor = mysql_connection.cursor(dictionary=True)
    try:
        cursor.execute(get_user_profile, (current_user,))
        profile_data = cursor.fetchone()

        data = json.loads(profile_data['person'])

        for product in data['last_order']['items']:
            images = organize_images_from_products(product=product)
            product['images'] = images

        # profile_data['cpf'] = formatters.format_cpf(profile_data['cpf'])
        return data

    except Exception as e:
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()


@router.post("/login", tags=['User'])
async def login_user(login: effect_login):
    try:

        cursor = mysql_connection.cursor(dictionary=True)
        cursor.execute(get_person_id_query, (login.email.strip().lower(),))
        person = cursor.fetchone()
        # cursor.close

        if person is None:
            raise HTTPException(
                status_code=401, detail="Usuário não encontrado")

        if bcrypt.checkpw(login.password.encode("utf-8"), person["password"].encode("utf-8")):
            person.pop("password", None)
            token = generate_jwt_token(
                {'user_id': person["id"], 'seller_id': person['id_seller']})
            return {"access_token": token,
                    "person": person}
        else:
            raise HTTPException(status_code=401, detail="Senha incorreta")
    except Exception as e:
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/create-account", tags=['User'])
def create_account(account: new_account):
    try:
        cursor = mysql_connection.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM PERSON WHERE CPF LIKE %s OR EMAIL LIKE %s", (account.cpf, account.email))
        persons = cursor.fetchall()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    print(persons)
    cpfValid = True
    emailValid = True
    for person in persons:
        if person['cpf'] == account.cpf:
            cpfValid = False
        if person['email'] == account.email:
            emailValid = False

    if not cpfValid and not emailValid:
        cursor.close()
        raise HTTPException(
            status_code=409, detail="O CPF e email inseridos já possuem cadastro")
    elif not cpfValid and emailValid:
        cursor.close()
        raise HTTPException(
            status_code=409, detail="O CPF inserido já está cadastrado")
    elif cpfValid and not emailValid:
        cursor.close()
        raise HTTPException(
            status_code=409, detail="O email inserido já está cadastrado")

    try:
        # Conectar ao banco de dados
        cursor = mysql_connection.cursor(dictionary=True)

        # Codificação de senha
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(account.password.encode("utf-8"), salt)
        account.password = hashed_password

        id = str(uuid.uuid4())
        cursor.execute(
            "INSERT INTO PERSON (ID, NAME, CPF, EMAIL, BIRTHDAY, PHONE_NUMBER, PASSWORD) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (id, account.name, account.cpf, account.email, account.birth,
             account.phone, account.password)
        )
        mysql_connection.commit()

        # Realizar consulta para obter os dados inseridos

        cursor.execute(get_person_id_query, (account.email,))
        person = cursor.fetchone()
        # Fechar o cursor e retornar o ID do produto
        token = generate_jwt_token({'user_id': person["id"]})
        return {"access_token": token,
                "person": person}

    except Exception as e:
        # Em caso de erro, cancelar a transação e retornar uma resposta de erro
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()


@router.post("/principal-ship", tags=['User'])
async def get_data_user(principal_ship: id_ship, current_user: int = Depends(token.get_current_user)):
    try:
        cursor = mysql_connection.cursor(dictionary=True)
        cursor.execute(
            'UPDATE person SET principal_ship_id = %s WHERE id = %s', (principal_ship.id, current_user))
        mysql_connection.commit()
        return True
    except Exception as e:
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
