import requests
from bs4 import BeautifulSoup as bs
 
def forecast(URL):
    req = requests.get(URL)
    soup = bs(req.text, 'html.parser')

    forecasts = soup.find_all('li', attrs={'Column--column--1p659'})
    for i in range(len(forecasts)):
        timeFrame = forecasts[i].find('span', attrs={'class', 'Ellipsis--ellipsis--1sNTm'}).text
        tempValue = forecasts[i].find('div', attrs={'class', 'Column--temp--5hqI_'}).text

        chanceOfRain = forecasts[i].find('span', attrs={'class', 'Column--precip--2ck8J'}).text
        formatChanceOfRain =  chanceOfRain.replace("Rain", "Rain ")

        timeFrame = timeFrame.replace(":", "")
        try:
            timeFrame = int(timeFrame)
        except ValueError:
            pass


        forecasts[i] = {
            'time': timeFrame,
            'temp': tempValue,
            'chance': formatChanceOfRain
        }
    
    return forecasts