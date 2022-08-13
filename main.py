from scrape_condition import conditions
from scrape_forecast import forecast

URL = 'https://weather.com/en-PH/weather/today/l/9649a410203fa0d4c1082bc29eb8ab42e886f153fc186ac35b3e440253c85fea'

weather_condition = conditions(URL)
weather_forecast = forecast(URL)

today_strs = ("Morning", "Afternoon", "Evening", "Overnight")
hour_objs = []
today_objs = []
day_objs = []

try:
    from forecast_class.today_forecast import Today_Forecast
    from forecast_class.day_forecast import Day_Forecast
    from forecast_class.hour_forecast import Hour_Forecast

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

for day in day_objs:
    print(day.info())