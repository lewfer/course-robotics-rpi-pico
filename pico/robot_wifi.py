# Basic robotics template

from PicoRobotics import KitronikPicoRobotics
import time
import digitalio
import board
import network 

PORT = 5000

# Create robotics object
motor = KitronikPicoRobotics()

# Create a network object
net = network.Network()

try:
    # Connect to WIFI
    net.connectWifi()

    # Create receiver to listen for messages
    net.createReceiver(PORT)

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