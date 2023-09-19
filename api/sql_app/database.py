from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, Date, Text, Double, Boolean, ForeignKey
from . import schemas

SQLALCHEMY_DATABASE_URL = "mysql://admin:admin@127.0.0.1:3306/SILLICON_STORE"

# SQLALCHEMY_DATABASE_URL = "127.0.0.1://3306/sillicon_store"
engine = create_engine(SQLALCHEMY_DATABASE_URL)


Base = declarative_base()

Base.metadata.create_all(bind=engine)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
