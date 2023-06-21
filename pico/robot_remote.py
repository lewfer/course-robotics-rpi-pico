# Basic robotics remote control template

from PicoRobotics import KitronikPicoRobotics
import time
import digitalio
import board
import network 

PORT = 5000
HOST = "192.168.1.101" 

# Create a network object
net = network.Network()

try:
    # Connect to WIFI
    net.connectWifi()

    # Create receiver to listen for messages
    net.createSender(HOST, PORT)

    # Receive messages
    while True:
        message = net.receiveMessage()
        print("Received", message)
                
        # Process the message
        splitMessage = message.strip().split(",")
        action = splitMessage[0]
        if action=="forward":
            speed = int(splitMessage[1])
            motor.motorOn(1, "f", speed)
            motor.motorOn(2, "f", speed)
        elif action=="stop":
            motor.motorOff(1)
            motor.motorOff(2)

except Exception as e:
    print("Error", e)