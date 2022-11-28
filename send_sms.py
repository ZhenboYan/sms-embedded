# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
phone_number = str(os.environ['PHONE_NUMBER'])

client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='running a test',
         from_='+12137725021',
         to=f'+1{phone_number}'
     )

print(message.sid)
