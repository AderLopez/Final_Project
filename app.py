#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask,render_template, request
app = Flask(__name__)


#Import libraries for Assignment
import urllib.request
import json
from get_weather import get_weathers
import nba
from random import randint


#Normal path when not using a specific folder:
#@app.route("/")
#def hello():
#    return app.send_static_file("index.html")

#Line of code necessary to change the Path of the templates of HTML since coding in Visual Studio
app = Flask(__name__, template_folder='templates') 



#Calling the index.html that will be the home page, in this case is set for module 7 assignment:
@app.route('/')
def Index():
    
    return render_template("index.html")

#Calling the experience webpage
@app.route('/projects')
def projects():
    return render_template("projects.html")

#Calling the experience webpage
@app.route('/experience')
def experience():
    return render_template("experience.html")

#Calling the skills webpage
@app.route('/skills')
def skills():
    return render_template("skills.html")

#Calling the education webpage
@app.route('/education')
def education():
    return render_template("education.html")

#Calling the licenses webpage
@app.route('/licenses')
def licenses():
    return render_template("licenses.html")


#Calling module 11 assignment:
@app.route('/module_11',methods=['POST','GET'])
def module_11():
    return render_template("module_11.html")

#Calling module 10 assignment:
@app.route('/module_10',methods=['POST','GET'])
def module_10():
    return render_template("module_10.html")

#Calling module 9 assignment:
@app.route('/module_9',methods=['POST','GET'])
def module_9():
    return render_template("module_9.html")

#Calling module 8 assignment:
@app.route('/module_8',methods=['POST','GET'])
def module_8():
    import requests
    import creating_workbook
    import pandas as pd

    #Getting information to plot from COINCAP:

    if request.method == 'POST':
        url = 'https://api.coincap.io/v2/assets'
        response = requests.get(url)
        #print(response)
        #copying the json information twice to use it differently.

        data = response.json()
        data1 = response.json()
        df= pd.DataFrame(data1['data'])
        mean_price = pd.to_numeric(df['priceUsd']).mean()
        print(mean_price)
        median_price = pd.to_numeric(df['priceUsd']).median()
        print(median_price)
        std_price = pd.to_numeric(df['priceUsd']).std()
        print(std_price)
        data = [{"Coin_Name": item['name'], "Rank": item['rank'],"priceUsd": item['priceUsd']} for item in data['data']]

        creating_workbook.Creating_workbook(data, round(mean_price,1), round(median_price,1), round(std_price,1))
        # for cur in data['data']:
        #     print(cur['name'],cur['symbol'],cur['rank'])
        return render_template("module_8.html",mean = round(mean_price,1),median = round(median_price,1),std = round(std_price,1))

    #Normal Get request, when there is no information sent:
    elif request.method == 'GET':
      return render_template("module_8.html")

#Calling module 7 assignment:
@app.route('/module_7',methods=['POST','GET'])
def module_7():
    import messaging
    import harry_potter

    if request.method == 'POST':

        #Values obtain from the user:
        #Evaluating if the user input a number, to avoid an error:
        if request.form.get('number') == "":
            number = 0
        else:
             number =int(request.form.get('number'))

        #We need a number between 1 and 40 to called a character from Harry potter API:
        if number >=1 and number<=40:
            link = harry_potter.get_random_picture(number)
            if link != "":
                link = link
            else:
                #Image for a scenario that there is no image in the API 
                link = "static/images/No_Image_Available.jpg"  
        else:
            #Image for a scenario where the user didn't input a number:
            link = "static/images/No_Image_Available.jpg"
        
        message = messaging.messaging_process()
        return render_template("module_7.html",number = number, link = link,message=message)

    #Normal Get request, when there is no information sent:
    elif request.method == 'GET':
      #Initial Image to get a better look
      link = "static/images/hogwarts_background.jpg"
      return render_template("module_7.html",link=link)

#Calling module 6 assignment:
@app.route('/module_6', methods=['POST','GET'])
def module_6():
    #Calling the nba program that gets the information and saves the graphs:
    #Information retrieve about teams:
    teams_number = nba.all_teams()

    #Information retrieve about players:
    players_number, Highest_country_provider,highest_height,tallest_player = nba.players()

    return render_template("module_6.html", teams_number = teams_number, players_number=players_number,Highest_country_provider=Highest_country_provider,tallest_player=tallest_player,highest_height=highest_height)

