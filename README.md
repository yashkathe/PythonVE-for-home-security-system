
# Home Security System with RaspberryPI

The system with a help of few sensors, monitored by our RPi, keeps our house safe from 
burglars, gas leaks and also monitors the room temperature conditions.


## Compoenents used

    1. Raspberry Pi 3B+
    2. DHT22 sensor (temperature and humidity)
    3. MQ6 sensor (gas leak)
    4. IR sensor (for burglar alarm)

## Packages installed 

    1. Flask
    2. NGiNX
    3. UWSGI
    4. Skeleton


## Analysis

- At the bottom of the stack is the hardware, which in our case is Raspberry Pi 3B+.
- On top of this, we got our OS, which is Raspbian Stretch Lite.
- The OS gives us access to the features of the hardware.
- On top of the OS, we have got a python web micro framework called Flask.
- Flask specializes in making it easy to create simple web applications.
- The application server we using is uWSGI.
- uWSGI is a link between our actual web server and our flask application.
- The web server that we are using is NGiNX.
- NGinX is responsible for exposing our application to the internet

## Circuit Diagram

![Circuit Digram](https://raw.githubusercontent.com/yashkathe/Security-system-with-raspberryPi/college-project/assets/Picture1.png)


## Circuit connections

![P 1](https://raw.githubusercontent.com/yashkathe/Security-system-with-raspberryPi/college-project/assets/Picture4.png)
![P 2](https://raw.githubusercontent.com/yashkathe/Security-system-with-raspberryPi/college-project/assets/Picture5.png)
![P 3](https://raw.githubusercontent.com/yashkathe/Security-system-with-raspberryPi/college-project/assets/Picture7.png)

## Website to read sensor states

![p 1](https://raw.githubusercontent.com/yashkathe/Security-system-with-raspberryPi/college-project/assets/Picture2.png)
![p 1](https://raw.githubusercontent.com/yashkathe/Security-system-with-raspberryPi/college-project/assets/Picture3.png)
