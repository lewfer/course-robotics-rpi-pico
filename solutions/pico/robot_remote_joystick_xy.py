# Basic robotics remote control template
# Using a 2-axis analogue joystick

import time
from digitalio import DigitalInOut, Direction, Pull
import analogio
import board
import network 

PORT = 5000
HOST = "192.168.1.113" 

#  Set up axes on pins 27 and 28 as an analogue input pin
axisy = analogio.AnalogIn(board.GP27_A1)
axisx = analogio.AnalogIn(board.GP28_A2)

# Set up the button on pin 18 as a digital input pin
press = DigitalInOut(board.GP18)
press.direction = Direction.INPUT
press.pull = Pull.UP               # Pull up so button value is True when not pressed


# Create a network object
net = network.Network()

try:
    # Connect to WIFI
    net.connectWifi()

    # Create receiver to listen for messages
    net.createSender(HOST, PORT)

    # Receive messages
    base = 1200
    while True:
        # Centre x and y on 0
        valy = axisy.value - 32767
        valx = axisx.value - 32767

        # Compute speed, applying easing to slow the acceleration
        speed = (abs(valy)-base)/(32767-base)
        speed = int(speed * speed * 100)
        print(valx,valy, press.value,speed)

        # Interpret the 
        if valx < -base:
            net.sendMessage("left," + str(40))
        elif valx > base:
            net.sendMessage("right," + str(40))
        elif valy > base:
            net.sendMessage("forward," + str(speed))
        elif valy < -base:
            net.sendMessage("backward," + str(speed))
        elif not press.value:
            print("servo")
            net.sendMessage("servoup")
            time.sleep(0.5)
            net.sendMessage("servodown")            
        else:
            net.sendMessage("stop")
        time.sleep(0.1)

except Exception as e:
    print("Error", e)