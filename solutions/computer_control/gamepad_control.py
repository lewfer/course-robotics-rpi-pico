# Example solution code to control a RPi Pico robot over a Wifi network using a gamepad

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
countdown = 5

# Keep checking the gamepad
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False # stop the program

    # Get gamepad inputs for KXD controller
    axisy = gamepad.get_axis(1)     # left joytick, y direction. Up = -1, down = 1
    axisx = gamepad.get_axis(0)     # left joystick, x direction.  Left = -1, right = 1
    button0 = gamepad.get_button(0) # Y button
    button1 = gamepad.get_button(1) # B button
    hatx,haty = gamepad.get_hat(0)  # 4-way controller hat

    # Make movements according to gamepad inputs
    # Uses easing (speed*speed) to slow down acceleration
    if axisx>0.2:
        speed = axisx
        speed = int(speed*speed*100)
        command = "right," + str(speed)
    elif axisx<-0.2:
        speed = -axisx
        speed = int(speed*speed*100)
        command = "left," + str(speed)
    elif axisy<-0.2:
        speed = -axisy
        speed = int(speed*speed*100)
        command = "forward," + str(speed)
    elif axisy>0.2:
        speed = axisy
        speed = int(speed*speed*100)
        command = "backward," + str(speed)       
    elif haty==1:
        command = "forward,100"   
    elif haty==-1:
        command = "backward,100"
    elif hatx==-1:
        command = "right,100"
    elif hatx==-1:
        command = "left,100"
    elif button0==1:
        command = "servoup"     
    elif button1==1:
        command = "servodown"            
    else:
        command = "stop"

    # Send command to the robot if it has changed
    if command != lastCommand or countdown > 0:
        print(command)
        net.sendMessage(command)
        if command != lastCommand:
            lastCommand = command
            countdown = 5
        countdown -= 1

    # Fill the window background with white
    screen.fill((255, 255, 255))

    # Update the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()

