import tkinter as tk
from tkcalendar import *
from tkinter import *

root=tk.Tk()
root.geometry("500x500")
root.resizable(True,True)
root.iconbitmap("stolf.ico")
root.title("GET DATE")

cal=Calendar(root,selectmode="day",year=2023,month=4,day=4)
cal.pack(pady=20,fill="both",expand=True)
  
def date():
    label.config(text=cal.get_date())


button=Button(root,text="GET DATE",command=date)
button.pack(pady=20)

label=Label(root,text="")
label.pack(pady=20)

root.mainloop()