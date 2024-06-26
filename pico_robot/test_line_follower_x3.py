# Test line following sensors (3 way) on a RPi Pico

import board
from digitalio import DigitalInOut, Direction, Pull
import time

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

# Show the sensor status (True is light, False is dark)
while True:
    print(left.value, middle.value, right.value)
    time.sleep(0.01)