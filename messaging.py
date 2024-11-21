import os
from twilio.rest import Client
import random
import json

def messaging_process():
    try:
        #Find your Account SID and Auth Token at twilio.com/console
        #and set the environment variables. See http://twil.io.secure
        account_sid = os.getenv('ACCOUNT_SID')
        auth_token = os.getenv('AUTHENTICATION_TOKEN')
        client = Client(account_sid,auth_token)
        #we will create our db

        import space_information
        import get_weather
        import harry_potter

        number_people_space =   space_information.space_people_number()
        print(number_people_space)  
        temperature = get_weather.get_city('sudbury')
        print(temperature)
        harry_message = harry_potter.information()
        print(harry_message)



        user_list = {
            'Username_1':{
            'name': 'Username_1',
            'number': os.getenv('MY_PHONE_NUMBER'),
            'lucky': random.randint(1,100),
            'location': 'sudbury'
            },

            'Username_2':{
            'name': 'Username_2',
            'number': os.getenv('MY_PHONE_NUMBER'),
            'lucky': random.randint(1,100),
            'location': 'calgary'
            }
        

        }




        for key, value in user_list.items():
            
            #Creating a Message to send
            text_message = f'Hello {value['name'].title()} your lucky number is {value['lucky']} and the number of people in space are {number_people_space} and in the city of {value['location']} the temperature is {temperature}. The Harry Potter character details are {harry_message} '
            print(text_message) 
            message = client.messages.create(
            body = text_message,
            from_ = '+16466813863',#virtual number
            to = os.getenv('MY_PHONE_NUMBER'), # Your number
            )
            with open('message.json','a') as outfile: #saving the file
                json.dump(text_message,outfile, indent = 4)

        Message = "You send a text message successfully"

        return Message
    except:
        Message = "There was a problem sending your message"
        return Message


