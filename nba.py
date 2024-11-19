import requests
import pandas as pd
import graph_matplot
import graphs_pygal

def check_team(team_id):

    #using Fast API and Key to obtain the Information: 
    api_url = f"https://api.balldontlie.io/v1/teams/{team_id}"
    api_key = "e3a45507-3c34-4985-a209-d19601d50d54" # enter your api key
    headers = {"Authorization": f"{api_key}"}
    response = requests.get(api_url, headers=headers)
    print(response.status_code)

    # List to store the responses
    team_list = []

    #If the authorization is successful we send the information:
    if response.status_code == 200:
        team_list.append(response.json())

    # Use the key information of the list
    team_name = team_list[0]["data"]["name"]
    team_city = team_list[0]["data"]["city"]
    team_abbreviation = team_list[0]["data"]["abbreviation"]
    print(team_list)
    return team_name, team_city,team_abbreviation

#Code to obtain the information from all teams:
def all_teams():

    #using Fast API and Key to obtain the Information: 
    api_url = f"https://api.balldontlie.io/v1/teams"
    api_key = "e3a45507-3c34-4985-a209-d19601d50d54" # enter your api key
    headers = {"Authorization": f"{api_key}"}
    response = requests.get(api_url, headers=headers)
    print(response.status_code)
    print(response.json())

    # List to store the responses
    team_list = []

    #If the authorization is successful we send the information:
    if response.status_code == 200:
        team_list.append(response.json())

        #We transform the information from JSON to a dataframe for manipulation:
        df = pd.json_normalize(response.json(), 'data')

        #Obtaining the number of teams:
        teams_number = len(df)
        print(teams_number)

        #Configuring the information for a dataframe to be displayed when printing:
        pd.set_option('display.max_rows', 500)
        pd.set_option('display.max_columns', 12)
        pd.set_option('display.width', 400) 

    return teams_number#, team_city,team_abbreviation

#Code to obtain the information from all players:
def players():

    #using Fast API and Key to obtain the Information: 
    api_url = f"https://api.balldontlie.io/v1/players"
    api_key = "e3a45507-3c34-4985-a209-d19601d50d54" # enter your api key
    headers = {"Authorization": f"{api_key}"}
    response = requests.get(api_url, headers=headers)
    print(response.status_code)
    print(response.json())

    # List to store the responses
    team_list = []

    #If the authorization is successful we send the information:
    if response.status_code == 200:
        team_list.append(response.json())

        #We transform the information from JSON to a dataframe for manipulation:
        df = pd.json_normalize(response.json(), 'data')

        #Counting the number of players to show in the dashboard:
        players_number = len(df)
        Highest_country_provider =df['country'].value_counts().idxmax()
        print(Highest_country_provider)
        print(players_number)

        #Getting the height in cm:
        df['height_cm'] = df['height'].apply(height_to_cm)
        highest_height = df['height_cm'].max()
        tallest_player_index = df['height_cm'].idxmax()
        tallest_player = df.loc[tallest_player_index, 'first_name']

        # Extracting country names
        countries = df['country'].value_counts()
        print(countries)

        # Count players for each country





    #Configuring the information for a dataframe to be displayed when printing:
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 12)
    pd.set_option('display.width', 400) 

    #Creating graphs with matplot:
    name = "Height Distribution"
    values = df['height_cm'] 
    graph_matplot.graph_histogram(name,values,"Height","Frecuency" )


    #Creating graphs with matplot:
    name = "Weight Distribution"
    values = df['weight'] 
    print(values)
    graph_matplot.graph_histogram(name,values, "Weight","Frecuency")


    #Creating graphs with matplot:
    name = "Players per country"
    values = countries
    print(values)
    graph_matplot.graph_Barchar(name,values, "Players","Country")
    
    #Creating graphs pygal:
    name = "Players per country"
    values = countries
    print(values)
    graphs_pygal.graph_bar_chart(name,values,"Countries","Number of players" )



    return players_number, Highest_country_provider, highest_height,tallest_player #, team_city,team_abbreviation


#Calculating the height in cm to show the tallest height
def height_to_cm(height):
    feet, inches = map(int, height.split('-'))
    return feet * 30.48 + inches * 2.54