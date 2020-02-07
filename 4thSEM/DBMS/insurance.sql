show tables;
show databases;
create database college;
use college;
show databases;
create database prob_insurance;
show tables;
use prob_insurance;
create table person(driver_id char(10) ,
	name char(30),
	address char(100),
	primary key(driver_id));
drop table person;
create table person(driver_id char(10) ,
	name char(30),
	address char(100),
	primary key(driver_id));
create table car(reg_num varchar(10),
	model varchar(100),
    year int);
alter table car
add primary key(reg_num);
create table accident(report_num int,
	accident_date date,
    location varchar(100));
select * from car;
create table owns(driver_id char(10),
	reg_num varchar(10),
    primary key(driver_id),
    foreign key(driver_id) references person(driver_id),
    foreign key(reg_num) references car(reg_num));
alter table owns
 drop primary key;
desc owns;
drop table owns;
create table owns(driver_id char(10),
	reg_num varchar(10),
    primary key(driver_id,reg_num),
    foreign key(driver_id) references person(driver_id),
    foreign key(reg_num) references car(reg_num));
alter table accident
add primary key(report_num);
create table participated(driver_id char(10),
	reg_num varchar(10),
	report_num int,
    damage_amount varchar(10),
    primary key(driver_id,reg_num,report_num),
    foreign key(driver_id) references person(driver_id),
    foreign key(reg_num)  references car(reg_num),
    foreign key(report_num) references accident(report_num));
show tables;
insert into person
	values('A01','Richard','Srinivas Nagar'),('A02','Pradeep','Rajaji nagar'),('A03','Smith','Ashok Nagar'),('A04','Venu','N R Colony'),('A05','John','Hanumanth Nagar');
insert into car
		values('KA052250','Indica',1990),('KA031181','Lancer',1957),('KA095477','Toyota',1998),('KA053408','Honda',2008),('KA0451702','Audi',2005);
insert into owns(driver_id,reg_num)
	values ('A01',"KA052250"),('A02',"KA053408"),('A03',"KA031181"),('A04',"KA095477"),('A05',"KA041702");
insert into accident
	values (11,20030101,'Mysore Road'),(12,20040202,'South End Circle'),(13,20030121,'Bull Temple Road'),(14,20080217,'Mysore Road'),(15,20050403,'Kannakpura Road');
