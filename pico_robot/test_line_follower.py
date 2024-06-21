# Test line following sensor on a RPi Pico

import board
from digitalio import DigitalInOut, Direction, Pull
import time

# Set up the sensor
sensor = DigitalInOut(board.GP10)
sensor.direction = Direction.INPUT
sensor.pull = Pull.DOWN   

# Show the sensor status (True is light, False is dark)
while True:
    print(sensor.value)
    time.sleep(0.01)
