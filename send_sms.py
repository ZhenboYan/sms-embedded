import sys
import serial
from time import sleep

NUM = sys.argv[2]
MSG = sys.argv[3]

SERIAL_PORT = '/dev/{}'.format(sys.argv[1])

SERIAL_RATE = 115200
ser = serial.Serial(SERIAL_PORT,SERIAL_RATE)


OPERATE_SMS_MODE = 'AT+CMGF=1\r'
SEND_SMS = 'AT+CMGS="{}"\r'.format(NUM)

def sendCommand(command):
	ser.write(command.encode())
	sleep(0.2)
    
def main():
	print ("Sending SMS to {}".format(NUM))
	if not ser.is_open:
		ser.open()
        print("here1")
        
	if ser.is_open:
		sendCommand(OPERATE_SMS_MODE)
		sendCommand(SEND_SMS)
		sendCommand(MSG)
		sendCommand('\x1A')	#sending CTRL-Z
							#https://en.wikipedia.org/wiki/ASCII
        print("here2")

		ser.close()

if __name__ == "__main__":
	try:
		main()
        print("here13")

	except ValueError as e:
		print ("Error : {}".format(e))