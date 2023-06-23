# Basic robotics remote control template

import time
from digitalio import DigitalInOut, Direction, Pull
import board
import network 

PORT = 5000
HOST = "192.168.1.101" 

# Set up the button on pin 16 as a digital input pin
up = DigitalInOut(board.GP16)
up.direction = Direction.INPUT
up.pull = Pull.DOWN               # Pull down so button value is True when pressed


# Create a network object
net = network.Network()

try:
    # Connect to WIFI
    net.connectWifi()

    # Create receiver to listen for messages
    net.createSender(HOST, PORT)

    # Receive messages
    while True:
        if up.value:
            net.sendMessage("forward,20")
        else:
            net.sendMessage("stop")

except Exception as e:
    print("Error", e)