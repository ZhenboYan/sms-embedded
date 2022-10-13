# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']
account_sid = "ACc694da8ac49970a09c99ff6a81f6b872"
auth_token = "69e27d55c9c4d94059e3296f55aa49d5"

client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='test',
         from_='+12137725021',
         to='+18327742877'
     )

print(message.sid)
