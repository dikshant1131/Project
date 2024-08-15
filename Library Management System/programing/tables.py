import mysql.connector

con = mysql.connector.connect(user = "root", host = "localhost")
mycursor = con.cursor()

mycursor.execute("create database library_management_db;")
mycursor.execute("use library_management_db")
mycursor.execute("""
Create table books_details 
(book_id int Primary key auto_increment,
title varchar(50) unique not null,
author varchar(50) ,
copies int 
);
""")

mycursor.execute("""
create table student_details (
student_id int Primary Key,
student_name varchar(50) not null,
class char(5) not null
);
""")

mycursor.execute("""
create table book_entries(
book_id int,
student_id int,
issue_date date,
return_date date,
foreign key (book_id) references books_details(book_id),
foreign key (student_id) references student_details(student_id)   
);
""")

con.commit()
mycursor.close()