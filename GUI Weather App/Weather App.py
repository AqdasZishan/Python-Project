import tkinter as tk
import requests
from PIL import Image, ImageTk

root = tk.Tk()

HEIGHT = 500
WIDTH = 600

def format_responses(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        country = weather['sys']['country']
        feels = weather['main']['feels_like']
        min_t = weather['main']['temp_min']
        max_t = weather['main']['temp_max']
        
        desc = desc.capitalize()

        final_str = 'City: %s \nCountry: %s \nConditions: %s \nTemperature(°C): %s   Feels Like(°C): %s \nMin Temp(°C): %s    Max Temp(°C): %s' % (name, country, desc, temp, feels, min_t, max_t)
        
    except:
        final_str = 'ERROR: Unable to find the city'
        
    return final_str

def get_weather(city):
    weather_key = 'edffd1bf975a74d5d10e58c5ac8be2d3'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID':weather_key, 'q':city, 'units':'metric'}
    response = requests.get(url, params=params)
    #print(response.json())
    weather = response.json()

    label['text'] = format_responses(response.json())

    icon_name = weather['weather'][0]['icon']
    open_image(icon_name)
    
def open_image(icon):
    size = int(lower_frame.winfo_height()*0.25)
    img = ImageTk.PhotoImage(Image.open('./img/'+icon+'.png').resize((size, size)))
    weather_icon.delete("all")
    weather_icon.create_image(0,0, anchor='nw', image=img)
    weather_icon.image = img

C = tk.Canvas(root, height=HEIGHT, width=WIDTH)
background_image= tk.PhotoImage(file='./landscape_real.png')
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

C.pack()                          
                            
frame = tk.Frame(root, bg='#42c2f4', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=(' ', 15))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=40, command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#42c2f4', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

bg_color = 'white'
label = tk.Label(lower_frame) 
label.config(font=(' ',15), bg=bg_color)
label.place(relwidth=1, relheight=1)

weather_icon = tk.Canvas(label, bg=bg_color, bd=0, highlightthickness=0)
weather_icon.place(relx=.78, rely=0, relwidth=1, relheight=0.5)

root.iconbitmap('sun_icon.ico')
root.title("Weather App")

root.minsize(width=WIDTH ,height=HEIGHT)
root.maxsize(width=WIDTH ,height=HEIGHT)

root.mainloop()
