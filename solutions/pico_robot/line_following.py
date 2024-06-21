# Test line following sensors (3 way)

import board
from digitalio import DigitalInOut, Direction, Pull
import time
import PicoRobotics

# Create robotics object
motor = PicoRobotics.KitronikPicoRobotics()

# Set up the sensors on the 3 pins
right = DigitalInOut(board.GP10)
right.direction = Direction.INPUT
right.pull = Pull.DOWN   

middle = DigitalInOut(board.GP11)
middle.direction = Direction.INPUT
middle.pull = Pull.DOWN 

left = DigitalInOut(board.GP12)
left.direction = Direction.INPUT
left.pull = Pull.DOWN

speed = 20
speedAdjust = 0.8
direction = "r"

def drive(leftSpeed, rightSpeed):
    if leftSpeed<0:
        motor.motorOn(1, "f", -leftSpeed)
    else:
        motor.motorOn(1, "r", leftSpeed)
    if rightSpeed<0:
        motor.motorOn(2, "f", -rightSpeed)
    else:
        motor.motorOn(2, "r", rightSpeed)
        
# Show the sensor status (True is light, False is dark)
while True:
    LEFT = not left.value
    RIGHT = not right.value
    MIDDLE = not middle.value
    
    print(LEFT, MIDDLE, RIGHT)
    
    if MIDDLE and not LEFT and not RIGHT:
        # We are over the line - go straight
        drive(speed, speed)
        
    elif LEFT and not MIDDLE and not RIGHT:
        # We can see the line to the left - turn full left
        drive(speed, -speed)
        
    elif RIGHT and not MIDDLE and not LEFT:
        # We can see the line to the right - turn full right
        drive(-speed, speed)
        
    elif LEFT and MIDDLE and not RIGHT:
        # We can see the line to the left and centre - turn a bit left
        drive(speed*speedAdjust, -speed*speedAdjust)
        
    elif RIGHT and MIDDLE and not LEFT:
        # We can see the line to the right and centre - turn a bit right
        drive(-speed*speedAdjust, speed*speedAdjust)
        
    elif not LEFT and not MIDDLE and not RIGHT:
        # We can't see the line at all
        drive(speed*speedAdjust, speed*speedAdjust)
        
    elif LEFT and RIGHT and not MIDDLE:
        # We can see the line on both sides but not the centre
        drive(speed*speedAdjust, speed*speedAdjust)
        
    elif LEFT and MIDDLE and RIGHT:
        # We can see the line on all sensors
        drive(speed*speedAdjust, speed*speedAdjust)
        
    time.sleep(0.01)