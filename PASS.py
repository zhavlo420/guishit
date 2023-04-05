import tkinter as tk
from tkcalendar import *
from tkinter import *
import webbrowser
from PIL import ImageTk, Image  
from random import randint


root=tk.Tk()
root.geometry("500x500")
root.resizable(True,True)
root.iconbitmap("stolf.ico")
root.title("STREAMDECK")

passw=chr(randint(33,125))

def getpass():
    pass_entry.delete(0,END)
    
passlen=int(passentry.get())
my_pass=''

for x in range(passlen):
    my_pass+=chr(randint(33,125))
pass_entry.insert(0,my_pass)
    

    

l1=LabelFrame(root,text="how many char")
l1.pack(pady=20)

passentry=Entry(l1,font=("arial",20))
passentry.pack(pady=20,padx=20)

pass_entry=Entry(root,text='',font=("arial",22))
pass_entry.pack(pady=20)

frame=Frame(root)
frame.pack(pady=20)



b1=Button(frame,text="GENERATE PASS",command=getpass)
b1.grid(row=0,column=0,padx=10)

b2=Button(frame,text="C2C",command=copy)
b2.grid(row=0,column=1,padx=10)