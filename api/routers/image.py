from fastapi import APIRouter, FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os


router = APIRouter()


@router.get("/image/product/{image_path}", tags=["Imagens"])
def get_image(image_path: str):
    print(image_path)
    file_path = str("public/product/" + image_path)
    if os.path.exists(file_path):
        return FileResponse(file_path)
    return {"error": "File not found"}
    # return image_path


@router.get("/image/brand/{image_path}", tags=["Imagens"])
def get_image(image_path: str):
    print(image_path)
    file_path = str("public/brand/" + image_path)
    if os.path.exists(file_path):
        return FileResponse(file_path)
    return {"error": "File not found"}
    # return image_path
