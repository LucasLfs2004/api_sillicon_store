use sillicon_store;

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

create table product (
	id varchar(255) not null,
    name varchar(100) not null,
    description text not null,
    brand varchar(50) not null,
    color varchar(50) not null,
    price double not null,
    stock int not null,
    active boolean not null,
    created_at date not null,
    updated_at date not null,
    rating double not null,
    category varchar(50) not null,
    featured boolean not null,
	owner int not null,
    primary key (id),
);


create table image (
	id varchar(255) not null,
    path varchar(255) not null,
    foreign key (id) references product(id)
);
