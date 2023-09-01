from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Date, Text, Double, Boolean


SQLALCHEMY_DATABASE_URL = "mysql://admin:admin@127.0.0.1:3306/SILLICON_STORE"

# SQLALCHEMY_DATABASE_URL = "127.0.0.1://3306/sillicon_store"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()

class Person(Base):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    email = Column(String(150), nullable=False)
    cpf = Column(String(14), nullable=False)
    phone = Column(String(15), nullable=False)
    password = Column(String(255), nullable=False)
    birth = Column(Date, nullable=False)
    created_at = Column(Integer, nullable=False)
    updated_at = Column(Integer, nullable=False)

class Brand(Base):
    __tablename__ = "brand"

    name = Column(String(50), primary_key=True)
    brand_logo = Column(String(255))


class category(Base):
    __tablename__ = "category"

    name = Column(String(50), primary_key=True)
    poster_path = Column(String(255), nullable=False)

class product(Base):
    __tablename__ = "product"

    id = Column(String(255), primary_key=True)
    owner = Column(Integer, nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    brand = Column(String(50), nullable=False)
    color = Column(String(50))
    price = Column(Double, nullable=False)
    stock = Column(Integer, nullable=False)
    active = Column(Boolean, nullable=False)
    created_at = Column(Integer, nullable=False)
    updated_at = Column(Integer, nullable=False)
    category = Column(String(50), nullable=False)
    featured = Column(Boolean, nullable=False)
    