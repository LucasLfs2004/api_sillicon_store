# Tabelas do banco de dados
## category
uuid
nome_categoria

## product
uuid int not null
nome string
imagens
marca
descricao
fabricante
preco
juros

## person
uuid
nome
cpf
rg
email

## vendedor


## MySQL

CREATE TABLE PERSON (
ID INT NOT NULL,
NAME VARCHAR(100) NOT NULL,
CPF VARCHAR(14) UNIQUE NOT NULL,
EMAIL VARCHAR(70) UNIQUE NOT NULL,
NASCIMENTO DATE NOT NULL,
TELEFONE VARCHAR(15),
SENHA VARCHAR(255) NOT NULL,
PRIMARY KEY(ID)
);

INSERT INTO PERSON (ID, NAME, CPF, EMAIL, NASCIMENTO, TELEFONE, SENHA) VALUES (0, 'Lucas Ferreira Silva', '520.945.658-74', 'lucas.lfs2004@gmail.com', '2004-06-19', '(11) 97968-4799', 'GallardoLP-570');

SELECT * FROM PERSON