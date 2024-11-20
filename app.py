#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask,render_template, request
app = Flask(__name__)


#Import libraries for Assignment 3
import urllib.request
import json
from get_weather import get_weathers
import nba


#Normal path when not using a specific folder:
#@app.route("/")
#def hello():
#    return app.send_static_file("index.html")

#Line of code necessary to change the Path of the templates of HTML since coding in Visual Studio
app = Flask(__name__, template_folder='templates') 


#Calling the index.html that will be the home page.
@app.route('/',methods=['POST','GET'])
def Index():
    import space_information
    import get_weather
    import harry_potter

    number_people_space =   space_information.space_people_number()
    print(number_people_space)  
    temperature = get_weather.get_city('sudbury')
    print(temperature)
    character = harry_potter.information()
    print(character)



    return render_template("module_7.html")




#Calling the BMI calculator as post and get to calculate values taken from user input:
@app.route('/bmi', methods=['POST','GET'])
def bmi():
    
    #This first method evaluates the input from user and return two messages:
    if request.method == 'POST':
        
        #Import the BMI function to calculate the BMI
        import bmi

        #Values obtain from the user:
        height = request.form.get('height')  
        weight = request.form.get('weight') 

        #BMI function returns two values after given the height and weight
        bmi, message = bmi.bmi_calculator(float(weight), float(height))
        
        #Changing the BMI into a message to show in HMTL:
        bmi = f"Yor BMI is {bmi}"

        #Returning the two messages for the user with the calculation and evaluation of BMI.
        return render_template('bmi.html', bmi = bmi, message = message)
    
    #Normal Get request, when there is no information sent:
    elif request.method == 'GET':
      return render_template("bmi.html")


#Calling the weather webpage
@app.route('/weather')
def weather():
    
    #Importing the weather function from a .py file
    import weather 

    #Using the function I get the description for the day and temperature on celcius.
    description, temperature = weather.printing_weather()

    #Returning the variables to be shown in the Webpage in HTML
    return render_template("weather.html", description = description, temperature = temperature)

#Calling the Dashboard
@app.route('/dashboard', methods=['POST','GET'])
def dashboard():
    #Calling the nba program that gets the information and saves the graphs:
    #Information retrieve about teams:
    teams_number = nba.all_teams()

    #Information retrieve about players:
    players_number, Highest_country_provider,highest_height,tallest_player = nba.players()

    return render_template("dashboard.html", teams_number = teams_number, players_number=players_number,Highest_country_provider=Highest_country_provider,tallest_player=tallest_player,highest_height=highest_height)



