# Template code to control a RPi Pico robot over a Wifi network using a gamepad

# Import the pygame library
import pygame
from pygame.locals import *
import network

# Specify the IP address of your robot
HOST = "192.168.1.80" 

# Specify the port number to send messages on
PORT = 5000

# Create a network object
net = network.Network()

# Set up a message sender
net.createSender(HOST, PORT)

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Run until the user asks to quit
running = True

# Initialise the gamepad
pygame.joystick.init()
gamepad = pygame.joystick.Joystick(0)

# Set up the initial command
command = "stop"        # current command
lastCommand = "stop"    # previous command

# Keep checking the gamepad
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False # stop the program

    # Get gamepad inputs
    axis1 = gamepad.get_axis(1)
    button1 = gamepad.get_button(1)
    hatx,haty = gamepad.get_hat(0)

    # Make movements according to gamepad inputs
    if axis1<-0.5:
        command = "forward,50"
    elif haty==1:
        command = "forward,100"
    elif button1==1:
        command = "forward,20"         
    else:
        command = "stop"

    # Send command to the robot if it has changed
    if command != lastCommand:
        net.sendMessage(command)
        lastCommand = command

    # Fill the window background with white
    screen.fill((255, 255, 255))

    # Update the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()

