import os
from twilio.rest import Client
import random

#Find your Accound SID and Auth Tokek at twilio.com/console
#and set the enviroment variables. See http://twil.io.secure
account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTHENTICATION_TOKEN')
#client = Client('ACd35627c7b3439c03bdd3993168473c99','de8e7fbca47a8d42840b66bd29198981')
client = Client(account_sid,auth_token)
print(account_sid)
#we will create our db

# Student = {
#     'Alopez':{
#         'name': 'A. Lopez',
#         'number': '+12499792331', #Virtual number
#         'lucky': random.randint[(1,100)],
#         'location': 'sudbury'
#         }
#     }


message = client.messages.create(
    body = "Welcome to BTA Connected Data 1016",
    from_ = '+16466813863',#virtual number
    to = '+12499792331', # Your number

)

# print(message.body)

