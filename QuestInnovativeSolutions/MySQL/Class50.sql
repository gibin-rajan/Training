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
select * from studentdetails where place='www';

-- display records of a person whose age is greater than 25
select * from studentdetails where age>=25;

-- distinct-- used to display duplicate data of given column
select distinct name from studentdetails;
select distinct * from studentdetails;
select distinct name,place  from studentdetails;

-- orderby

select age from studentdetails order by age;#by default this will be in ascending order
select age from studentdetails order by age desc; # for decending order
select age from studentdetails order by age asc; # for manual ascending order
select * from studentdetails order by age desc,name asc;

-- add new column to a existing table
alter table studentdetails add email varchar(20);

alter table studentdetails add email varchar(20),add lang varchar(20);
-- modify column datatype
alter table studentdetails modify email int;

-- rename a column name
alter table studentdetails change column email EmailId int;

-- drop column
alter table studentdetails drop column EmailId;

-- truncate--- remove all contents or values of the table but not delete the table
-- it will remove the values inside the table
truncate table studentdetails;

-- diplay first row of the table 
select * from studentdetails limit 1;

-- to display last row of the table
select * from studentdetails order by id desc limit 1;

-- as --used to create a temporary table name 
select age as Studentage, name as studentName from studentdetails;

-- arithmatic operators(+,-,*,/,%)
select 20+30 as sum;

select id+age as result from studentdetails;

select age+5 as result from studentdetails;

-- comparison operator (<,>,<=,>=,=,!=)
select 10>5 as result;
select 10!=5 as result;

-- logical operator
select * from studentdetails where age=10 and place='tvm';

select * from studentdetails where age=10 or place='tvm';

-- between

select * from studentdetails where age between 10 and 23;

-- exists
-- the main query if the sub query is true(sub query means the query inside exists)

select * from studentdetails where exists(select* from studentdetails where age=20 or name='gi');

# in

select * from studenetdetails where name in ("gi",'abc');

# like 

select * from studentdetails where name like 'abc';
select * from studentdetails where name like 'a%';-- starts with letter a
select * from studentdetails where name like '%a';-- ends with letter a
select * from studentdetails where name like '%b%';-- if the letter present in the letter in anywhere

# not like

select * from studentdetails where name not like 'abc';

# string functions()
# length()

select name,length(name) as count from studentdetails;

# concat()

select concat(name,' ',place) as data from studentdetails;

# upper() , lower()

select upper(name) from studentdetails;

# reverse()

select reverse(place) from studentdetails;

# repeat()

select repeat('hello',3) as new;

select repeat(place,2) from studentdetails;

select left('Hello',2) as neww;

select right('Hello',2) as data;

# math functions()
# abs()-- absolute
select abs(-15) as rslt;

# avg()
select avg(age) from studentdetails;

# round()
select round(5.9999);

# count()
select count(age) from studentdetails;

# max()
select name,max(age) from studentdetails;
select name,age from studentdetails where age=(select max(age) from studentdetails);

# min()
select min(age) from studentdetails;

# sum()
select sum(age) from studentdetails;

#sqrt()
select sqrt(9);

-- date functions()
# current_timstamp() --- get current date and time
select current_timestamp() as time;

select day('2022/03/28');

select month('2022/03/28');

select year('2022/03/28');

select dayname('2022/03/28');

select sysdate();

select curtime();

select now();

select date_format('2022/03/29','%d');-- 29
select date_format('2022/03/29','%D');-- 29th
select date_format('2022/03/29','%m');-- 03
select date_format('2022/03/29','%M');-- March
select date_format('2022/03/29','%y');-- 22
select date_format('2022/03/29','%Y');-- 2022

select date('2022/03/29'); -- print date in correct format

select datediff('2022/03/29','2022/02/28');-- difference between two dates

select * from studentdetails;
insert into studentdetails values (5,'Joe',20,'tvm'),(6,'Jimmy',21,'Kochi');

-- group by- decending order(rslt)
select count(age) as rslt,age from studentdetails group by age order by rslt desc;

-- having -- instead of using 'where' we can use 'having'. In beloow case
-- because of count we cant use 'where' tag so in those times we use 'having'

select count(age) as rslt,age from studentdetails group by age having count(age)>2;
