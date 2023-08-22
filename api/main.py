import calendar
import time
import os
import uuid
import mysql.connector
import bcrypt
import jwt
import secrets
import datetime
from typing import Optional
from typing import List
from typing import Union
from datetime import date
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, Request, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
import shutil
from fastapi.responses import JSONResponse


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
    "*" # Adicione a URL do seu aplicativo ReactJS aqui
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


current_GMT = time.gmtime()
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

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=400)


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

        if bcrypt.checkpw(login.senha.encode("utf-8"), person["senha"].encode("utf-8")):
            person.pop("senha", None)
            token = generate_jwt_token({'user_id': person["id"]})
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
    created_at: Optional[int] = None
    updated_at: Optional[int] = None

# Rota para adicionar um novo usuário
@app.post("/create-account")
def create_account(account: NewAccount):
    try:
        cursor = mysql_connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM PERSON WHERE CPF LIKE %s OR EMAIL LIKE %s", (account.cpf, account.email))
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
        raise HTTPException(status_code=409 ,detail="O CPF e email inseridos já possuem cadastro")
    elif not cpfValid and emailValid:
        cursor.close()
        raise HTTPException(status_code=409, detail="O CPF inserido já está cadastrado")
    elif cpfValid and not emailValid:
        cursor.close()
        raise HTTPException(status_code=409, detail="O email inserido já está cadastrado")
    
    try:
        # Conectar ao banco de dados
        cursor = mysql_connection.cursor(dictionary=True)
        
        #Codificação de senha
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(account.password.encode("utf-8"), salt)
        account.password = hashed_password

        #uuid
        uuid_int = int.from_bytes(uuid.uuid4().bytes[:4], byteorder="big") % (2 ** 32)
        account.uuid = uuid_int

        #timestamp
        time_stamp = calendar.timegm(current_GMT)
        account.created_at = int(time_stamp)
        account.updated_at = int(time_stamp)
        # Executar a inserção na tabela produtos
        cursor.execute(
            "INSERT INTO PERSON (ID, NAME, CPF, EMAIL, NASCIMENTO, TELEFONE, SENHA, CREATED_AT, UPDATED_AT) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (account.uuid, account.name, account.cpf, account.email, account.birth, account.phone, account.password, account.created_at, account.updated_at)
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

upload_folder = "public"
os.makedirs(upload_folder, exist_ok=True)

# class ImgUpload(BaseModel):
#     path: List[UploadFile]


class new_product(BaseModel):
    owner: int
    name: str
    description: str
    brand: str
    price: float
    stock: int
    featured: Optional[bool] = True
    category: str
    active: Optional[bool] = True
    color: Optional[str] = "null"
    created_at: Optional[int] = 0
    updated_at: Optional[int] = 0
    rating: Optional[int] = 0
    id: Optional[str] = None

@app.post("/create-product")
async def create_product(owner: str = Form(), name: str = Form(), description: str = Form(), brand: str = Form(), category: str = Form(), 
                   price: str = Form(), stock: str = Form(), featured: str = Form(), files: List[UploadFile] = File(...)):
    filenames = []
    time_stamp = calendar.timegm(current_GMT)
    product = {
                'id': str(uuid.uuid4()),
                'owner': owner,
                'active': bool(featured),
                'featured': True,
                'name': name,
                'description': description,
                'brand': brand,
                'category': category,
                'price': float(price),
                'stock': int(stock),
                'color': str('null'),
                'created_at': int(time_stamp),
                'updated_at': int(time_stamp),
             }
    try:
        # Conectar ao banco de dados
        cursor = mysql_connection.cursor(dictionary=True)
        
        # Executar a inserção na tabela produtos
        cursor.execute(
            "INSERT INTO PRODUCT (id, owner, name, description, brand, price, stock, active, created_at, updated_at, category, featured) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (product['id'], product['owner'], product['name'], product['description'], product['brand'], product['price'], product['stock'], 
             product['active'], product['created_at'], product['updated_at'], product['category'], product['featured'])
        )
        # Fechar o cursor e retornar o ID do produto
        for file in files:
            filename = str(time.time()) + file.filename.replace(' ', '_')
            filenames.append(filename)
            file_path = os.path.join(upload_folder, filename)
            with open(file_path, "wb") as f:
                f.write(file.file.read())
            cursor.execute(
                    "INSERT INTO image (id, path) VALUES (%s, %s)",
                    (product['id'], str("public/" + filename))
                )
        print(filenames)

        cursor.execute(
            "INSERT INTO rating (id, amount, rating) VALUES (%s, %s, %s)",
        (product['id'], int(0), int(0))
        )
        mysql_connection.commit()


        # Realizar consulta para obter os dados inseridos
        cursor.execute("""
                    SELECT
                        product.id AS id,
                        product.name AS product_name,
                        product.description AS product_description,
                        product.brand AS product_brand,
                        product.price AS product_price,
                        product.stock AS product_stock,
                        product.category AS product_category,
                        JSON_ARRAYAGG(
                            JSON_OBJECT(
                                'img_path', image.path
                            )
                        ) AS images,
                        JSON_ARRAYAGG(
                            JSON_OBJECT(
                                'amount', rating.amount,
                                'rating', rating.rating
                            )
                       ) AS rating
                    FROM
                        product
                    LEFT JOIN
                        image ON product.id = image.id
                    LEFT JOIN
                        rating ON product.id = rating.id
                    WHERE
                        product.id = %s
                    GROUP BY
                        product.id;
                       """, (product['id'],)
                       )
        product_data = cursor.fetchone()
        cursor.close()
        return {"new_product:": product_data}
    except Exception as e:
        # Em caso de erro, cancelar a transação e retornar uma resposta de erro
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally: 
        cursor.close()


