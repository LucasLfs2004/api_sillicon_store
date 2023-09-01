# Bibliotecas instaladas para o funcionamento da API

### fastapi

### bcrypt

### flask

### flask-mysql

### mysql-connector-python

### pyjwt

### python-multipart

### sqlalchemy

###

# Tabelas do Banco de dados mySql

### Person

UUID int not null
name varchar
cpf varchar unique
email varchar unique
birth date
created_at int(timestamp)
updated_at int(timestamp)
password varchar

# product

uuid int not null
name varchar
description varchar
brand varchar
color varchar
price double
stock int
active boolean
created_at
updated_at
rating
category
featured

# carrinho

uuid_person int not null
uuid_product int not null
quantidade int not null

# Images

uuid_product
path varchar
