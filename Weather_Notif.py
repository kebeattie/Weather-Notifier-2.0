import requests
import json
import re
from bs4 import BeautifulSoup
from win10toast import ToastNotifier



n = ToastNotifier()

userInput = input("Enter your location: ")

response_API = requests.get("http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/datatype/6620/xml/3840?res=3hourly&key=60071ca7-b9e5-4686-92bc-4d405064b6ca")

sitelist = requests.get("http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/sitelist?key=60071ca7-b9e5-4686-92bc-4d405064b6ca")

list = sitelist.json()

#for i in list:
   # for j in i:
       # if j == "name":
           #print (x)
            
#print (list)

locations = (list["Locations"] ["Location"])
#print (locations)

name = ([sub["name"] for sub in locations])

#if userInput == name:
    
id = ([sub["name"] for sub in locations])

print (id)

#for i in locations:
    #for j in i:
        #print (j)

print (response_API.status_code)


def getweather(url):
    r = requests.get(url)
    return r.text

htmldata = getweather("https://www.metoffice.gov.uk/weather/forecast/gcmzggpxq#?date=2024-02-23")

soup = BeautifulSoup (htmldata, 'html.parser')


#print (soup.prettify())

high_temp = str(soup.find("span", class_="tab-temp-high"))

low_temp = str(soup.find("span", class_="tab-temp-low"))

max_temp = re.findall("[0-9]+", high_temp)

min_temp = re.findall("[0-9]+", low_temp)


result = "High temp = " + max_temp[0] + "°C" + " Low temp = " + min_temp[0] + "°C" + " in Liverpool"

n.show_toast("Live Weather Update", result, duration = 10)