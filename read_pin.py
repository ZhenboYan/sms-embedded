from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
read_pin=16

GPIO.setup(read_pin,GPIO.IN,pull_up_down=GPIO.PUD_UP)

while(1):
    if GPIO.input(read_pin) == 0:
        print("sending message now")
        sleep(0.1)
        