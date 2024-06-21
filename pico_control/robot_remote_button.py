# Template to control a RPi Pico robot over Wifi from another Pico using buttons as controls

import time
from digitalio import DigitalInOut, Direction, Pull
import board
import network 

# Specify the IP address of your robot
HOST = "192.168.1.80" 

# Specify the port number to send messages on
PORT = 5000

# Set up a button on pin 16 as a digital input pin
up = DigitalInOut(board.GP16)
up.direction = Direction.INPUT
up.pull = Pull.DOWN               # Pull down so button value is True when pressed


# Create a network object
net = network.Network()

try:
    # Connect to WIFI
    net.connectWifi()

    # Set up a message sender
    net.createSender(HOST, PORT)

    # Send messages
    while True:
        if up.value:
            net.sendMessage("forward,20")
        else:
            net.sendMessage("stop")
        time.sleep(0.1)

except Exception as e:
    print("Error", e)