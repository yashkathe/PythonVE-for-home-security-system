
from flask import Flask, request, render_template
import sys
import Adafruit_DHT

app = Flask(__name__)
app.debug = True # Make this False if you are no longer debugging

@app.route("/")
def hello():
    return render_template("intro.html")

@app.route("/lab_temp")
def lab_temp():
	humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 17)
	if humidity is not None and temperature is not None:
		return render_template("lab_temp.html",temp=temperature,hum=humidity)
	else:
		return render_template("no_sensor.html")

@app.route("/other_sensors")
def sensors2():
        import RPi.GPIO as GPIO 
        import time 
        inPin = 13
        inPin2 = 7
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(inPin, GPIO.IN)
        GPIO.setup(inPin2, GPIO.IN)
        while True:
            value = GPIO.input(inPin)
            value2 = GPIO.input(inPin2)
            
            if value2 == 1 and value == 1:
                return render_template("other-sensors.html", message = "not detected" , message2 = "Gas leak detected")
            elif value2==1 and value==0:
                return render_template("other-sensors.html", message = "not detected" , message2 = "No Gas leak detected")
            elif value2==0 and value==1:
                return render_template("other-sensors.html", message = "detected" , message2 = "Gas leak detected")
            else:
                return render_template("other-sensors.html", message = "detected", message2 = "No Gas leak detected")
            time.sleep(0.1)






if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)


