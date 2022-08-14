from tkinter import *
from tkinter import ttk

from src.forecasting.scrape_condition import conditions
from src.forecasting.scrape_forecast import forecast

URL = 'https://weather.com/en-PH/weather/today/l/9649a410203fa0d4c1082bc29eb8ab42e886f153fc186ac35b3e440253c85fea'

# Scrape what we want
weather_condition = conditions(URL)
weather_forecast = forecast(URL)

# The list contains keyword that today's forecast will use.
# The hour forecast can be classified since the website use military time.
# The three forecasts can then be classified easily.
today_strs = ("Morning", "Afternoon", "Evening", "Overnight")
hour_objs = []
today_objs = []
day_objs = []

try:
    from src.forecasting.forecast_class import Forecast
except ImportError:
    print('Import error in forecast class organizations')
else:
    for forecast in weather_forecast:
        time = forecast['time']
        temp = forecast['temp']
        chance = forecast['chance']

        # Create different classes for each types
        if isinstance(time, int) or time == 'Now':
            inst = Forecast(time, temp, chance)
            hour_objs.append(inst)
        elif time in today_strs:
            inst = Forecast(time, temp, chance)
            today_objs.append(inst)
        else:
            inst = Forecast(time, temp, chance)
            day_objs.append(inst)

gui = Tk()
gui.geometry("1000x600")
gui.title("Ummbela")
try:
    from src.gui_frames.condition_frame import Condition_Frm
    from src.gui_frames.forecasts_frame import Forecast_Frm
except ImportError:
    print("Import error in frames.")
else:
    window_frm = ttk.Frame(gui)
    window_frm.pack()

    condition_frm = Condition_Frm(window_frm, weather_condition)
    condition_frm.setup()
    condition_frm.pack()

    today_frm = Forecast_Frm(window_frm, today_objs)
    today_frm.setup()
    today_frm.pack()

    hour_frm = Forecast_Frm(window_frm, hour_objs)
    hour_frm.pack()
    hour_frm.setup()

    day_frm = Forecast_Frm(window_frm, day_objs)
    day_frm.pack()
    day_frm.setup()

gui.mainloop()
