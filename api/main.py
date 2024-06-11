from routers import person, product, category, brand, comment, image, cart, seller, ship, banner, voucher, order
from fastapi import HTTPException, Depends, FastAPI
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from database.connection import mysql_connection
from dependencies.token import generate_jwt_token
from requests.person import get_person_id_query
from typing import Annotated
import uvicorn
import time
import bcrypt
import signal

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

current_GMT = time.gmtime()


app.include_router(person.router)
app.include_router(product.router)
app.include_router(category.router)
app.include_router(brand.router)
app.include_router(comment.router)
app.include_router(image.router)
app.include_router(cart.router)
app.include_router(seller.router)
app.include_router(ship.router)
app.include_router(banner.router)
app.include_router(voucher.router)
app.include_router(order.router)


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=400)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    try:
        cursor = mysql_connection.cursor(dictionary=True)
        cursor.execute(get_person_id_query,
                       (form_data.username.strip().lower(),))
        person = cursor.fetchone()

        if person is None:
            raise HTTPException(
                status_code=401, detail="Usuário não encontrado")

        if bcrypt.checkpw(form_data.password.encode("utf-8"), person["password"].encode("utf-8")):
            person.pop("password", None)
            token = generate_jwt_token(
                {'user_id': person["id"], 'seller_id': person['id_seller']})
            return {"access_token": token,
                    "token_type": "bearer",
                    "person": person}
        else:
            raise HTTPException(status_code=401, detail="Senha incorreta")
    except Exception as e:
        mysql_connection.rollback()
        raise HTTPException(status_code=500, detail=str(e))


def shutdown():
    print("Encerrando a aplicação...")


if __name__ == "__main__":
    signal.signal(signal.SIGINT, lambda s, f: shutdown())
    uvicorn.run(app, host="0.0.0.0", port=8080)
