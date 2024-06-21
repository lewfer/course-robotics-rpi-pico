# Test motor with kitronik robotics board on a RPi Pico

import PicoRobotics
import time

# Create robotics object
robot = PicoRobotics.KitronikPicoRobotics()

# Move motor forward, increasing speed
print("Forward")
for speed in range(0,100):
    robot.motorOn(1, "f", speed)
    time.sleep(0.1)

# Move motor backward, increasing speed
print("Reverse")
for speed in range(0,100):
    robot.motorOn(1, "r", speed)
    time.sleep(0.1)

print("Stop")
robot.motorOff(1)
