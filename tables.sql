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
    created_at int not null,
    updated_at int not null,
    category varchar(50) not null,
    featured boolean not null,
    primary key(id),
    foreign key (owner) references person(id),
    foreign key (category) references category(name)
);

create table rating (
	id varchar(255) not null,
    amount int not null,
    rating double not null,
    foreign key (id) references product(id)
);

create table image (
	id varchar(255) not null,
    path varchar(255) not null,
    foreign key (id) references product(id)
);

create table category (
	id varchar(255) not null,
    name varchar(50) unique not null,
	primary key(id)
);
