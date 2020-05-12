CREATE DATABASE BooksDB;
use BooksDB;
CREATE TABLE Publisher(
  pname VARCHAR(15),
  phone INT(10),
  address VARCHAR(30),
  PRIMARY KEY(pname));

CREATE TABLE Book(
  book_id INT,
  title VARCHAR(15),
  pub_yr VARCHAR(15),
  pname VARCHAR(15),
  PRIMARY KEY(book_id),
  foreign key (pname) REFERENCES Publisher(pname));

CREATE TABLE Author(
  aname VARCHAR(15),
  book_id INT,
  PRIMARY KEY(book_id,aname),
  foreign key(book_id) REFERENCES Book(book_id) ON DELETE CASCADE);

CREATE TABLE Library_Branch(
  branch_id INT,
  bname VARCHAR(30),
  address VARCHAR(30),
  PRIMARY KEY(branch_id));

CREATE TABLE Book_Copies(
  no_of_copies INT,
  book_id INT,
  branch_id INT,
  PRIMARY KEY(book_id,branch_id),
  foreign key(book_id) REFERENCES Book(book_id) ON DELETE CASCADE,
  foreign key(branch_id) REFERENCES Library_Branch(branch_id) ON DELETE CASCADE);

CREATE TABLE Card(
  card_no INT,
  PRIMARY KEY(card_no));

CREATE TABLE Book_Lending(
  date_out date,
  due_date date,
  book_id INT,
  branch_id INT,
  card_no INT,
  PRIMARY KEY(book_id,branch_id,card_no),
  foreign key(book_id) REFERENCES Book(book_id) ON DELETE CASCADE,
  foreign key(branch_id) REFERENCES Library_Branch(branch_id) ON DELETE CASCADE,
  foreign key(card_no) REFERENCES Card(card_no) ON DELETE CASCADE);


INSERT INTO PUBLISHER VALUES ('MCGRAW-HILL', 9989076587, 'BANGALORE'); 
INSERT INTO PUBLISHER VALUES ('PEARSON', 9889076565, 'NEWDELHI'); 
INSERT INTO PUBLISHER VALUES ('RANDOM HOUSE', 7455679345, 'HYDRABAD'); 
INSERT INTO PUBLISHER VALUES ('HACHETTE LIVRE', 8970862340, 'CHENAI'); 
INSERT INTO PUBLISHER VALUES ('GRUPO PLANETA', 7756120238, 'BANGALORE'); 

INSERT INTO BOOK VALUES (1,'DBMS','JAN-2017', 'MCGRAW-HILL'); 
INSERT INTO BOOK VALUES (2,'ADBMS','JUN-2016', 'MCGRAW-HILL'); 
INSERT INTO BOOK VALUES (3,'CN','SEP-2016', 'PEARSON'); 
INSERT INTO BOOK VALUES (4,'CG','SEP-2015', 'GRUPO PLANETA'); 
INSERT INTO BOOK VALUES (5,'OS','MAY-2016', 'PEARSON'); 

INSERT INTO AUTHOR VALUES ('NAVATHE', 1); 
INSERT INTO AUTHOR VALUES ('NAVATHE', 2); 
INSERT INTO AUTHOR VALUES ('TANENBAUM', 3); 
INSERT INTO AUTHOR VALUES ('EDWARD ANGEL', 4); 
INSERT INTO AUTHOR VALUES ('GALVIN', 5); 

INSERT INTO LIBRARY_BRANCH VALUES (10,'RR NAGAR','BANGALORE'); 
INSERT INTO LIBRARY_BRANCH VALUES (11,'RNSIT','BANGALORE'); 
INSERT INTO LIBRARY_BRANCH VALUES (12,'RAJAJI NAGAR', 'BANGALORE'); 
INSERT INTO LIBRARY_BRANCH VALUES (13,'NITTE','MANGALORE'); 
INSERT INTO LIBRARY_BRANCH VALUES (14,'MANIPAL','UDUPI'); 

INSERT INTO BOOK_COPIES VALUES (10, 1, 10); 
INSERT INTO BOOK_COPIES VALUES (5, 1, 11); 
INSERT INTO BOOK_COPIES VALUES (2, 2, 12); 
INSERT INTO BOOK_COPIES VALUES (5, 2, 13); 
INSERT INTO BOOK_COPIES VALUES (7, 3, 14); 
INSERT INTO BOOK_COPIES VALUES (1, 5, 10); 
INSERT INTO BOOK_COPIES VALUES (3, 4, 11); 

INSERT INTO CARD VALUES (100); 
INSERT INTO CARD VALUES (101); 
INSERT INTO CARD VALUES (102); 
INSERT INTO CARD VALUES (103); 
INSERT INTO CARD VALUES (104);

INSERT INTO BOOK_LENDING VALUES ('2017-01-01','2017-06-01', 1, 10, 101); 
INSERT INTO BOOK_LENDING VALUES ('2017-01-11','2017-03-11', 3, 14, 101); 
INSERT INTO BOOK_LENDING VALUES ('2017-02-21','2017-04-21', 2, 13, 101); 
INSERT INTO BOOK_LENDING VALUES ('2017-03-15','2017-07-15', 4, 11, 101); 
INSERT INTO BOOK_LENDING VALUES ('2017-04-12','2017-05-12', 1, 11, 104); 

/*1. Retrieve details of all books in the library – id, title, name of publisher, authors, number of copies in each branch, etc. */

SELECT B.BOOK_ID, B.TITLE, B.PNAME, A.ANAME, C.NO_OF_COPIES, L.BRANCH_ID 
FROM BOOK B, AUTHOR A, BOOK_COPIES C, LIBRARY_BRANCH L 
WHERE B.BOOK_ID=A.BOOK_ID 
AND B.BOOK_ID=C.BOOK_ID 
AND L.BRANCH_ID=C.BRANCH_ID;	

/*2. Get the particulars of borrowers who have borrowed more than 3 books, but from Jan 2017 to Jun 2017. */
SELECT CARD_NO 
FROM BOOK_LENDING 
WHERE DATE_OUT BETWEEN 2017-01-01 AND 2017-06-01 
GROUP BY CARD_NO 
HAVING COUNT(*)>3;

/* 3.Delete a book in BOOK table. Update the contents of other tables to reflect this data manipulation operation. */
DELETE FROM BOOK
WHERE BOOK_ID=3;

/* 4.Partition the BOOK table based on year of publication. Demonstrate its working with a simple query. */
CREATE VIEW V_PUBLICATION AS 
SELECT PUB_YR 
FROM BOOK;
SELECT * FROM V_PUBLICATION;

/*5. Create a view of all books and its number of copies that are currently available in the Library. */
CREATE VIEW V_BOOKS AS 
SELECT B.BOOK_ID, B.TITLE, C.NO_OF_COPIES 
FROM BOOK B, BOOK_COPIES C, LIBRARY_BRANCH L 
WHERE B.BOOK_ID=C.BOOK_ID 
AND C.BRANCH_ID=L.BRANCH_ID;

SELECT * FROM V_BOOKSCREATE DATABASE