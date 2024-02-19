create table personcourse(courseid int primary key auto_increment, coursename varchar(20),person_id int,foreign key(person_id) references person(personid));

-- inner join
select person.personname,personcourse.coursename,person.personid from person inner join personcourse on person.personid=personcourse.person_id=personcourse.person_id;
-- left join

select * from person left join personcourse on person.personid=personcourse.person_id;

-- right join

select * from person right join personcourse on person.personid=personcourse.person_id;

-- stored procedures

DELIMITER &&
create procedure personprocedure()
begin
select person.personid as personid, personcourse.coursename as coursename, person.personname as Name from person inner join personcourse on person.personid=personcourse.person_id;
end &&

drop procedure personprocedure;

-- view - virtual table 
create view personview as select personname,personid from person;

-- display table using viewname
select * from personview;

-- update view
alter view personview as select personid,personname from person;

-- drop 
drop view personview




