use sillicon_store;

create table product (
	id varchar(255) not null,
    owner bigint not null,
    name varchar(100) not null,
    description text not null,
    brand varchar(50) not null,
    color varchar(50),
    price double not null,
    stock int not null,
    active boolean not null,
    created_at date not null,
    updated_at date not null,
    rating double not null,
    category varchar(50) not null,
    featured boolean not null,
    primary key(id),
    foreign key (owner) references person(id)
);



drop table product;

CREATE TABLE person (
id INT NOT NULL,
name VARCHAR(100) NOT NULL,
cpf VARCHAR(14) UNIQUE NOT NULL,
email VARCHAR(70) UNIQUE NOT NULL,
nascimento DATE NOT NULL,
telefone VARCHAR(15),
senha VARCHAR(255) NOT NULL,
PRIMARY KEY(ID)
);

INSERT INTO person (id, name, cpf, email, nascimento, telefone, senha) VALUES (0, 'Lucas Ferreira Silva', '520.945.658-74', 'lucas.lfs2004@gmail.com', '2004-06-19', '(11) 97968-4799', 'GallardoLP-570');

create table image (
	id varchar(255) not null,
    path varchar(255) not null,
    foreign key (id) references product(id)
);
