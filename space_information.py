import urllib. request
import json
import random

def space_people_number():
    try:
        url= 'http://api.open-notify.org/astros.json'
        request= urllib. request.urlopen( url)
        result = json. loads(request. read( ))
        number = result['number']
        #print(f"The number of people in the space is:{result['number']} ")
        return number   
    except:
        return