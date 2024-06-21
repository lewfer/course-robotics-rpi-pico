# Test ultrasonic distance sensor on a RPi Pico

import time
import board
import adafruit_hcsr04

# Create the sonar object connected to the given pins
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.GP6, echo_pin=board.GP7)

# Display the distance measurement
while True:
    try:
        print(sonar.distance)
    except RuntimeError:
        print("Error")
    time.sleep(0.1)