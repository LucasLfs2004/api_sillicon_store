
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Date, Text, Double, Boolean, ForeignKey
from .database import Base


class Product(Base):
    __tablename__ = "product"

    id = Column(String(255), primary_key=True)
    # owner = Column(Integer, ForeignKey("person.id"), nullable=False)
    seller_id = Column(Integer, ForeignKey("person.id"), nullable=False)
    seller = relationship("Person", back_populates="products")
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    brand = Column(String(50), ForeignKey("brand.name"), nullable=False)
    color = Column(String(50))
    price = Column(Double, nullable=False)
    stock = Column(Integer, nullable=False)
    active = Column(Boolean, nullable=False)
    created_at = Column(Integer, nullable=False)
    updated_at = Column(Integer, nullable=False)
    category = Column(String(50), ForeignKey("category.name"), nullable=False)
    featured = Column(Boolean, nullable=False)
    rating = relationship('Rating', uselist=False,
                          back_populates='product', foreign_keys='Product.id', primaryjoin="and_(Product.id==Rating.id)")
    images = relationship('Image', back_populates='product',
                          )


class Person(Base):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    email = Column(String(150), nullable=False, unique=True)
    cpf = Column(String(14), nullable=False, unique=True)
    phone = Column(String(15), nullable=False)
    password = Column(String(255), nullable=False)
    birth = Column(Date, nullable=False)
    created_at = Column(Integer, nullable=False)
    updated_at = Column(Integer, nullable=False)
    is_admin = Column(Boolean, default=False)
    is_seller = Column(Boolean, default=False)
    products = relationship("Product",
                            back_populates="seller",
                            )


class Brand(Base):
    __tablename__ = "brand"

    name = Column(String(50), primary_key=True)
    brand_logo = Column(String(255))


class Category(Base):
    __tablename__ = "category"

    name = Column(String(50), primary_key=True)
    poster_path = Column(String(255), nullable=False)


class Image(Base):
    __tablename__ = "image"
    id = Column(String(255), primary_key=True)
    product_id = Column(String(255), ForeignKey("product.id"))
    path = Column(String(255))
    product = relationship('Product', back_populates='images')


class Rating(Base):
    __tablename__ = "rating"

    id = Column(String(255), ForeignKey("product.id"), primary_key=True)
    amount = Column(Integer, nullable=False)
    rating = Column(Double, nullable=False)
    product = relationship(
        'Product', back_populates='rating', uselist=False, foreign_keys="Rating.id",  primaryjoin="and_(Rating.id==Product.id)")
