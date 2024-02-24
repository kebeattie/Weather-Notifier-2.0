import requests
import json
import re
from bs4 import BeautifulSoup
from win10toast import ToastNotifier


n = ToastNotifier()

userInput = input("Enter your location: ")

sitelist = requests.get("http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/sitelist?key=60071ca7-b9e5-4686-92bc-4d405064b6ca") # Retrieves JSON with all Uk location IDs

list = sitelist.json()
       
locations = (list["Locations"] ["Location"])

name = ([sub["name"] for sub in locations]) # Creates list with all location names
  
id = ([sub["id"] for sub in locations]) # Creates list with all location IDs

no = 0 # Counter so that we can match location name with id from two lists

for i in name: # Checks that the user input matches a name in the locations list
    no = no +1 
    if i.upper() == userInput.upper():
        print (i)
        break

locationID = id[no-1] # The counter we created earlier lets us match the location name with id. id is needed to pass into the URL for the API request

response_API = requests.get("https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&appid=2d05883852e6679dea8af8488a408f09") # Requests weather data for user specified location

weatherData = response_API.json()
print (weatherData)


#data = (weatherData["SiteRep"]["DV"]["Location"]["Period"][4]["Rep"]) # Createslist of relevant weather data from JSON

#t = ([sub["T"] for sub in data]) # Extracts all temp values and stores in list

#p = ([sub["Pp"] for sub in data]) # Extracts all precip values and stores in list

#print (response_API.status_code)

#print (t)
#print (p)

#result = "Current Temp = " + t[3] + "°C\n" + "Chance of Rain = " + p[3] + "%" + " in " + userInput # Puts all releveant information into string to be passed into notification

#n.show_toast("Live Weather Update", result, duration = 10) # Sends notification