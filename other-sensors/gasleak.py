import RPi.GPIO as GPIO 
import time 
inPin = 13
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(inPin, GPIO.IN)
while True:
    value = GPIO.input(inPin)
    print(value)

    if value :
        print('Gas leak detected')
    else:
        print('No Gas Leak detected')
    time.sleep(0.1)
