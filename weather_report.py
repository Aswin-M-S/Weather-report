import requests
import time
import datetime as dt
curr_time = dt.datetime.now().hour

if curr_time < 12:
    wish = "Good morning"
elif (curr_time >= 12 and curr_time <=15):
    wish = "Good afternoon"
else:
    wish = "Good evening"


user = input("Enter your name")
print("Hello...  "+user+".."+wish)
print("")

city = input("Enter a city name to check current weather")

api_key = "8080d4edf5fb25a4c25cb09173c79229"

api_link = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key

r = requests.get(api_link)

city_weather_report = r.json()


# to get temperature of the given city
temp = int((city_weather_report['main']['temp']) - 273.15)
# to get the real feel temperature of the location
real_feel_temp = int((city_weather_report['main']['feels_like']) - 273.15)
# to get maximum temperature of the given city
max_temp = int((city_weather_report['main']['temp_max']) - 273.15)
# to get minimum temperature of the given city
min_temp = int((city_weather_report['main']['temp_min']) - 273.15)


# to get the current pressure in bars
curr_pressure = ((city_weather_report['main']['pressure'])/1000)
# to get the humidity
curr_humidity = (city_weather_report['main']['humidity'])
# to get the visibility
visibility = ((city_weather_report['visibility'])/1000)


# to get the windspeed in km/hr
wind_speed = (city_weather_report['wind']['speed'])


# to get the cloud
cloud = (city_weather_report['weather'][0]['description'])

#to get the coordinates of the given location
longitute = (city_weather_report['coord']['lon'])

latitude = (city_weather_report['coord']['lat'])



print("Fetching todays current weather report....")
time.sleep(3)
print(" ")
print(f'Geographical location of {city} is {longitute}° longitude and {latitude}° latitude.')
time.sleep(1)
print(" ")
print("Today you can expect "+cloud+".")
time.sleep(1)
print(f'The current temperature is {temp}°C, but feels like {real_feel_temp}°C, Minimum observed temperature is {min_temp}°C and Maximum observed temperature is {max_temp}°C.')
time.sleep(1.5)
if real_feel_temp >= 30:
    print("Its gonna be a hot day.....Keep your doors and windows open")
else:
    print("Today is cooler than ususal.")
print(" ")
time.sleep(1)
print(f"Current humidity {curr_humidity}%")
if curr_humidity > 50:
    print("You are gonna feel humid and hot")
elif curr_humidity == 45:
    print("You will experience ideal humidity")
elif curr_humidity < 30:
    print("Low Humidity")
print("")
time.sleep(1)
print(f"Visibility {visibility}Km")
print(f"Current pressure {curr_pressure}bar")
print(" ")
time.sleep(1)
print(f"Wind Speed {wind_speed}Km/hr")