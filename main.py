# pip install bs4
# pip install tkinter
# pip install requests

from bs4 import BeautifulSoup
import requests
from tkinter import *
from tkinter import messagebox
import time


headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
          }


def enter(event=None):
    city = box.get()
    if city:
        weather(city)


def weather(city):
    city += "+weather"
    try:
        res = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8'
                ,headers=headers)
        
        soup = BeautifulSoup(res.text, 'html.parser')

        location = soup.select('#wob_loc')[0].getText().strip().split(',')
        day = soup.select('#wob_dts')[0].getText().strip().split(',')[0]
        current_time = time.ctime().split()[3][:5]
        weather_condition = soup.select('#wob_dc')[0].getText().strip()
        temperature = soup.select('#wob_tm')[0].getText().strip()
        precipitation = soup.select('#wob_pp')[0].getText().strip()
        humidity = soup.select('#wob_hm')[0].getText().strip()
        wind = soup.select('#wob_ws')[0].getText().strip()

        l = (location[0] + " is located in" + " ".join(location[1:]) + '.\n' +
            'Precipitation : ' + precipitation + ', ' + 'Humidity : ' + humidity + ',' + ' Wind : '+ wind +
            "\nToday it's " + day + ', ' + current_time + ' and is ' + weather_condition.lower() + ".\nThe Temperature is " + temperature + '°C.')
        
        messagebox.showinfo(f"{location[0]} info", l)

    except:
        messagebox.showinfo(f"{city} info", ["Something's wrong! please.. try again"])


def h():
    messagebox.showinfo('Help','''
                        1) Enter the city name.
                        2) Press Enter on the keyboard or search button on screen.
                        3) Weather info of the city will be displayed.
                        ''')


def q():
    exit()


master = Tk()
master.title("Weather")
master.geometry("250x92")

Label(master, text='Enter city: ').grid(row=0)

box = Entry(master)
box.grid(row=0, column=1, columnspan=10, sticky=W)

search = Button(master, text="Search", command=enter)
search.grid(row=1, column=4)
master.bind('<Return>',enter)

help = Button(master, text="Help", command=h)
help.grid(row=2, column=0)

quit = Button(master, text='Quit', command=q)
quit.grid(row=2, column=9)

mainloop()
