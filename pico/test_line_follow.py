# Test button input (button connected to 3V3)

import board
from digitalio import DigitalInOut, Direction, Pull
import time

# Set up the button on pin 18 as a digital input pin
right = DigitalInOut(board.GP6)
right.direction = Direction.INPUT
right.pull = Pull.DOWN               # Pull down so button value is True when pressed

middle = DigitalInOut(board.GP7)
middle.direction = Direction.INPUT
middle.pull = Pull.DOWN               # Pull down so button value is True when pressed

left = DigitalInOut(board.GP8)
left.direction = Direction.INPUT
left.pull = Pull.DOWN               # Pull down so button value is True when pressed

# Show the button status (True is pressed, False is not pressed)
while True:
    print(left.value, middle.value, right.value)
    time.sleep(0.01)