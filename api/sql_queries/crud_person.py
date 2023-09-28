from sqlalchemy.orm import Session, aliased
from sqlalchemy.exc import IntegrityError
import bcrypt
import uuid
import calendar
import time
from fastapi import HTTPException
from sql_app.schemas import PersonBase, PersonLogin, PersonOffice
from sql_app.models import Person
from dependencies.token import generate_jwt_token
import re


class MyException(HTTPException):
    def __init__(self, detail: str, status_code: int = 400):
        super().__init__(status_code=status_code, detail=detail)


def login_person(db: Session, user: PersonLogin):
    try:
        account = db.query(Person).filter(
            Person.email == user.email).first()
        if account is None:
            raise MyException(
                detail="Usuário não encontrado", status_code=401)
        if bcrypt.checkpw(user.password.encode("utf-8"), account.password.encode("utf-8")):
            del account.password
            account.token = generate_jwt_token({'user_id': account.id})
            return {"message": "Login efetuado com sucesso", "user_data": account}
        else:
            raise MyException(status_code=401, detail="Senha incorreta")
    except MyException as e:
        return {'status_error: ': e.status_code,
                'description_error: ': e.detail}
    except Exception as e:
        raise MyException(status_code=500, detail=str(e))


def create_person(db: Session, user: PersonBase):
    try:
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(user.password.encode("utf-8"), salt)

        user.password = hashed_password

        # uuid
        uuid_int = int.from_bytes(
            uuid.uuid4().bytes[:4], byteorder="big") % (2 ** 30)

        # timestamp
        timestamp = int(time.time())
        print(timestamp)
        db_user = Person(id=uuid_int, name=user.name,
                         email=user.email, cpf=user.cpf, phone=user.phone, password=hashed_password, birth=user.birth, created_at=timestamp, updated_at=timestamp)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except IntegrityError as e:
        error_message = str(e)
        print(str(e))

        if 'Duplicate entry' in error_message and 'person.email' in error_message:
            return 'O email inserido já está cadastrado em nosso banco de dados'
        elif 'Duplicate entry' in error_message and 'person.cpf' in error_message:
            return 'O cpf inserido já está cadastrado em nosso banco de dados'
        else:
            return str(e)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def get_person(db: Session, param: str):
    try:
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(pattern, param):
            person = db.query(Person).filter(
                Person.email == param).first()
            if person:
                return {'user: ': person}
            else:
                return {'user: ': None}
        else:
            person = db.query(Person).filter(Person.cpf == param).first()
            if person:
                return {'user: ': person}
            else:
                return {'user: ': None}
    except Exception as e:
        raise MyException(status_code=500, detail=str(e))


def get_people(db: Session):
    peoples = db.query(Person).all()
    for i in range(len(peoples)):
        del peoples[i].password
    return peoples


def update_person(db: Session, person_id: int, updated_person: Person):
    person = db.query(Person).filter(Person.id == person_id).first()
    if person:
        for key, value in updated_person.dict().items():
            setattr(person, key, value)
        db.commit()
        db.refresh(person)
    return person


def update_person_seller_status(db: Session, office: PersonOffice):
    person = db.query(Person).filter(Person.email == office.email).first()
    if person:
        # Atualiza o atributo is_seller
        person.is_seller = office.is_active
        db.commit()  # Confirme a transação para persistir as alterações no banco de dados
        return True  # Retorna True para indicar que a atualização foi bem-sucedida
    else:
        return False  # Retorna False se o ID da pessoa não for encontrado


def update_person_admin_status(db: Session, office: PersonOffice):
    person = db.query(Person).filter(Person.email == office.email).first()
    if person:
        # Atualiza o atributo is_seller
        person.is_admin = office.is_active
        db.commit()  # Confirme a transação para persistir as alterações no banco de dados
        return True  # Retorna True para indicar que a atualização foi bem-sucedida
    else:
        return False  # Retorna False se o ID da pessoa não for encontrado


def delete_person(db: Session, param: str):
    try:
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(pattern, param):
            person = db.query(Person).filter(
                Person.email == param).first()
            if person:
                db.delete(person)
                db.commit()
        else:
            person = db.query(Person).filter(Person.cpf == param).first()
            if person:
                db.delete(person)
                db.commit()
    except Exception as e:
        raise MyException(status_code=500, detail=str(e))
