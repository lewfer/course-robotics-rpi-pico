# Basic robotics remote control template
# Using a 2-axis analogue joystick

import time
from digitalio import DigitalInOut, Direction, Pull
import analogio
import board
import network 

PORT = 5000
HOST = "192.168.1.101" 

#  Set up axes on pins 27 and 28 as an analogue input pin
axis1 = analogio.AnalogIn(board.GP27_A1)
axis2 = analogio.AnalogIn(board.GP28_A2)

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
    while True:
        val1 = axis1.value
        val2 = axis2.value
        print(val1,val2, press.value)
        if val1 > 40000:
            net.sendMessage("forward,20")
        else:
            net.sendMessage("stop")
        time.sleep(0.1)

except Exception as e:
    print("Error", e)