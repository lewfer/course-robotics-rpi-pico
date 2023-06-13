import network
import time

HOST = "192.168.1.101" 
PORT = 5000

# Create a network object
net = network.Network()

# Set up a message sender
net.createSender()

# Send messages to drive the robot forward for 2 seconds then stop
net.sendMessage(HOST, PORT, "forward,20")
time.sleep(2)
net.sendMessage(HOST, PORT, "stop")
