import urllib. request
import json
import random


url= 'http://api.open-notify.org/astros.json'
request= urllib. request.urlopen( url)
result = json. loads(request. read( ))

print(f"The number of people in the space is:{result['number']} ")

city = 'sudbury'
weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=4389ff17f08ecf9f478e9a96f5da7950"
request = urllib.request.urlopen(weather_url)
result = json.loads(request.read())
print(result['main']['temp'])

#Converting to celsius:
temp = round(result['main']['temp']-273.15,2)
print(temp)

#Getting information from Harry Potter:
urt = 'https://hp-api.herokuapp.com/api/characters'
request = urllib.request.urlopen( url )
result = json.loads( request. read( ))
print( result)
char = random.randint(1,39)

print(char)


