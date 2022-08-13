import requests
from bs4 import BeautifulSoup as bs
 
def conditions(URL):
    req = requests.get(URL)
    soup = bs(req.text, 'html.parser')

    dateAndTime = soup.find('div', attrs={'CurrentConditions--header--27uOE'}).text
    currentTemp = soup.find('span', attrs={'class', 'CurrentConditions--tempValue--3a50n'}).text
    currentCondition = soup.find('div', attrs={'class', 'CurrentConditions--phraseValue--2Z18W'}).text
    
    return [
        dateAndTime,
        currentTemp,
        currentCondition,
    ]


        
