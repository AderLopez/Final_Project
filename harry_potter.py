import urllib. request
import json
import random

#function to get the information from the API of Harry potter:
def information():
    try:
        url= 'https://hp-api.herokuapp.com/api/characters'
        request= urllib. request.urlopen( url)
        result = json. loads(request. read( ))
        char = random.randint(1,40)
        print(char)
        character = result[char]

        #Analyzing if the character is a wizard or not:
        if result[char]['wizard']==True:
            print(result[char]["image"])
            return f"{result[char]["name"]} is in the house of Wizards and the name of the actor is: {result[char]["actor"]} and the image of the character is {result[char]["image"]}"

        else:
            print(result[char]["image"])
            return f"{result[char]["name"]} is not in the house of Wizard and the name of the actor is: {result[char]["actor"]} and the image of the character is {result[char]["image"]}"
    except:
        return

#Additional function to get a picture with the user input a number.
def get_random_picture(number):
    try:
        if number>=1 and number<=40:
            url= 'https://hp-api.herokuapp.com/api/characters'
            request= urllib. request.urlopen( url)
            result = json. loads(request. read( ))
            char = random.randint(1,40)
            character = result[char]
            return result[char]["image"]
        else:
            return "No valid Number"
    except:
        return