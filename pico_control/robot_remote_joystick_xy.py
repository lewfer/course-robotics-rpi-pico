# Template to control a RPi Pico robot over Wifi from another Pico using a 2-axis analogue joystick

import time
from digitalio import DigitalInOut, Direction, Pull
import analogio
import board
import network 

# Specify the IP address of your robot
HOST = "192.168.1.80" 

# Specify the port number to send messages on
PORT = 5000

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
    while True:
        # Centre x and y on 0
        valy = axisy.value - 32767
        valx = axisx.value - 32767

        # Act on the values
        print(valx,valy, press.value)
        if valy > 2000:
            net.sendMessage("forward,20")
        else:
            net.sendMessage("stop")
        time.sleep(0.1)

except Exception as e:
    print("Error", e)