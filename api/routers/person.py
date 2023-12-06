from fastapi import APIRouter
from database.connection import mysql_connection
from fastapi import HTTPException
from models.models import new_account, effect_login
from dependencies.token import generate_jwt_token
import bcrypt
import uuid
import calendar
from dependencies.const import current_GMT

router = APIRouter()


@router.get("/person", tags=['person'])
def get_persons():
    cursor = mysql_connection.cursor(dictionary=True)
    cursor.execute("""
                   SELECT
                        person.id,
                        person.name,
                        person.cpf,
                        person.email,
                        person.birthday,
                        person.phone_number,
                        seller.admin as isAdmin,
                        seller.seller as isSeller,
                        seller.id as idSeller
                    FROM
                        person
                    LEFT JOIN
                        seller ON person.id = seller.id_person;
                   """)
    # cursor.execute("select * from person")
    person = cursor.fetchall()
    cursor.close()
    return person


@router.post("/login", tags=['person'])
def effect_login(login: effect_login):
    try:
        cursor = mysql_connection.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM PERSON WHERE EMAIL LIKE %s", (login.email,))
        person = cursor.fetchone()
        cursor.close

        if person is None:
            raise HTTPException(
                status_code=401, detail="Usuário não encontrado")

        if bcrypt.checkpw(login.senha.encode("utf-8"), person["password"].encode("utf-8")):
            person.pop("password", None)
            token = generate_jwt_token({'user_id': person["id"]})
            return {"message": "Login efetuado com sucesso", "user_data": person, "user_token": token}
        else:
            raise HTTPException(status_code=401, detail="Senha incorreta")
    except Exception as e:
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/create-account", tags=['person'])
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

        # uuid int
        # uuid_int = int.from_bytes(
        #     uuid.uuid4().bytes[:4], byteorder="big") % (2 ** 32)

        #uuid 
        account.uuid = str(uuid.uuid4())
        print(account.uuid)

        # timestamp
        time_stamp = calendar.timegm(current_GMT)
        account.created_at = int(time_stamp)
        account.updated_at = int(time_stamp)
        # Executar a inserção na tabela produtos
        cursor.execute(
            "INSERT INTO PERSON (ID, NAME, CPF, EMAIL, BIRTHDAY, PHONE_NUMBER, PASSWORD, CREATED_AT, UPDATED_AT) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (account.uuid, account.name, account.cpf, account.email, account.birth,
             account.phone, account.password, account.created_at, account.updated_at)
        )
        mysql_connection.commit()

        # Realizar consulta para obter os dados inseridos
        cursor.execute("SELECT * FROM PERSON WHERE ID = %s", (account.uuid,))
        inserted_data = cursor.fetchone()

        # Fechar o cursor e retornar o ID do produto
        cursor.close()
        return {"new_user:": inserted_data}
    except Exception as e:
        # Em caso de erro, cancelar a transação e retornar uma resposta de erro
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))
