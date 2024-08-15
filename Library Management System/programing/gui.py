import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from datetime import datetime as dt
import mysql.connector 

con = mysql.connector.connect(user = "root", host = "localhost")
mycursor = con.cursor()
mycursor.execute("use library_management_db")

login_window = tk.Tk()
login_window.geometry("800x500")
login_window.title("Admin Login")
# login_window.config(bg="#FFFACD")
# login_window.resizable(False,False)
img=Image.open("admin_background.jpg").resize((800,500))
bck_end=ImageTk.PhotoImage(img)
lbl=tk.Label(login_window,image=bck_end)
lbl.place(x=0,y=0)

def book_details():
    def add_book():
        title = title_entry.get()
        author= author_entry.get()
        copies= copies_entry.get()
        try: 
            mycursor.execute(f"""
insert into books_details (title, author, copies) values 
("{title}","{author}",{copies});
""")
            con.commit()
            messagebox.showinfo("Info","Details Added Successfully!")
        except Exception as e:
            messagebox.showerror("Error",e)
        
    book_details_window = tk.Toplevel()
    book_details_window.geometry("900x600")
    book_details_window.title("Book details")
    # book_details_window.resizable(False,False)
    img = Image.open("book_detail_img.jpeg").resize((900, 600))
    bck_end = ImageTk.PhotoImage(img)
    lbl = tk.Label(book_details_window, image=bck_end)
    lbl.place(x=0, y=0)
    lbl.image = bck_end 

    tk.Label(book_details_window,text="ADD BOOK TO LIBRARY",font=("Braggadocio",35,"underline"),fg="#EAAC7F",bg="#3E3838",width=30).pack(pady=12)

    tk.Label(book_details_window,text="Enter book title ",font=("Copperplate Gothic",25,"italic"),width=15,bg="#493323",fg="#FFDF91").place(x=180,y=110)
    title_entry = tk.Entry(book_details_window,font=("Bradley Hand",25,"italic"),fg="black",bg="#91684A")
    title_entry.place(x=450,y=110)

    tk.Label(book_details_window,text="Enter book author",font=("Copperplate Gothic",25,"italic"),width=15,bg="#493323",fg="#FFDF91").place(x=180,y=180)
    author_entry=tk.Entry(book_details_window,font=("Bradley Hand",25,"italic"),fg="black",bg="#91684A")
    author_entry.place(x=450,y=180)

    tk.Label(book_details_window,text="No. of copies",font=("Copperplate Gothic",25,"italic"),width=15,bg="#493323",fg="#FFDF91").place(x=180,y=250)
    copies_entry=tk.Entry(book_details_window,font=("Bradley Hand",25,"italic"),fg="black",bg="#91684A")
    copies_entry.place(x=450,y=250)

    tk.Button(book_details_window,text="Submit",font=("Baloo Bhaijaan",30,"bold"),fg="red",bg="white",borderwidth=7,relief="raised",command=add_book).place(x=380,y=350)

def issue_book():
    issue_book_window = tk.Toplevel()
    issue_book_window.geometry("900x600")
    issue_book_window.title("Issue Book")
    issue_book_window.resizable(False,False)
    img = Image.open("issue_book_img.jpeg").resize((900, 600))
    bck_end = ImageTk.PhotoImage(img)
    lbl = tk.Label(issue_book_window, image=bck_end)
    lbl.place(x=0, y=0)
    lbl.image = bck_end 

    def issue():
        book_id = book_id_entry.get()
        student_id = student_id_entry.get()
        date = dt.now().strftime("%Y-%m-%d")
        mycursor.execute(f"select copies from books_details where book_id = {book_id}")
        copies = mycursor.fetchall()[0][0]
        if copies>0:
            mycursor.execute(f"insert into book_entries (book_id, student_id,issue_date) value ({book_id},{student_id},'{date}')")
            mycursor.execute(f"update books_details set copies = copies-1 where book_id = {book_id}")
            con.commit()
            messagebox.showinfo("Info","Book is issued successfully!")
        else:
            messagebox.showinfo("Info","Book is currently unavailable!")

    tk.Label(issue_book_window,text="ISSUE A BOOK",font=("Braggadocio",35,"underline"),fg="#EAAC7F",bg="#3E3838",width=30).pack(pady=23)

    tk.Label(issue_book_window,text="Enter book ID",font=("Copperplate Gothic",25,"italic"),width=15,bg="#493323",fg="#FFDF91").place(x=180,y=140)
    book_id_entry = tk.Entry(issue_book_window,font=("Bradley Hand",25,"italic"),fg="black",bg="#91684A")
    book_id_entry.place(x=450,y=140)

    tk.Label(issue_book_window,text="Enter Student ID",font=("Copperplate Gothic",25,"italic"),width=15,bg="#493323",fg="#FFDF91").place(x=180,y=210)
    student_id_entry=tk.Entry(issue_book_window,font=("Bradley Hand",25,"italic"),fg="black",bg="#91684A")
    student_id_entry.place(x=450,y=210)

    tk.Button(issue_book_window,text="Submit",font=("Baloo Bhaijaan",30,"bold"),fg="red",bg="white",borderwidth=7,relief="raised",command=issue).place(x=380,y=350)

