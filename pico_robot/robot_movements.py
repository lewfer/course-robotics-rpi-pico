# Template for robotic movements for a RPi Pico Robot

import PicoRobotics
import time

# Create robotics object
motor = PicoRobotics.KitronikPicoRobotics()

speed = 100

print("Forward")
motor.motorOn(1, "f", speed)
motor.motorOn(2, "f", speed)
time.sleep(5)

print("Reverse")
# TODO

print("Left")
# TODO

print("Right")
# TODO

print("Stop")
motor.motorOff(1)
motor.motorOff(2)
