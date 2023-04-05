import tkinter as tk
from tkinter import *
import time
import requests
import json
from PIL import Image,ImageTk

r=Tk()
r.title("TO-DO-LIST")
r.geometry("400x600+400+100")
r.resizable(False,False)


tasklist=[]

def addtask():
    task=task_input.get()
    listbox.insert(END,task)
            
def deltask():
    listbox.delete(ANCHOR)
    
    
def func1():
   
    try:
        with open("todo.txt","r") as taskfile:
            tasks=taskfile.readlines()

        for task in tasks:
            if task !='\n':
                task_list.append(task)
                listbox.insert(END,task)
    except:
        file=open('todo.txt','w')
        file.close()
    

img = ImageTk.PhotoImage(Image.open("topbar.png"))
l1 = Label(r, image = img)
l1.pack()

#noteimg=ImageTk.PhotoImage(Image.open("task.png"))
#l2 = Label(r, image = noteimg)
#l2.place(anchor=NW)
#l2.pack()

heading=Label(r,text="TASK LIST",font="arial 15 bold",fg="white",bg="#C1CDCD")
heading.place(x=145,y=15)

frame=Frame(r,width=400,height=60,bg="white")
frame.place(x=0,y=180)

task=StringVar()
task_input=Entry(frame,width=15,font="arial 18",bd=0)
task_input.place(x=10,y=5)
task_input.focus()

button=Button(frame,text="ADD",font="arial 8 bold",width=10,height=4,bg="#66CDAA",fg="#fff",command=addtask)
button.place(x=310,y=0)

#box 
frame2=Frame(r,bd=3,width=810,height=280,bg="#DCDCDC")
frame2.pack(pady=(140,0))
listbox=Listbox(frame2,font=('arial',10),width=400,height=17,bg="#32405b",fg="white",cursor="hand2",selectbackground="#5a95ff")
listbox.pack(side=LEFT,fill=BOTH,padx=2)
scrollbar=Scrollbar(frame2)
scrollbar.pack(side=RIGHT,fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

del_icon = ImageTk.PhotoImage(Image.open("delete.png"))
Button(r,image=del_icon,bd=0,command=deltask).pack(side=BOTTOM,pady=13)


r.mainloop()