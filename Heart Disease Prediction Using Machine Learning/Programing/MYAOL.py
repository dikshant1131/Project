import mysql.connector
from tkinter import messagebox

# 
def Save_Data_MySql(B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R):
    try:
        mydb = mysql.connector.connect(host='localhost',user='root')
        mycursor=mydb.cursor()
        print('connection stablished!')
#    
    except:
       messagebox.showerror('connection','Database connection not stablished!')

    try:
       command='create database Heart_Data'
       mycursor.execute(command)

       command='use Heart_Data'
       mycursor.execute(command)

       command='create table data(user int auto_increment key not null, Name varchar(50),Date varchar(100),DOB varchar(100),age varchar(100),sex varchar(100),Cp varchar(100),trestbps varchar(100),chol varchar(100),fbs varchar(100),restecg varchar(100),thalach varchar(100),exang varchar(100),oldpeak varchar(100),slop varchar(100),thal varchar(100),result varchar(100))'
       mycursor.execute(command)

       command='insert into data(Name,Date,DOB,age,sex,Cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slop,ca,thal,Result) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
       mycursor.execute(command,(B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R))
       mydb.commit()
       mydb.close()
       messagebox.showinfo('Register','New user added sucessfull!!!!!')#yrr isme ek rakho ya heart_data ya hear
    except:
        messagebox.showerror('info','there is mistake in the above code!!!!')

Save_Data_MySql('dishu','08/08/2024','2005','44','1','1','233','233','1','1','233','1','233.0','0','2','1','0')