-- creating new database
# syntax create database dbname;

create database StudentsDB;
-- delete database
drop database studentsdb;
-- view all db
show databases;
-- select db using query or double click the table from schemas
use studentsdb;

-- create table
# syntax create table tablename (columnname datatype);
create table StudentDetails(id integer,name varchar(20),age integer,place varchar(25)); 

-- drop table
drop table studentdetails;

-- insert
# syntax insert into tablename values(corressponding values)
insert into studentdetails values(1,'Abcd',10,'yyy');
insert into studentdetails values(2,'cd',10,'yy');
insert into studentdetails values(3,'bcd',10,'y'),(4,'d',10,'www');

-- display table
select * from studentdetails;

-- display particular query
select name,place from studentdetails;

-- update query
update studentdetails set name='gi' where id=1;

update studentdetails set place='YYY' where id =3;

-- display complete record of a person using their place
select place='yyy' from studentdetails;
