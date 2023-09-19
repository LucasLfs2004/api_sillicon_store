from fastapi import APIRouter, Depends
from database.connection import mysql_connection
from fastapi import HTTPException
# from models.models import Person, effect_login
from dependencies.token import generate_jwt_token
# import bcrypt
# import uuid
# import calendar
# from dependencies.const import current_GMT
from sqlalchemy.orm import Session
from sql_app.database import SessionLocal
from sql_app.models import Person
from sql_app.schemas import PersonBase, PersonLogin, PersonDelete
from sql_app.crud_person import get_people, create_person, login_person, delete_person

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/person", tags=['person'])
def get_persons(db: Session = Depends(get_db)):
    people = get_people(db)
    return {'people': people}


@router.post("/login", tags=['person'])
def login(user: PersonLogin, db: Session = Depends(get_db)):
    login = login_person(db, user)
    return login


@router.post("/person", tags=['person'])
def post_person(user: PersonBase, db: Session = Depends(get_db)):
    validation = create_person(db, user)
    return validation


@router.delete("/person", tags=['person'])
def person_delete(param: PersonDelete, db: Session = Depends(get_db)):
    delete = delete_person(db, param)
    return delete
