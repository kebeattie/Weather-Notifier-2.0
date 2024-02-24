import requests
import json
from win10toast import ToastNotifier

n = ToastNotifier()
lat = None
lon = None

while (lat == None or lon == None):
    userInput = input("Enter your location: ")

    sitelist = requests.get("http://api.openweathermap.org/geo/1.0/direct?q=" + userInput.title() + "&limit=1&limit=1&appid=2d05883852e6679dea8af8488a408f09") # Retrieves JSON site lat and lon

    list = sitelist.json() # Puts data from API call into json object
    
    try:
        lat = str((list[0]["lat"]))
        lon = str((list[0]["lon"])) #extracts lat and lon from json. To be passed into next API call
    except:
        print ("\nLocation not found\n")
       
response_API = requests.get("https://api.openweathermap.org/data/3.0/onecall?lat=" + lat +"&lon=" + lon +"&units=metric&exclude=minutely,hourly,daily,alerts&appid=2d05883852e6679dea8af8488a408f09") # Requests weather data for user specified location

weatherData = response_API.json() # Puts data from API call into json object

currentTemp = (weatherData["current"]["temp"]) # Extracts current temp from json
print (currentTemp)

condition = (weatherData["current"]["weather"][0]["description"]) # Extracts current condtion from json
print (condition)


result = "Current Temp = " + str(currentTemp) + "°C\n" + "Condition = " + condition.title() # Puts all releveant information into string to be passed into notification

n.show_toast(userInput.title() + " Current Weather", result, duration = 10) # Sends notification