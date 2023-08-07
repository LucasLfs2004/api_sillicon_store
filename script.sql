use sillicon_store;

create table product (
	uuid varchar(255) not null,
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
    
);