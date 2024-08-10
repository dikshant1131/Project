from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from tkinter import filedialog
import platform
import psutil
from PIL import Image,ImageTk

#brightness
import screen_brightness_control as pct

# audio
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities , IAudioEndpointVolume

# weather
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

# clock 
from time import strftime

#calendar
from tkcalendar import *

# open google
import pyautogui 
import subprocess
import webbrowser as wb
import random


root=Tk()
root.title('Mac-Soft Tool')
root.geometry('1200x700')
root.resizable(False,False)
root.configure(bg='#292e2e')

#icone 
# image_icon=PhotoImage('icon.png')
# root.iconphoto(False,image_icon)

windo_image = Image.open("icon.png")        # it is used to add  the icone in the windor 
image_icon = ImageTk.PhotoImage(windo_image)
root.iconphoto(False,image_icon)

Body=Frame(root,width=1200,height=900,bg='#d6d6d6')   
Body.pack(pady=20,padx=20)
#-----------------------------------------
LHS=Frame(Body,width=400,height=735,bg='#f4f5f5',highlightbackground='#adacb1',highlightthickness=1)
LHS.place(x=10,y=10)
# LOGO
photo=PhotoImage(file="laptop.png")
myimage=Label(LHS,image=photo,background='#f4f5f5')
myimage.place(x=-40,y=-20)

# logo_image=Image.open('laptop.png').resize((8,10))
# image_logo= ImageTk.PhotoImage(logo_image)
# image_logo=Label(LHS,image=image_logo,background='#f4f5f5')
# image_logo.place(x=-2,y=10)

my_system=platform.uname()
l1=Label(LHS,text=my_system.node,bg="#f4f5f5",font=('Acumin Variable Concept',15,'bold'),justify='center')
l1.place(x=20,y=300)

l2=Label(LHS,text=f'Version:{my_system.version}',bg="#f4f5f5",font=('Acumin Variable Concept',8),justify='center')
l2.place(x=20,y=330)


l3=Label(LHS,text=f'System:{my_system.system}',bg="#f4f5f5",font=('Acumin Variable Concept',15),justify='center')
l3.place(x=20,y=350)


l4=Label(LHS,text=f'Machine:{my_system.machine}',bg="#f4f5f5",font=('Acumin Variable Concept',15),justify='center')
l4.place(x=20,y=390)


l5=Label(LHS,text=f'Total Ram installed:{round(psutil.virtual_memory().total/1000000000,2)}GB',bg="#f4f5f5",font=('Acumin Variable Concept',15),justify='center')
l5.place(x=20,y=420)


l6=Label(LHS,text=f'Processor:{my_system.processor}',bg="#f4f5f5",font=('Acumin Variable Concept',7,'bold'),justify='center')
l6.place(x=20,y=460)

l7=Label(LHS,text='Dikshant',bg="#f4f5f5",font=('Acumin Variable Concept',15,'bold'),justify='center')
l7.place(x=10,y=550)







#-----------------------------------------
RHS=Frame(Body,width=710,height=300,bg='#f4f5f5',highlightbackground='#adacb1',highlightthickness=1)
RHS.place(x=430,y=10)

system=Label(RHS,text='System:',font=('Acumin Variable Concept',20,'bold'),bg='#f4f5f5')
system.place(x=10,y=10)

###### Battery#############################################3
def convertTime(seconds):
    minutes,seconds=divmod(seconds,60)
    hours,minutes=divmod(minutes,60)
    return '%d:%02d:%02d'% (hours,minutes,seconds)

def none():
    global battery_png
    global battery_label
    battery=psutil.sensors_battery()
    percent=battery.percent
    time=convertTime(battery.secsleft)

    # print(percent)
    # print(time)

    lbl.config(text=f'{percent}%')
    lbl_plug.config(text=f'Plug in:{str(battery.power_plugged)}',font=('Acumin Variable Concept',20,'bold'))
    lbl_time.config(text=f'{time}remaining',font=('Acumin Variable Concept',15,'bold'))
    lbl_time.place(x=350,y=150)
    lbl.place(x=350,y=50)
    lbl_plug.place(x=350,y=200)


    battery_label=Label(RHS,background='#f4f5f5')
    battery_label.place(x=0,y=50)

    
   


    lbl.after(1000,none)

    if battery.power_plugged==True:
        battery_png=PhotoImage(file="charging.png")
        battery_label.config(image=battery_png)
    else:
        battery_png=PhotoImage(file='battery.png')
        battery_label.config(image=battery_png)
    



    

