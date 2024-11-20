import urllib. request
import json
import random

def information():
    url= 'https://hp-api.herokuapp.com/api/characters'
    request= urllib. request.urlopen( url)
    result = json. loads(request. read( ))
    #print(f"The number of people in the space is:{result['number']} ")
    char = random.randint(1,40)
    print(char)
    character = result[char]
    return character   