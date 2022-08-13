from cgitb import text
from tkinter import *
from tkinter import ttk

from src.forecast_class.scrape_condition import conditions
from src.forecast_class.scrape_forecast import forecast

URL = 'https://weather.com/en-PH/weather/today/l/9649a410203fa0d4c1082bc29eb8ab42e886f153fc186ac35b3e440253c85fea'

weather_condition = conditions(URL)
weather_forecast = forecast(URL)

today_strs = ("Morning", "Afternoon", "Evening", "Overnight")
hour_objs = []
today_objs = []
day_objs = []

try:
    from src.forecast_class.today_forecast import Today_Forecast
    from src.forecast_class.day_forecast import Day_Forecast
    from src.forecast_class.hour_forecast import Hour_Forecast

    for forecast in weather_forecast:
        time = forecast['time']
        temp = forecast['temp']
        chance = forecast['chance']

        if isinstance(time, int) or time == 'Now':
            inst = Hour_Forecast(time, temp, chance)
            hour_objs.append(inst)
        elif time in today_strs:
            inst = Today_Forecast(time, temp, chance)
            today_objs.append(inst)
        else:
            inst = Day_Forecast(time, temp, chance)
            day_objs.append(inst)
except ImportError:
    print('Import Error')

gui = Tk()
gui.geometry("1000x600")
condition_frm = ttk.Frame(gui, padding=10)
condition_frm.pack()

for i in range(len(weather_condition)):
    label = ttk.Label(condition_frm, text=str(weather_condition[i])).pack()

today_frm = ttk.Frame(gui, padding=10)
today_frm.pack()
for i in range(len(today_objs)):
    cur_frm = ttk.Frame(today_frm, width=100, height=100, padding=15)
    ttk.Label(cur_frm, text=today_objs[i].info()["time"]).pack()
    ttk.Label(cur_frm, text=today_objs[i].info()["temp"]).pack()
    ttk.Label(cur_frm, text=today_objs[i].info()["chance"]).pack()
    cur_frm.pack(side=LEFT)

hour_frm = ttk.Frame(gui, padding=10)
hour_frm.pack()
for i in range(len(hour_objs)):
    cur_frm = ttk.Frame(hour_frm, width=100, height=100, padding=15)
    ttk.Label(cur_frm, text=hour_objs[i].info()["time"]).pack()
    ttk.Label(cur_frm, text=hour_objs[i].info()["temp"]).pack()
    ttk.Label(cur_frm, text=hour_objs[i].info()["chance"]).pack()
    cur_frm.pack(side=LEFT)

day_frm = ttk.Frame(gui, padding=10)
day_frm.pack()
for i in range(len(day_objs)):
    cur_frm = ttk.Frame(day_frm, width=100, height=100, padding=15)
    ttk.Label(cur_frm, text=day_objs[i].info()["time"]).pack()
    ttk.Label(cur_frm, text=day_objs[i].info()["temp"]).pack()
    ttk.Label(cur_frm, text=day_objs[i].info()["chance"]).pack()
    cur_frm.pack(side=LEFT)
    
gui.mainloop()
