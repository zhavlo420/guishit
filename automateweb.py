import tkinter as tk
from tkcalendar import *
from tkinter import *
import webbrowser
from PIL import ImageTk, Image  

root=tk.Tk()
root.geometry("500x500")
root.resizable(True,True)
root.iconbitmap("stolf.ico")
root.title("STREAMDECK")

def open():
    webbrowser.open_new("https://www.youtube.com/@zhavlo")

def open2():
    webbrowser.open_new("https://www.twitch.tv/zyloislive")
    
 
img= PhotoImage(file="yt.png")
#resized_image= img.resize((50,50), Image.ANTIALIAS)
button=Button(root,image=img,command=open)

button.pack(anchor=CENTER)


img2= PhotoImage(file="twitch.png")
button2=Button(root,image=img2,command=open2)
button2.pack(anchor=CENTER)

root.mainloop()

