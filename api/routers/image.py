from fastapi import APIRouter, FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles


router = APIRouter()
app = FastAPI()

# Configuração para servir arquivos estáticos (imagens) da pasta "public"
# app.mount("/public", StaticFiles(directory="public"), name="public")

# Rota para servir imagens estáticas


@router.get("/image/{image_path}", tags=["Imagens"])
def get_image(image_path: str):
    return image_path
