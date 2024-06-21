# Example solution code to control a RPi Pico robot over a Wifi network using the computer keyboard

import network
import msvcrt

# Specify the IP address of your robot
HOST = "192.168.1.80" 

# Specify the port number to send messages on
PORT = 5000

# Create a network object
net = network.Network()

# Set up a message sender
net.createSender(HOST, PORT)

# Get a keyboard character
def getCh():
    c = ord(msvcrt.getch())
    if (c==0 or c==224):
        c = ord(msvcrt.getch())
        return "right" if c==77 else "left" if c==75 else "up" if c==72 else "down" if c==80 else ""
    else:
        return chr(c) 

# Wait for key presses and send appropriate commands to the robot
c = " "
while c!="x" :
    c = getCh()
    print(c)
    if c=="up":
        net.sendMessage("forward,20")
    elif c=="down":
        net.sendMessage("backward,20")
    elif c=="left":
        net.sendMessage("left,20")
    elif c=="right":
        net.sendMessage("right,20")
    elif c==" ":
        net.sendMessage("stop")

