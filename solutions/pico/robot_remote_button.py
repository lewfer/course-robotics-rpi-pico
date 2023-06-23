# Basic robotics remote control template
# Using buttons as controls

import time
from digitalio import DigitalInOut, Direction, Pull
import board
import network 

PORT = 5000
HOST = "192.168.1.101" 

# Set up the buttons 
up = DigitalInOut(board.GP16)
up.direction = Direction.INPUT
up.pull = Pull.DOWN               # Pull down so button value is True when pressed

down = DigitalInOut(board.GP17)
down.direction = Direction.INPUT
down.pull = Pull.DOWN               # Pull down so button value is True when pressed

left = DigitalInOut(board.GP18)
left.direction = Direction.INPUT
left.pull = Pull.DOWN               # Pull down so button value is True when pressed

right = DigitalInOut(board.GP19)
right.direction = Direction.INPUT
right.pull = Pull.DOWN               # Pull down so button value is True when pressed

press = DigitalInOut(board.GP20)
press.direction = Direction.INPUT
press.pull = Pull.DOWN               # Pull down so button value is True when pressed



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
            print("up")
            net.sendMessage("forward,20")
        elif down.value:
            print("down")
            net.sendMessage("backward,20")
        elif left.value:
            print("left")
            net.sendMessage("left,20")
        elif right.value:
            print("right")
            net.sendMessage("right,20")
        elif press.value:
            print("servo")
            net.sendMessage("servoup")
            time.sleep(0.5)
            net.sendMessage("servodown")
        else:
            net.sendMessage("stop")
        time.sleep(0.1)

except Exception as e:
    print("Error", e)