from api.database.connection import mysql_connection
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException as StarletteHTTPException
import time
import uvicorn
import signal
from api.routers import person, product, category, comment, brand, image, cart, seller, ship, banner, voucher

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
app.include_router(comment.router)
app.include_router(brand.router)
app.include_router(image.router)
app.include_router(cart.router)
app.include_router(seller.router)
app.include_router(ship.router)
app.include_router(banner.router)
app.include_router(voucher.router)

# @app.exception_handler(StarletteHTTPException)
# async def http_exception_handler(request, exc):
#     return PlainTextResponse(str(exc.detail), status_code=exc.status_code)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=400)

@app.get("/")
def read_root():
    return {"Hello": "World"}

def shutdown():
    # Realize qualquer limpeza necessária antes de encerrar
    print("Encerrando a aplicação...")

def main():
    signal.signal(signal.SIGINT, lambda s, f: shutdown())
    uvicorn.run(app, host="0.0.0.0", port=8080)


if __name__ == '__main__':
    main()
    