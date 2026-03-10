create database registration;
use registration;
create table register(id int auto_increment primary key,name varchar(100),
fathername varchar(100),village varchar(100),amount int);
select *from register;
delete from register where id=1;