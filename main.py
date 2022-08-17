from curses import window
from tkinter import *
from tkinter import ttk

from src.forecasting.scrape_condition import conditions
from src.forecasting.scrape_forecast import forecast
from src.url_class import URL_CLASS
from src.forecasting.forecast_class import Forecast_Class

from src.gui_frames.condition_frame import Condition_Frm
from src.gui_frames.forecasts_frame import Forecast_Frm

def main():
    URLS = URL_CLASS()

    # default url is manila
    current_url = URLS.manila

    gui = Tk()
    gui.geometry("1000x600")
    gui.title("Ummbela")

    # The list contains keyword that today's forecast will use.
    # The hour forecast can be classified since the website use military time.
    # The three forecasts can then be classified easily.
    today_strs = ("Morning", "Afternoon", "Evening", "Overnight")
    weather_conditions = []
    hour_objs = []
    today_objs = []
    day_objs = []

    def refetch(url = URLS.manila):
        nonlocal hour_objs, today_objs, day_objs, weather_conditions
        # Scrape whatever we need
        weather_conditions = conditions(url)
        weather_forecast = forecast(url)

        # makes sure these lists are empty
        hour_objs = []
        today_objs = []
        day_objs = []

        for fc in weather_forecast:
            time = fc['time']
            temp = fc['temp']
            chance = fc['chance']

            # Create different classes for each types
            if isinstance(time, int) or time == 'Now':
                inst = Forecast_Class(time, temp, chance)
                hour_objs.append(inst)
            elif time in today_strs:
                inst = Forecast_Class(time, temp, chance)
                today_objs.append(inst)
            else:
                inst = Forecast_Class(time, temp, chance)
                day_objs.append(inst)

    def infoFrame():
        nonlocal gui

        window_frm = ttk.Frame(gui)
        window_frm.pack()

        condition_frm = Condition_Frm(window_frm, weather_conditions)
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

        return window_frm

    refetch()
    window_frame = infoFrame()
    window_frame.pack()

    options = [
        "",
        "Manila",
        "Makati",
        "Marikina",
        "Quezon"
    ]

    def changeCity(*args):
        city = clicked.get()

        if city == "Manila":
            refresh(url=URLS.manila)
        elif city == "Marikina":
            refresh(url=URLS.marikina)
        elif city == "Makati":
            refresh(url=URLS.makati)
        elif city == "Quezon":
            refresh(url=URLS.quezon)

    def refresh(url = current_url):
        nonlocal window_frame
        window_frame.destroy()
        current_url = url

        refetch(url)
        window_frame = infoFrame()
        window_frame.pack()

    access = ttk.Frame(gui, padding=10)
    access.place(x=450, y=450)

    clicked = StringVar()
    clicked.set("Manila")

    drop = ttk.OptionMenu(access, clicked, *options, command=changeCity)
    drop.pack()

    change_btn = ttk.Button(access, command=refresh, text="refresh")
    change_btn.pack()

    gui.mainloop()


if __name__ == "__main__":
    main()

