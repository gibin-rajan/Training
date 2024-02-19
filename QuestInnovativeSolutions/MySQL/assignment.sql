create database Employee;
use employee;
create table employeedetails(id integer,Empname varchar(20),place varchar(25),salary integer);
insert into employeedetails values(1,'A','Bangalore',10000),(2,'B','Kerala',11000),(3,'C','TN',12000),(4,'D','Kerala',11000);
select * from employeedetails;