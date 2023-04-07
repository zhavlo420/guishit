import tkinter as tk
from tkcalendar import *
from tkinter import *
import webbrowser
from PIL import ImageTk, Image  
from random import randint


root=tk.Tk()
root.geometry("500x420")
root.resizable(True,True)
root.iconbitmap("stolf.ico")
root.title("MORTGAGE")


def pay():
    if amounten.get() and inten.get() and perien.get():
        years=int(perien.get())
        months=years*12
        rate=float(inten.get())
        loan=int(amounten.get())
        
        
        monthly_rate = rate / 100 / 12 
        pay = (monthly_rate / (1 - (1 + monthly_rate)**(-months))) * loan
        pay= f"{pay:,.2f}"
        pay_label.config(text=f"Monthly Payment: ${pay}")

    else:
        pay_label.config(text="BLANK")
    
    
    

labelframe=LabelFrame(root,text="Mortgage Calc")
labelframe.pack(pady=30)
frame=Frame(labelframe)
frame.pack(pady=20)

#lab and entry boxes
amount=Label(frame,text="loan amount")
amounten=Entry(frame,font=("arial",20))

inte=Label(frame,text="interest rate")
inten=Entry(frame,font=("arial",20))


peri=Label(frame,text="period(years)")
perien=Entry(frame,font=("arial",20))

#matrix
amount.grid(row=0,column=0)
amounten.grid(row=0,column=1)

inte.grid(row=1,column=0)
inten.grid(row=1,column=1,pady=20)

peri.grid(row=2,column=0)
perien.grid(row=2,column=1)

butn=Button(labelframe,text="calculate",command=pay)
butn.pack(pady=20)

pay_label=Label(root,text="",font=("arial",20))
pay_label.pack(pady=20)

root.mainloop()