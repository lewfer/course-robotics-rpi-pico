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

# Set up a status LED
led = digitalio.DigitalInOut(board.GP2)
led.direction = digitalio.Direction.OUTPUT

try:
    # Connect to WIFI
    net.connectWifi()
    #net.startWifiAccessPoint("myrobot","hellorobot")

    # Flash LED to show that wifi connection has completed
    led.value = True
    time.sleep(0.5)
    led.value = False

    # Create receiver to listen for messages
    net.createReceiver(PORT)

    # Receive messages
    while True:
        message = net.receiveMessage()
        print("Received", message)
        
        # Flash LED to show that a message has been received
        led.value = True
        time.sleep(0.1)
        led.value = False
        
        # Process the message
        splitMessage = message.strip().split(",")
        action = splitMessage[0]
        if action=="forward":
            speed = int(splitMessage[1])
            motor.motorOn(1, "f", speed)
            motor.motorOn(2, "f", speed)
        elif action=="backward":
            speed = int(splitMessage[1])
            motor.motorOn(1, "r", speed)
            motor.motorOn(2, "r", speed)
        elif action=="left":
            speed = int(splitMessage[1])
            motor.motorOn(1, "r", speed)
            motor.motorOn(2, "f", speed)
        elif action=="right":
            speed = int(splitMessage[1])
            motor.motorOn(1, "f", speed)
            motor.motorOn(2, "r", speed)            
        elif action=="stop":
            motor.motorOff(1)
            motor.motorOff(2)
        elif action=="servoup":
            motor.servoWrite(1, 160)
        elif action=="servodown":
            motor.servoWrite(1, 20)

except Exception as e:
    print("Error", e)