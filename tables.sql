-- Active: 1693570597002@@127.0.0.1@3306@SILLICON_STORE

use sillicon_store;

create table
    person (
        id int not null,
        name varchar(50) not null,
        email varchar(150) not null,
        cpf varchar(14) not null,
        phone varchar(15) not null,
        password varchar(255) not null,
        birth date not null,
        created_at int not null,
        updated_at int not null,
        PRIMARY KEY(id),
    );

create table
    product (
        id varchar(255) not null,
        owner bigint not null,
        name varchar(255) not null,
        description text not null,
        brand varchar(50) not null,
        color varchar(50),
        price double not null,
        stock int not null,
        active boolean not null,
        created_at int not null,
        updated_at int not null,
        category varchar(50) not null,
        featured boolean not null,
        primary key(id),
        foreign key (owner) references person(id),
        foreign key (category) references category(name)
    );

create table
    rating (
        id varchar(255) not null,
        amount int not null,
        rating double not null,
        foreign key (id) references product(id)
    );

create table
    image (
        id varchar(255) not null,
        path varchar(255) not null,
        foreign key (id) references product(id)
    );

create table
    category (
        name varchar(50) unique not null,
        poster_path varchar(255) not null,
        primary key(name)
    );

create table
    brand (
        name varchar(50) unique not null,
        brand_logo varchar(255),
        primary key(id)
    );