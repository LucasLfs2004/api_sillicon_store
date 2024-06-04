from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
import os

router = APIRouter()


@router.get("/image/product/{image_path}", tags=["Imagens"])
async def get_image(image_path: str):
    file_path = str("public/product/" + image_path)
    if os.path.exists(file_path):
        return FileResponse(file_path)
    raise HTTPException(status_code=404, detail=str('File not found'))


@router.get("/image/brand/{image_path}", tags=["Imagens"])
async def get_image(image_path: str):
    file_path = str("public/brand/" + image_path)
    if os.path.exists(file_path):
        return FileResponse(file_path)
    raise HTTPException(status_code=404, detail=str('File not found'))


@router.get("/image/banner/{image_path}", tags=["Imagens"])
async def get_image(image_path: str):
    file_path = str("public/banner/" + image_path)
    if os.path.exists(file_path):
        return FileResponse(file_path)
    raise HTTPException(status_code=404, detail=str('File not found'))
