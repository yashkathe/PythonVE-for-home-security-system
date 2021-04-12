import RPi.GPIO as GPIO 
import time 
inPin2 = 7
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(inPin, GPIO.IN)
while True:
    value = GPIO.input(inPin2)
    print(value)

    if value :
        print('not detected')
    else:
        print('detected')
    time.sleep(0.1)
