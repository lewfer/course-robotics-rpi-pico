# Basic robotic movements

import PicoRobotics
import time

# Create robotics object
robot = PicoRobotics.KitronikPicoRobotics()

speed = 100

print("Forward")
robot.motorOn(1, "f", speed)
robot.motorOn(2, "f", speed)
time.sleep(5)


print("Reverse")
robot.motorOn(1, "r", speed)
robot.motorOn(2, "r", speed)
time.sleep(5)

print("Left")
robot.motorOn(1, "f", 0)
robot.motorOn(2, "f", speed)
time.sleep(2)

print("Right")
robot.motorOn(1, "f", speed)
robot.motorOn(2, "f", 0)
time.sleep(2)

print("Stop")
robot.motorOff(1)
robot.motorOff(2)