def return_book():
    return_book_window = tk.Toplevel()
    return_book_window.geometry("900x600")
    return_book_window.title("Return Book")
    return_book_window.resizable(False,False)
    img = Image.open("return_book_img.jpeg").resize((900, 600))
    bck_end = ImageTk.PhotoImage(img)
    lbl = tk.Label(return_book_window, image=bck_end)
    lbl.place(x=0, y=0)
    lbl.image = bck_end 

    def book_return():
        book_id = book_id_entry.get()
        student_id = student_id_entry.get()
        date = dt.now().strftime("%Y-%m-%d")
        try:
            command =f"update book_entries set return_date ='{date}' where student_id={student_id} and book_id={book_id} "
            mycursor.execute(command)
            updatebook=f"update books_details set copies=copies+1 where book_id ={book_id}"
            mycursor.execute(updatebook)
            con.commit()
            messagebox.showinfo("Info","Book is returned successfully!")
        except Exception as e:
            print(e)
            messagebox.showinfo("Info","No such issued data is present")

    tk.Label(return_book_window,text="RETURN A BOOK",font=("Braggadocio",35,"underline"),fg="#EAAC7F",bg="#3E3838",width=30).pack(pady=23)

    tk.Label(return_book_window,text="Enter book ID",font=("Copperplate Gothic",25,"italic"),width=15,bg="#493323",fg="#FFDF91").place(x=180,y=140)
    book_id_entry = tk.Entry(return_book_window,font=("Bradley Hand",25,"italic"),fg="black",bg="#91684A")
    book_id_entry.place(x=450,y=140)

    tk.Label(return_book_window,text="Enter Student ID",font=("Copperplate Gothic",25,"italic"),width=15,bg="#493323",fg="#FFDF91").place(x=180,y=210)
    student_id_entry=tk.Entry(return_book_window,font=("Bradley Hand",25,"italic"),fg="black",bg="#91684A")
    student_id_entry.place(x=450,y=210)

    tk.Button(return_book_window,text="Submit",font=("Baloo Bhaijaan",30,"bold"),fg="red",bg="white",borderwidth=7,relief="raised",command=book_return).place(x=380,y=350)


def show_books():
    show_book_window = tk.Toplevel()
    show_book_window.geometry("900x600")
    show_book_window.title("Show Book ")
    show_book_window.resizable(False,False)
    img = Image.open("show_books_img.jpeg").resize((900, 600))
    bck_end = ImageTk.PhotoImage(img)
    lbl = tk.Label(show_book_window, image=bck_end)
    lbl.place(x=0, y=0)
    lbl.image = bck_end 

    def display_books():
        mycursor.execute("SELECT * FROM books_details")
        books = mycursor.fetchall()
        book_list = tk.Listbox(show_book_window, font=("Bradley Hand", 20), bg="#FFFACD", fg="#3D2B1F")
        book_list.place(x=50, y=100, width=800, height=400)
        for book in books:
            book_list.insert(tk.END, f"ID: {book[0]}|\t Title: {book[1]}|\t\t Author: {book[2]}|\t\t Copies: {book[3]}")

    tk.Label(show_book_window, text="BOOK DETAILS", font=("Braggadocio", 35, "underline"), fg="#EAAC7F", bg="#3E3838", width=30).pack(pady=23)
    display_books()

