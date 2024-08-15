import mysql.connector

con = mysql.connector.connect(user = "root", host = "localhost")
mycursor = con.cursor()
mycursor.execute("use library_management_db")
mycursor.execute("""
INSERT INTO books_details ( title, author, copies) VALUES 
( 'To Kill a Mockingbird', 'Harper Lee', 5),
( '1984', 'George Orwell', 4),
( 'The Great Gatsby', 'F. Scott Fitzgerald', 3),
( 'The Catcher in the Rye', 'J.D. Salinger', 6),
( 'The Hobbit', 'J.R.R. Tolkien', 7),
( 'Pride and Prejudice', 'Jane Austen', 2),
( 'The Lord of the Rings', 'J.R.R. Tolkien', 8),
( 'Animal Farm', 'George Orwell', 5),
( 'Jane Eyre', 'Charlotte Bronte', 4),
( 'The Book Thief', 'Markus Zusak', 3),
( 'The Chronicles of Narnia', 'C.S. Lewis', 6),
( 'Wuthering Heights', 'Emily Bronte', 7),
( 'Harry Potter and the Sorcerers Stone', 'J.K. Rowling', 10),
( 'Harry Potter and the Chamber of Secrets', 'J.K. Rowling', 10),
( 'Harry Potter and the Prisoner of Azkaban', 'J.K. Rowling', 10),
( 'Harry Potter and the Goblet of Fire', 'J.K. Rowling', 10),
( 'Harry Potter and the Order of the Phoenix', 'J.K. Rowling', 10),
( 'Harry Potter and the Half-Blood Prince', 'J.K. Rowling', 10),
( 'Harry Potter and the Deathly Hallows', 'J.K. Rowling', 10),
( 'The Alchemist', 'Paulo Coelho', 5);
""")

mycursor.execute("""
INSERT INTO student_details (student_id, student_name, class) VALUES 
(1, 'Alice Johnson', '10A'),
(2, 'Bob Smith', '10A'),
(3, 'Charlie Brown', '10B'),
(4, 'David Wilson', '10B'),
(5, 'Eva Green', '10C'),
(6, 'Frank White', '10C'),
(7, 'Grace Harris', '10D'),
(8, 'Henry Walker', '10D'),
(9, 'Isabel King', '11A'),
(10, 'Jack Baker', '11A'),
(11, 'Katie Morgan', '11B'),
(12, 'Liam Scott', '11B'),
(13, 'Mia Rogers', '11C'),
(14, 'Noah Reed', '11C'),
(15, 'Olivia Perry', '11D'),
(16, 'Paul Russell', '11D'),
(17, 'Quincy Young', '12A'),
(18, 'Rachel Edwards', '12A'),
(19, 'Samuel Fisher', '12B'),
(20, 'Tina Foster', '12B');
""")

con.commit()
mycursor.close()