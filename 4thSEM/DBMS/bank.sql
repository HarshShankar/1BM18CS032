show databases;
create database bank;
show databases;
use bank;
create table branch(branch_name varchar(40) not null unique ,branch_city varchar(50),assests float , primary key(branch_name));
create table bankaccount(accno int not null unique,branch_name varchar(40),balance float,primary key(accno),foreign key(branch_name) references branch(branch_name));
create table bankcustomer(customer_name varchar(40) not null unique,customer_street varchar(50),customer_city varchar(50),primary key(customer_name));
create table depositer(customer_name varchar(40) not null unique,accno int not null unique,primary key(customer_name),foreign key(customer_name) references bankcustomer(customer_name),foreign key(accno) references bankaccount(accno));   
create table loan(loan_number int not null unique,branch_name varchar(40),amount float,primary key(loan_number),foreign key(branch_name) references branch(branch_name));
insert into branch
	values("SBI_Chamrajpet","Bangalore",50000),("SBI_ResidencyRoad","Bangalore",10000),("SBI_ShivajiRoad","Bombay",20000),("SBI_ParlimentRoad","Delhi",10000),("SBI_Jantarmantar","Delhi",20000);
insert into bankaccount
	values(1,"SBI_Chamrajpet",2000),(2,"SBI_ResidencyRoad",5000),(3,"SBI_ShivajiRoad",6000),(4,"SBI_ParlimentRoad",9000),(5,"SBI_Jantarmantar",8000),(6,"SBI_ShivajiRoad",4000),(8,"SBI_ResidencyRoad",4000),(9,"SBI_ParlimentRoad",3000),(10,"SBI_ResidencyRoad",5000),(11,"SBI_Jantarmantar",2000);
insert into bankcustomer
	values("Avinash","Bull_Temple_Road","Bangalore"),("Dinesh","Bannergatta","Bangalore"),("Mohan","NationalCollege_Road","Bangalore"),("Nikhil","Akbar_Road","Delhi"),("Ravi","Prithviraj_Road","Delhi");
insert into depositer
		values("Avinash",1),("Dinesh",2),("Nikhil",4),("Ravi",5);
insert into loan
	values(1,"SBI_Chamrajpet",1000),(2,"SBI_ResidencyRoad",2000),(3,"SBI_ShivajiRoad",3000),(4,"SBI_ParlimentRoad",4000),(5,"SBI_Jantarmantar",5000);
    
