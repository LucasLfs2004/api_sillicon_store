import uuid
import mysql.connector

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
class NewAccount(BaseModel):
    nome: str
    uuid: int
    cpf: str
    email: str
    nascimento: date
    telefone: str
    senha: str

# Rota para adicionar um novo usuário
@app.post("/api/create-account")
def create_account(account: NewAccount):
    try:
        # Conectar ao banco de dados
        cursor = mysql_connection.cursor(dictionary=True)

        uuid_int = int.from_bytes(uuid.uuid4().bytes[:4], byteorder="big") % (2 ** 32)
        account.uuid = int(uuid_int)

        # Executar a inserção na tabela produtos

        cursor.execute(
            "INSERT INTO PERSON (ID, NAME, CPF, EMAIL, NASCIMENTO, TELEFONE, SENHA) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (account.uuid, account.nome, account.cpf, account.email, account.nascimento, account.telefone, account.senha)
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