lbl=Label(RHS,font=('Acumin Variable Concept',40,'bold'),bg='#f4f5f5')
lbl.place(x=200,y=40)

lbl_plug=Label(RHS,font=('Acumin Variable Concept',10),bg='#f4f5f5')
lbl_plug.place(x=20,y=100)

lbl_time=Label(RHS,font=('Acumin Variable Concept',15),bg='#f4f5f5')
lbl_time.place(x=200,y=100)

none()

##############################################

#######################################Speaker###############################
lbl_speaker=Label(RHS,text='Speaker:',font=('arial',12,'bold'),bg='#f4f5f5')
lbl_speaker.place(x=10,y=200)
volume_value=tk.DoubleVar()

def get_current_volume_value():
    return '{: .2f}'.format(volume_value.get())



def volume_changed(event):
    device=AudioUtilities.GetSpeakers()
    interface = device.Activate(IAudioEndpointVolume._iid_,CLSCTX_ALL,None)
    volume = cast(interface,POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevel(-float(get_current_volume_value()),None)


style=ttk.Style()
style.configure('TScale',background='#f4f5f5')

volume=ttk.Scale(RHS,from_=60,to=0,orient='horizontal',command=volume_changed,variable=volume_value)

volume.place(x=100,y=205)
volume.set(20)
##################################################
###############Brightness###############################
lbl_brightness=Label(RHS,text='Brightness:',font=('arial',12,'bold'),bg='#f4f5f5')
lbl_brightness.place(x=10,y=250)
current_value=tk.DoubleVar()

def get_current_value():
    return  '{: .2f}'.format(current_value.get())

def brightness_changed(event):
    pct.set_brightness(get_current_value())



brightness=ttk.Scale(RHS,from_=0,to=100,orient='horizontal',command=brightness_changed,variable=current_value)
brightness.place(x=130,y=250)
##############################################################################
def weather():
    app1=Toplevel()
    app1.geometry('750x750')
    app1.title('Weather')
    app1.configure(bg='#f4f5f5')
    app1.resizable(False,False)


    #icone:
    image_icon=PhotoImage(file='wether.png')
    app1.iconphoto(False,image_icon)

    def getWeather():
        try:

            city=textfield.get()

            geolocator=Nominatim(user_agent='geoapiExercises')
            location=geolocator.geocode(city)
            obj=TimezoneFinder()
            result=obj.timezone_at(lng=location.longitude,lat=location.latitude)

            home=pytz.timezone(result)
            local_time=datetime.now(home)
            current_time=local_time.strftime('%I:%M:%p')
            clock.config(text=current_time)
            name.config(text='CURRENT WEATHER')

            # weather:
            api='https://api.openweathermap.org/data/2.5/weather?lat='+city+'12e1b8983337f6191c355bdaad158b9e'
            json_data= requests.get(api).json()
            condition = json_data['weather'][0]['main']
            description= json_data['weather'][0]['description']
            temp = int(json_data['main']['temp']-270.15)
            pressure = json_data['main']['pressure']
            humidity= json_data['main']['humidity']
            wind= json_data['wind']['speed']

            t.config(text=(temp,'°'))
            c.config(text=(condition,'|','FEELS','LIKE',temp,'°'))

            w.config(text=wind)
            h.config(text=humidity)
            d.config(text=description)
            p.config(text=pressure)



        except Exception as e:
            messagebox.showerror('Weather App')
            

    # Search box :
    Search_image= PhotoImage(file='dishu.png')
    myimage=Label(app1,image=Search_image,bg='#f4f5f5')
    myimage.place(x=20,y=20)

    textfield=tk.Entry(app1,justify='center',width=17,font=('poppins',25,'bold'),bg='#404040',border=0,fg='white')
    textfield.place(x=50,y=40)
    textfield.focus()

    Search_icon=PhotoImage(file='search_icon.png')
    myimage_icon=Button(app1,image=Search_icon,borderwidth=0,cursor='hand2',bg='#404040',command=getWeather)
    myimage_icon.place(x=400,y=34)

    # logo:
    Logo_image=PhotoImage(file='logo.png')
    logo=Label(app1,image=Logo_image,bg='#f4f5f5')
    logo.place(x=150,y=100)

    # bottom box:
    Frame_image=PhotoImage(file='box.png')
    frame_myimage=Label(app1,image=Frame_image,bg='#f4f5f5')
    frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

    # time
    name=Label(app1,font=('arial',15,'bold'),bg='#f4f5f5')
    name.place(x=30,y=100)
    clock=Label(app1,font=('Helvetica',20),bg='#f4f5f5')
    clock.place(x=30,y=130)

    # label:
    label1=Label(app1,text='WIND',font=('Helvatica',15,'bold'),fg='white',bg='#1ab5ef')
    label1.place(x=60,y=650)

    label2=Label(app1,text='HUMIDITY',font=('Helvatica',15,'bold'),fg='white',bg='#1ab5ef')
    label2.place(x=180,y=650)


    label3=Label(app1,text='DESCRIPTION',font=('Helvatica',15,'bold'),fg='white',bg='#1ab5ef')
    label3.place(x=350,y=650)

    label4=Label(app1,text='PRESSURE',font=('Helvatica',15,'bold'),fg='white',bg='#1ab5ef')
    label4.place(x=550,y=650)

    t=Label(app1,font=('arial',70,'bold'),fg='#ee666d',bg='#f4f5f5')
    t.place(x=400,y=150)

    c=Label(app1,font=('arial',15,'bold'),fg='#ee666d',bg='#f4f5f5')
    c.place(x=400,y=250)
    
    w=Label(app1,text='. . .',font=('arial',20,'bold'),bg='#1ab5ef')
    w.place(x=65,y=680)
    
    h=Label(app1,text='. . .',font=('arial',20,'bold'),bg='#1ab5ef')
    h.place(x=200,y=680)
    
    d=Label(app1,text='. . .',font=('arial',20,'bold'),bg='#1ab5ef')
    d.place(x=390,y=680)
    
    
    p=Label(app1,text='. . .',font=('arial',20,'bold'),bg='#1ab5ef')
    p.place(x=590,y=680)
    
    







    app1.mainloop()


def clock():
    app2=Toplevel()
    app2.geometry('800x200')
    app2.configure(bg='#292e2e')
    app2.resizable(False,False)
    # icon:
    image_icon=PhotoImage(file='App2.png')
    app2.iconphoto(False,image_icon)
    def clock():
        text=strftime('%H:%M:%S %p')
        lbl.config(text=text)
        lbl.after(1000,clock)


    lbl=Label(app2,font=('digital-7',50,'bold'),width=20,bg='#f4f5f5',fg='#292e2e')
    lbl.pack(anchor='center',pady=20)
    clock()




    app2.mainloop()


def calendar():
    app3=Toplevel()
    app3.geometry('300x300')
    app3.title('Calender')
    app3.configure(bg='#292e2e')
    app3.resizable(False,False)


    # icon:
    image_icon=PhotoImage(file='App3.png')
    app3.iconphoto(False,image_icon)

    mycal=Calendar(app3,setmode='day',date_pattern='d/m/yy')
    mycal.pack(padx=15,pady=35)





    app3.mainloop()
################mode##################################################

button_mode=True    

def mode():
    global button_mode
    if button_mode:
        LHS.config(bg='#292e2e')
        myimage.config(bg='#292e2e')
        l1.config(bg='#292e2e',fg='#d6d6d6')
        l2.config(bg='#292e2e',fg='#d6d6d6')
        l3.config(bg='#292e2e',fg='#d6d6d6')
        l4.config(bg='#292e2e',fg='#d6d6d6')
        l5.config(bg='#292e2e',fg='#d6d6d6')
        l6.config(bg='#292e2e',fg='#d6d6d6')

        RHB.config(bg='#292e2e')
        app1.config(bg='#292e2e')
        app2.config(bg='#292e2e')
        app3.config(bg='#292e2e')
        app4.config(bg='#292e2e')
        app5.config(bg='#292e2e')
        app6.config(bg='#292e2e')
        app7.config(bg='#292e2e')
        app8.config(bg='#292e2e')
        app9.config(bg='#292e2e')
        app10.config(bg='#292e2e')
        apps.config(bg='#292e2e',fg='#d6d6d6')








        






        button_mode=False

    else:
        LHS.config(bg='#f4f5f5')
        myimage.config(bg='#f4f5f5')
        l1.config(bg='#f4f5f5',fg='#292e2e')
        l2.config(bg='#f4f5f5',fg='#292e2e')
        l3.config(bg='#f4f5f5',fg='#292e2e')
        l4.config(bg='#f4f5f5',fg='#292e2e')
        l5.config(bg='#f4f5f5',fg='#292e2e')
        l6.config(bg='#f4f5f5',fg='#292e2e')

        RHB.config(bg='#f4f5f5')
        app1.config(bg='#f4f5f5')
        app2.config(bg='#f4f5f5')
        app3.config(bg='#f4f5f5')
        app4.config(bg='#f4f5f5')
        app5.config(bg='#f4f5f5')
        app6.config(bg='#f4f5f5')
        app7.config(bg='#f4f5f5')
        app8.config(bg='#f4f5f5')
        app9.config(bg='#f4f5f5')
        app10.config(bg='#f4f5f5')

        apps.config(bg='#f4f5f5',fg='#292e2e')

        


        

        button_mode=True


######################game##############################
def game():
    app5=Toplevel()
    app5.geometry('700x700')
    app5.title('Ludo')
    app5.configure(bg='#dee2e5')
    app5.resizable(False,False)

    # icon:
    image_icon=PhotoImage(file='App5.png')
    app5.iconphoto(False,image_icon)

    app5.mainloop()


#################screenshot###########################33
def screenshot():
    root.iconify()
    myScreenshot=pyautogui.screenshot()
    file_path=filedialog.asksaveasfilename(defaultextension='.png')
    myScreenshot.save(file_path)


def file():
    subprocess.Popen(r'explorer /select,"C:\path\of\folder\file"')

def crome():
    wb.register('chrome',None)
    wb.open("https://www.gppgle.com/")

def close_apps():
    wb.register('chrome',None)
    wb.open("https://www.youtube.com")

def close_window():
    root.destroy()



        

#-----------------------------------------
RHB=Frame(Body,width=710,height=300,bg='#f4f5f5',highlightbackground='#adacb1',highlightthickness=1)
RHB.place(x=430,y=350)

apps=Label(RHB,text='Apps :',font=('Acumin Variable Concept',20,'bold'),bg='#f4f5f5')
apps.place(x=30,y=10)

app1_image=PhotoImage(file='wether.png') 
app1=Button(RHB,image=app1_image,bd=0,command=weather)     
app1.place(x=15,y=60)    

app2_image=PhotoImage(file='clock.png') 
app2=Button(RHB,image=app2_image,bd=0,command=clock)
app2.place(x=130,y=60)       

app3_image=PhotoImage(file='images.png')
app3=Button(RHB,image=app3_image,bd=0,command=calendar)
app3.place(x=260,y=60) 

app4_image=PhotoImage(file='switch.png')
app4=Button(RHB,image=app4_image,bd=0,command=mode)
app4.place(x=380,y=60)

app5_image=PhotoImage(file='ludo.png')
app5=Button(RHB,image=app5_image,bd=0,command=game)
app5.place(x=500,y=50)

app6_image=PhotoImage(file='camra.png')
app6=Button(RHB,image=app6_image,bd=0,command=screenshot)
app6.place(x=15,y=150)

app7_image=PhotoImage(file='file.png')
app7=Button(RHB,image=app7_image,bd=0,command=file)
app7.place(x=130,y=150)

app8_image=PhotoImage(file='google.png')
app8=Button(RHB,image=app8_image,bd=0,command=crome)
app8.place(x=260,y=150)


app9_image=PhotoImage(file='youtube.png')
app9=Button(RHB,image=app9_image,bd=0,command=close_apps)
app9.place(x=380,y=150)


app10_image=PhotoImage(file='App10.png')
app10=Button(RHB,image=app10_image,bd=0,command=close_window)
app10.place(x=520,y=150)







root.mainloop()
