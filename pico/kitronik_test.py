#AllMotorTest.py
# test code that ramps each motor 0-100-0 then changes direction and does it again.
#all motors run at once, but with staggered timings

import PicoRobotics
import time

board = PicoRobotics.KitronikPicoRobotics()
directions = ["f","r"]


for direction in directions:
    for speed in range(0,100):
        board.motorOn(1, direction, speed)
        board.motorOn(2, direction, speed)
        board.motorOn(3, direction, speed)
        board.motorOn(4, direction, speed)
        time.sleep(0.1) #ramp speed over 25x100ms => approx 2.5 second.
        
board.motorOff(1)
board.motorOff(2)
board.motorOff(3)
board.motorOff(4)