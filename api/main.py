import uuid
import mysql.connector
import bcrypt
import jwt
import secrets
import datetime
from typing import Optional
from datetime import date
from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


mysql_host = "127.0.0.1://3306/sillicon_store"
mysql_user = "admin"
mysql_password = "admin"
mysql_db = "SILLICON_STORE"

mysql_connection = mysql.connector.connect(
    user=mysql_user,
    password=mysql_password,
    database=mysql_db
)

origins = [
    "http://localhost:3000",  # Adicione a URL do seu aplicativo ReactJS aqui
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SECRET_KEY = secrets.token_hex(32)

def generate_jwt_token(payload):
    # Defina o tempo de expiração do token, por exemplo, 1 hora a partir do momento atual.
    expiration = datetime.datetime.utcnow() + datetime.timedelta(hours=240)
    
    # Crie o payload do token com os dados do usuário
    token_payload = {
        'exp': expiration,
        **payload  # Aqui você pode adicionar outras informações sobre o usuário, como ID, nome, etc.
    }
    
    # Gere o token utilizando a função jwt.encode()
    token = jwt.encode(token_payload, SECRET_KEY, algorithm='HS256')
    
    return token


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "Nome": "Lucas Ferreira Silva"}

@app.get("/person")
def get_persons():
    cursor = mysql_connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM PERSON")
    person = cursor.fetchall()
    cursor.close()
    return person


class effectLogin(BaseModel):
    email: str
    senha: str

@app.post("/login")
def effect_login(login: effectLogin):
    try:
        cursor = mysql_connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM PERSON WHERE EMAIL LIKE %s", (login.email,))
        person = cursor.fetchone()
        cursor.close

        if person is None:
            raise HTTPException(status_code=401, detail="Usuário não encontrado")

        if bcrypt.checkpw(login.senha.encode("utf-8"), person["SENHA"].encode("utf-8")):
            print("Eu entro aqui!")
            token = generate_jwt_token({'user_id': person["ID"]})
            return {"message": "Login efetuado com sucesso", "user_data": person, "user_token": token}
        else: 
            raise HTTPException(status_code=401, detail="Senha incorreta")
    except Exception as e:
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))

class NewAccount(BaseModel):
    name: str
    uuid: Optional[int] = None
    cpf: str
    email: str
    birth: date
    phone: str
    password: str


# Rota para adicionar um novo usuário
@app.post("/create-account")
def create_account(account: NewAccount):
    try:
        # Conectar ao banco de dados
        cursor = mysql_connection.cursor(dictionary=True)
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(account.password.encode("utf-8"), salt)
        account.password = hashed_password
        uuid_int = int.from_bytes(uuid.uuid4().bytes[:4], byteorder="big") % (2 ** 32)
        account.uuid = uuid_int
        print(account.uuid)

        # Executar a inserção na tabela produtos

        print("tentando...")
        cursor.execute(
            "INSERT INTO PERSON (ID, NAME, CPF, EMAIL, NASCIMENTO, TELEFONE, SENHA) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (account.uuid, account.name, account.cpf, account.email, account.birth, account.phone, account.password)
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


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)



