# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
read_pin=4
GPIO.setup(read_pin,GPIO.IN,pull_up_down=GPIO.PUD_UP)

def reading_pin(pin):
    if GPIO.input(read_pin) == 0:
        print("Successfully Read Pin")
        return 1
    
    return 0    
    

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']
account_sid = ""
auth_token = ""

client = Client(account_sid, auth_token)

while(1):
    if read_pin(read_pin):
        message = client.messages \
            .create(
                body='running a test',
                from_='+12137725021',
                to='+1'
            )

        print(message.sid)

        print("a message is sent!")
        print("now sleep 30s")
        sleep(30)
    
    sleep(0.2)