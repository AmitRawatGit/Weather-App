from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import  messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
 
root = Tk()
root.title("Weather App")
root.geometry("800x500+300+200")
root.resizable(False, False)

def getWeather():
    try:
        city = textField.get()
        geolocator = Nominatim(user_agent='geoapiExercise')
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime('%I:%M %p')
        clock.config(text=current_time)
        name.config(text='CURRENT WEATHER')
        # weather
        api = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=71409463205a7aaa6efd80d31f9bfe17'
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        t.config(text=(temp, "°"))
        c.config(text=(condition, '|', 'FEELS', 'LIKE', temp, '°'))
        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)
    except Exception as e:
        messagebox.showerror('Weather App','Invalid Entry !!')

# Search box
search_image = PhotoImage(file="Weather App\images\search_box.png")
myImage = Label(image=search_image)
myImage.place(x=20, y=20)
# textField
textField = tk.Entry(root, justify='center', width=17, font=('poppins', 25, 'bold'), bg='#404040', border=0, fg='white')
textField.place(x=50, y=40)
textField.focus()
# search icon
search_icon = PhotoImage(file="Weather App\images\search_icon.png")
myImageIcon = Button(image=search_icon, borderwidth=0, cursor='hand2', bg='#404040', command=getWeather)
myImageIcon.place(x=400, y=34)
# logo
logo_image = PhotoImage(file='Weather App\images\logo.png')
logo = Label(image=logo_image)
logo.place(x=150, y=100)
# botton box
frame_image = PhotoImage(file=r"Weather App\images\box.png")
frame = Label(image=frame_image)
frame.pack(padx=5, pady=5, side=BOTTOM)
# time
name = Label(root, font=('arial', 15, 'bold'))
name.place(x=30, y=100)
clock = Label(root, font=('Helvetica', 20))
clock.place(x=30, y=130)
# labels
label1 = Label(root, text='WIND', font=('Helvetica', 15, 'bold'), fg='white', bg='#1ab5ef')
label1.place(x=120, y=400)
label2 = Label(root, text='HUMIDITY', font=('Helvetica', 15, 'bold'), fg='white', bg='#1ab5ef')
label2.place(x=250, y=400)
label3 = Label(root, text='DESCRIPTION', font=('Helvetica', 15, 'bold'), fg='white', bg='#1ab5ef')
label3.place(x=430, y=400)
label4 = Label(root, text='PRESSURE', font=('Helvetica', 15, 'bold'), fg='white', bg='#1ab5ef')
label4.place(x=650, y=400)

t = Label(font=('arial', 70, 'bold'), fg='#ee666d') # t stands for temprature
t.place(x=400, y=150)

c = Label(font=('arial', 15, 'bold')) # c stands for condition
c.place(x=400, y=250)

w = Label(text='...', font=('arial', 20, 'bold'), bg='#1ab5ef') # w stands for wind
w.place(x=120, y=430)
h = Label(text='...', font=('arial', 20, 'bold'), bg='#1ab5ef') # h stands for humidity
h.place(x=250, y=430)
d = Label(text='...', font=('arial', 20, 'bold'), bg='#1ab5ef') # d stands for description
d.place(x=430, y=430)
p = Label(text='...', font=('arial', 20, 'bold'), bg='#1ab5ef') # p stands for pressure
p.place(x=650, y=430)


root.mainloop()