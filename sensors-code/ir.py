import RPi.GPIO as GPIO 
import time 
inPin2 = 7
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(inPin2, GPIO.IN)
while True:
    value2 = GPIO.input(inPin2)
    print(value)

    if value2 :
        print('not detected')
    else:
        print('detected')
    time.sleep(0.1)