def show_students():
    show_students_window = tk.Toplevel()
    show_students_window.geometry("900x600")
    show_students_window.title("Student details")
    show_students_window.resizable(False,False)
    img = Image.open("show_students_img.jpeg").resize((900, 600))
    bck_end = ImageTk.PhotoImage(img)
    lbl = tk.Label(show_students_window, image=bck_end)
    lbl.place(x=0, y=0)
    lbl.image = bck_end 

    def display_students():
        mycursor.execute("SELECT * FROM student_details")
        students = mycursor.fetchall()
        student_list = tk.Listbox(show_students_window, font=("Bradley Hand", 20), bg="#FFFACD", fg="#3D2B1F")
        student_list.place(x=50, y=100, width=800, height=400)
        for student in students:
            student_list.insert(tk.END, f"ID: {student[0]}\t| \tName: {student[1]}\t\t\t Class: {student[2]}")

    tk.Label(show_students_window, text="STUDENT DETAILS", font=("Braggadocio", 35, "underline"), fg="#EAAC7F", bg="#3E3838", width=30).pack(pady=23)
    display_students()

def main_window():

    new_window = tk.Toplevel(login_window)
    new_window.geometry("900x600") 
    new_window.title("Library Management System")
    new_window.resizable(False,False)
    img = Image.open("library.png").resize((900, 600))
    bck_end = ImageTk.PhotoImage(img)
    lbl = tk.Label(new_window, image=bck_end)
    lbl.place(x=0, y=0)
    lbl.image = bck_end  # Keep a reference to avoid garbage collection

    tk.Label(new_window,text="Welcome to Library Management System",bg="#FFFACD",fg="#3D2B1F",font=("Braggadocio",40,"bold underline")).pack(pady=60)

    tk.Button(new_window,text="Add Book Details",font=("Cooper",30,"bold"),bg="#FFFACD",fg="#3D2B1F",command= book_details,width=35).pack(pady=10)

    tk.Button(new_window,text="Issue Book",font=("Cooper",30,"bold"),bg="#FFFACD",fg="#3D2B1F",command= issue_book,width=35).pack(pady=10)

    tk.Button(new_window,text="Return Book",font=("Cooper",30,"bold"),bg="#FFFACD",fg="#3D2B1F",command= return_book,width=35).pack(pady=10)

    tk.Button(new_window,text="Show books detail",font=("Cooper",30,"bold"),bg="#FFFACD",fg="#3D2B1F",command= show_books,width=35).pack(pady=10)

    tk.Button(new_window,text="Show student detail",font=("Cooper",30,"bold"),bg="#FFFACD",fg="#3D2B1F",command= show_students,width=35).pack(pady=10)

    new_window.mainloop()

def login():
    if id_entry.get() == "harpreet@gmail.com" and password_entry.get() == "Harpreet":
        main_window()
    else:
        messagebox.showerror("Error","Invalid Password/ User ID")

tk.Label(login_window,text="Welcome to Library Management System", fg="white",bg="#3D2B1F",font=("Copperplate Gothic",30,"bold"),width=30).pack(pady=20)

tk.Label(login_window,text="Enter Admin ID",font=("Bradley Hand",25,"bold"),width=45,bg="#4B3621",fg="white").pack(pady=30)
id_entry = tk.Entry(login_window,font=("Bradley Hand",25,"italic"),width=45,bg="white",fg="#3D2B1F")
id_entry.pack()

tk.Label(login_window,text="Enter Password",font=("Bradley Hand",25,"bold"),width=45,bg="#4B3621",fg="white").pack(pady=30)
password_entry = tk.Entry(login_window,font=("Bradley Hand",25,"italic"),width=45,bg="white",fg="#3D2B1F")
password_entry.pack()

submit_button = tk.Button(login_window,text="Login",font=("Academy Engraved LET",25,"bold"),fg="red",borderwidth=7,command=login)
submit_button.pack(pady=40)


login_window.mainloop()