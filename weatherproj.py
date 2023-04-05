import tkinter as tk
from tkinter import *
import time
import requests
import json
from PIL import Image,ImageTk

def getweat(canvas):
    city=textfd.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=254be576ac101209a848fbc02a7ee70a"
    #254be576ac101209a848fbc02a7ee70a
    json_dat=requests.get(api).json()
    
    temp=int(json_dat['main']['temp']-273.15)#in k
    max_temp=int(json_dat['main']['temp_max']-273.15)
    min_temp=int(json_dat['main']['temp_min']-273.15)
    hum=json_dat['main']['humidity']

    final_in= "\n" + str(temp) + "°C" 
    fin_dat="\n" + "MAXIMUM TEMP:" +" " + str(max_temp) + "\n" + "MINIMUM TEMP:" +" " + str(min_temp) + "\n" +"Humidity:" +" " +str(hum)
    l1.config(text=final_in)
    l2.config(text=fin_dat)
    


canvas=tk.Tk()
canvas.geometry("300x300")
canvas.title("WEATHER")
#canvas.configure(bg="#B0C4DE")


t=("Arial",15,"bold")
f=("Arial",15,"bold")

textfd=tk.Entry(canvas,font =t)
textfd.pack(pady=20)
textfd.focus()
textfd.bind('<Return>',getweat)

l1=tk.Label(canvas,font =t)
l1.pack()
l2=tk.Label(canvas,font =f)
l2.pack()

image = Image.open("2275.png")
 

resize_image = image.resize((100, 100))
 
img = ImageTk.PhotoImage(resize_image)
 
# create label and add resize image
label1 = Label(image=img)
label1.image = img
label1.pack()

exit_button = Button(canvas, text="Exit", command=canvas.destroy)
exit_button.pack(pady=5)
canvas.mainloop()
