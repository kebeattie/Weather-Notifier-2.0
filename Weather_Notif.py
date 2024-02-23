import requests
import re
from bs4 import BeautifulSoup
from win10toast import ToastNotifier



n = ToastNotifier()

def getweather(url):
    r = requests.get(url)
    return r.text

htmldata = getweather("https://www.metoffice.gov.uk/weather/forecast/gcmzggpxq#?date=2024-03-25")

soup = BeautifulSoup (htmldata, 'html.parser')

#print (soup.prettify())

high_temp = str(soup.find("span", class_="tab-temp-high"))

low_temp = str(soup.find("span", class_="tab-temp-low"))

max_temp = re.findall("[0-9]+", high_temp)

min_temp = re.findall("[0-9]+", low_temp)


result = "High temp = " + max_temp[0] + "°C" + " Low temp = " + min_temp[0] + "°C" + " in Liverpool"

n.show_toast("Live Weather Update", result, duration = 10)