create database project

create table if not exists fatal (
    id serial primary key not null,
    created_on timestamp not null,
    error_level varchar(10) not null,
    error_message text not null
);