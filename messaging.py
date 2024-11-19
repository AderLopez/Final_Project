import os
from twilio.rest import Client

#Find your Accound SID and Auth Tokek at twilio.com/console
#and set the enviroment variables. See http://twil.io.secure
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid,auth_token)

#we will create our db

Student = {
    'Alopez':{
        'name': 'A. Lopez',
        'number': '+12499792331', #Virtual number
        'lucky': random.randint[(1,100)],
        'location': 'sudbury'
        }
    }


message = client.messages.create(
    body = "Welcome to BTA Connected Data 1016"
    from = '+1 646 681 3863'#virtual number
    to = '+12499792331' # Your number

)

print(message.body)

