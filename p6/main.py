from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title("Weather App")
root.geometry("800x400+200+100")
root.resizable(False , False)
def getWeather():
    try:
        city = text_field.get()
        
        geolocator = Nominatim(user_agent = "geoapiEercise")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng = location.longitude, lat = location.latitude)
        print(result)
        
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text = current_time)
        name.config(text = "CURRENT WEATHER")
        # api = "https://api.openweathermap.org/data/2.5/weather?id="+city+"&appid=ad1767b223e7954d2b9679ae9419bc6b"
        api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=ad1767b223e7954d2b9679ae9419bc6b"
        json_data = requests.get(api).json()
        t.config(text = str(json_data['main']['temp'] - 273.15))
        c.config(text = json_data['weather'][0]['main'])
        w.config(text = json_data['wind']['speed'])
        h.config(text = json_data['main']['humidity'])
        d.config(text = json_data['weather'][0]['description'])
        p.config(text = json_data['main']['pressure'])
    except Exception as e:
        messagebox.showerror('Weather App','Invaild Entry!!')
        
# except Exception as e:
#     messagebox.showerror("weather App", 'Invalid Entry')
image_search = PhotoImage(file = 'try_project\p6\search_bar.png')
searchbar_image = Label(image = image_search)
text_field = tk.Entry(root, justify= CENTER, width= 17, font = ("poppins", 18, 'bold'),bg ="#eeeeee", fg="black"  )
text_field.place(x =20,y= 20)
text_field.focus()


image_search_icon = PhotoImage(file = 'try_project\p6\search_icon.png')
search_icon = Button(image=image_search_icon, borderwidth=0, cursor= 'hand2', bg = "#147886", command=getWeather)
search_icon.place(x = 250, y = 18)

image_logo = PhotoImage(file="try_project\p6\weather_logo.png")
weather_logo = Label(image=image_logo)
weather_logo.place(x = 250, y = 90)

image_box = PhotoImage(file="try_project\p6\information_box.png")
information_box = Label(image=image_box)
information_box.pack(padx= 5, pady= 5, side = BOTTOM)

name = Label(root,font = ("arial", 15, "bold"))
name.place(x = 30, y = 100)
clock = Label(root, font= ("Merriweather",20))
clock.place(x=30, y=130)

label1 = Label(root, text="WIND", font= ("Merriweather",15, 'bold'), fg = 'white', bg = '#5AC909')
label1.place(x = 100,y = 330)

label2 = Label(root, text='HUMIDITY', font=('Merriweather', 15, 'bold'), fg = 'white', bg = "#5AC909")
label2.place(x = 210, y = 330)

label3 = Label(root, text = 'DESCRIPTION', font = ('Merriweather', 15, 'bold'),fg = 'white',bg = '#5AC909')
label3.place(x = 360, y = 330)

label4 = Label(root, text = 'PRESSURE', font = ('Merriweather', 15, 'bold'), fg = 'white', bg = '#5AC909')
label4.place(x = 570, y = 330)

t = Label(font=('arial', 50, 'bold'), bg = '#5AC909')
t.place(x = 400, y =150) 

c = Label(font=('arial', 20, 'bold'))
c.place(x = 400, y =150) 

w = Label(text= "....", font=('arial', 16, 'bold'), bg = '#5AC909')
w.place(x = 110, y = 360)

h = Label(text= "....", font=('arial', 16, 'bold'), bg = '#5AC909')
h.place(x = 230, y = 360)

d = Label(text= "....", font=('arial', 16, 'bold'), bg = '#5AC909')
d.place(x = 370, y = 360)

p = Label(text= "....", font=('arial', 16, 'bold'), bg = '#5AC909')
p.place(x = 590, y = 360)

root.mainloop()

        
        