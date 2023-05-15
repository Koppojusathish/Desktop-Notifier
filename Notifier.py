from tkinter import *
import tkinter.messagebox
from tkcalendar import Calendar, DateEntry
from datetime import date
import csv


def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:00 {sec.get()}"
    set_date  = date.get()
    task=f"{notifier.get()}"
    if(set_alarm_timer!="Hour:Minute AM" and task!=""):
        with open('data.csv', 'a', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            filed=[set_date,set_alarm_timer,task]
            writer.writerow(filed)
        tkinter.messagebox.showinfo("Successfull","Notfication Set Successfully")
        #alarm(set_alarm_timer,set_date,task)
        clock.destroy()
        
    else:
        tkinter.messagebox.showwarning("Error","Time and Message Could not be empty")
    



clock = Tk()
clock.title("NOTIFY SETTER")
clock.geometry("350x200")
clock.resizable(0, 0)
clock.eval('tk::PlaceWindow . center')
notifier=StringVar()
icon = PhotoImage(file="appicon.png")
setYourAlarm = Entry(clock,textvariable = notifier ,fg="blue",relief = "solid",width=25,font=("Helevetica",13,"bold"))

# The Variables we require to set the alarm(initialization):
hour= StringVar()
hour.set("Hour")
min= StringVar()
min.set("Minute") 
sec= StringVar()
sec.set("AM")
date = StringVar()


addTime = Label(clock,text = "TIME:",font=("Helevetica",13,"bold"))
addDate = Label(clock,text = "DATE:",font=("Helevetica",13,"bold"))
message = Label(clock,text = "MESSAGE:",font=("Helevetica",13,"bold"))
hr= OptionMenu(clock,hour,"01","02","03","04","05","06","07","08","09","10","11","12") 
mi=OptionMenu(clock,min,"00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59")  
sd=OptionMenu(clock,sec,"AM","PM")
cal = DateEntry(clock,textvariable = date,width= 8, background= "magenta3", foreground= "white",bd=2,font=("Helevetica",13,"bold"))


addDate.place(relx=0,rely=0)
addTime.grid(row = 1, column = 0, sticky = W, pady = 3)
cal.grid(row = 0, column = 1, sticky = W, pady = 3)
#hr.grid(row = 1, column = 1)  
hr.place(relx=0.26, rely=0.16)
#mi.grid(row = 1, column = 2)   
mi.place(relx=0.46, rely=0.16)
#sd.grid(row = 1, column = )   
sd.place(relx=0.69, rely=0.16)
message.grid(row = 2, column = 0, sticky = W, pady = 3)
setYourAlarm.grid(row = 2, column = 1, sticky = W, pady = 3)


#To take the time input by user:
submit = Button(clock,text = "Set Notify",fg="red",width = 10,command = actual_time)
submit.place(relx=0.5, rely=0.6, anchor=CENTER)


clock.mainloop()
#Execution of the window.
