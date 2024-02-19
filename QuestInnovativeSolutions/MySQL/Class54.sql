create table empdetails(emp_id int primary key not null auto_increment, first_name varchar(20) not null,age int check (age>=18), place varchar(20));
drop table empdetails;
insert into empdetails (first_name,age,place) values('Joe',20,'Kochi'),('James',19,'Tvm');
insert into empdetails (first_name,age,place) values('Alice',18,'Tvm');
alter table empdetails auto_increment=100;
select * from empdetails;

create table empsalary(empslry int primary key not null, salary int,empid int, foreign key(empid) references empdetails(empid));
insert into empsalary values(2,10000,2),(3,12000,2);
drop table empsalary;
select * from empsalary;