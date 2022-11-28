# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
read_pin=4
GPIO.setup(read_pin,GPIO.IN,pull_up_down=GPIO.PUD_UP)

def reading_pin(pin):
    if GPIO.input(read_pin) == 0:
        print("Successfully Read Pin")
        return True
    
    return False
    

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
phone_number = str(os.environ['PHONE_NUMBER'])
message = "pin activated"

client = Client(account_sid, auth_token)

while(1):
    if read_pin(read_pin):
        message = client.messages \
            .create(
                body=f'{message}',
                from_='+12137725021',
                to=f'+1{phone_number}'
            )
            
        print(message.sid)
        print("a message is sent!")
        print("now sleep 30s")
        sleep(30)
    
    sleep(0.2)