@app.post("/product")
async def create_product(
                            name: str = Form(),
                            description: str = Form(),
                            brand: str = Form(),
                            category: str = Form(),
                            price: str = Form(),
                            stock: str = Form(),
                            featured: str = Form(),
                            files: List[UploadFile] = File(...)
                         ):
    preco = float(price)
    print(preco)
    print({ 'name': name,
            'description': description,
            'brand': brand,
            'category': category,
            'price': float(price),
            'stock': int(stock),
            'featured': bool(featured),
            'files': files})
    return { 'name': name,
            'description': description,
            'brand': brand,
            'category': category,
            'price': price,
            'stock': stock,
            'featured': featured,
            'files': files}


@app.post("/upload")
def upload_image(files: List[UploadFile] = File(...)):
    filenames = []
    for file in files:
        filename = str(time.time()) + file.filename.replace(' ', '_')
        filenames.append(filename)
        file_path = os.path.join(upload_folder, filename)
        with open(file_path, "wb") as f:
            f.write(file.file.read())
    print(filenames)
    return {"filename": filenames}

class new_category(BaseModel):
    id: Optional[str] = None
    name: str 


@app.post("/add-category")
def create_category(category: new_category):
        try:
            cursor = mysql_connection.cursor(dictionary=True)
            category.id = str(uuid.uuid4())
            cursor.execute(
                "INSERT INTO CATEGORY (id, name) VALUES (%s, %s)",
                (category.id, category.name)
            )
            mysql_connection.commit()

            # Realizar consulta para obter os dados inseridos
            cursor.execute("SELECT * FROM category WHERE ID = %s", (category.id,))
            inserted_data = cursor.fetchone()

            # Fechar o cursor e retornar o ID do produto
            cursor.close()
            return {"new_category:": inserted_data}
        except Exception as e:
            # Em caso de erro, cancelar a transação e retornar uma resposta de erro
            mysql_connection.rollback()
            raise HTTPException(status_code=500, detail=str(e))



@app.get('/products')
def get_products():
    cursor = mysql_connection.cursor(dictionary=True)
    cursor.execute("""
                    SELECT
                        product.id AS id,
                        product.name AS product_name,
                        product.description AS product_description,
                        product.brand AS product_brand,
                        product.price AS product_price,
                        product.stock AS product_stock,
                        product.category AS product_category,
                        JSON_ARRAYAGG(
                            JSON_OBJECT(
                                'image_url', image.path
                            )
                        ) AS images
                    FROM
                        product
                    LEFT JOIN
                        image ON product.id = image.id
                    GROUP BY
                        product.id;
                    """)
    product = cursor.fetchall()
    cursor.close()
    return product




if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)

