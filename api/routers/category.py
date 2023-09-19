from fastapi import APIRouter, HTTPException
from models.models import new_category
from database.connection import mysql_connection
import uuid

router = APIRouter()


@router.get("/category", tags=["Categoria"])
def get_categorys():
    try:
        cursor = mysql_connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM category")
        categorys = cursor.fetchall()

        cursor.close()
        return {"categorys:": categorys}
    except Exception as e:
        cursor.close()
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/category", tags=['Categoria'])
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