#Calling the index.html that will be the home page.
@app.route('/module_5', methods=['POST','GET'])
def module_5():
    import Crytocurrency
    Crytocurrency.cryptocurrency()

    current_rate_btc,current_rate_jpy, current_date = Crytocurrency.Bitcoin_rate()
    return render_template("module_5.html",Current_date = current_date, Current_rate_BTC = current_rate_btc, Current_rate_JPY = current_rate_jpy )

#Calling the BMI calculator as post and get to calculate values taken from user input:
@app.route('/module_2_bmi', methods=['POST','GET'])
def module_2_bmi():
    
    #This first method evaluates the input from user and return two messages:
    if request.method == 'POST':
        
        #Import the BMI function to calculate the BMI
        import bmi

        #Values obtain from the user:
        height = request.form.get('height')  
        weight = request.form.get('weight') 

        #BMI function returns two values after given the height and weight
        bmi, message = bmi.bmi_calculator(float(weight), float(height))
        
        #Changing the BMI into a message to show in HTML:
        bmi = f"Yor BMI is {bmi}"

        #Returning the two messages for the user with the calculation and evaluation of BMI.
        return render_template('module_2_bmi.html', bmi = bmi, message = message)
    
    #Normal Get request, when there is no information sent:
    elif request.method == 'GET':
      return render_template("module_2_bmi.html")

#Calling the weather webpage
@app.route('/module_2_weather')
def module_2_weather():
    
    #Importing the weather function from a .py file
    import get_weather 

    #Using the function I get the description for the day and temperature on celsius.
    description, temperature = get_weather.printing_weather()

    #Returning the variables to be shown in the Webpage in HTML
    return render_template("module_2_weather.html", description = description, temperature = temperature)

#Assignment 3 new tab:
@app.route('/module_3')
def module_3():
    
    #Importing the libraries necessary:
    from space_information import iss_loc
    from get_weather import get_weathers
    from get_distance import distances
    from get_reverse_geo import address
    from get_country import country

    #Calling Iss_loc to get ISS latitude and longitude
    data = iss_loc()

    #Getting the latitude and longitude from data
    Iss_latitude, Iss_longitude, url_google = data

        #Additional method to obtain the information:
        #latitude, longitude = data[0],data[1]
    
        #Coordinates for Peru for testing:
        #Iss_latitude= -13.2577
        #Iss_longitude= -76.1413
    
    #Printing in the console the coordinates information:
    print(f"The ISS is located in: {Iss_latitude}, {Iss_longitude}")

    #Getting the weather on the ISS location:
    weather = get_weathers(Iss_latitude, Iss_longitude)

    #Weather is the jason variable that has Variables as temperature and description:
    temp_c = round (weather["main"]['temp'])
    description = weather ["weather"][0]["description"]
    #Printing the values in console as checking point:
    print(f'The temperature is: {temp_c}')
    print(f'The description is: {description}')


    #Calling Reverse Geolocation:
    add = address(Iss_latitude,Iss_longitude)

    #Analysis if the ISS is over water to get the flag of the country where it is:
    if(add["countryCode"] == ""):
        print("The ISS is over water")
        ISS_country = "the Ocean"
        flag_dynamic = "static/images/Ocean.jpg"
    else:
        #Location needs to be in lower case:
        location = add["countryCode"].lower()
        #Checkpoint to see the location
        print(f"The country Code is: {location}")
        flag_dynamic = country(location)[0]["flags"]["png"]
        #Checkpoint to see the flag link
        print(f'The link of the flag is the following: {flag_dynamic}')
        ISS_country = country(location)[0]["name"]["common"]
        #Checkpoint to see the country name
        print(f'The name of the country is: {ISS_country}')

    #Additional code to pass the flag of Peru for this code: 
    location = country("pe")
    flag_static = country("pe")[0]["flags"]["png"]


    #Find the distance between Cambrian College us and the ISS(Using Stack Overflow):
    
    #Coordinates found online:
    Sudbury_latitude = 46.5290876
    Sudbury_longitude = -80.9433008

    #Calling the functions to measure the distance between Cambrian and ISS
    distance = distances(Sudbury_latitude, Sudbury_longitude,Iss_latitude, Iss_longitude)
    print(f"The distance between sudbury and ISS is: {distance} in Km")


    return render_template("module_3.html", Latitude = Iss_latitude, Longitude = Iss_longitude, Link = url_google,
                           Temperature = temp_c, Description = description,
                           Country_Name = ISS_country ,Flag_static = flag_static,Flag_dynamic = flag_dynamic,
                           Distance = distance )








#Creating the server on port 8080
app.run(host='0.0.0.0', port = 8080)
