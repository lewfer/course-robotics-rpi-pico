# Think Create Learn Raspberry Pi Pico Robotics Course
# 

For more details:
[www.thinkcreatelearn.co.uk](www.thinkcreatelearn.co.uk)


Based on [Adafruit Circuit Python for Raspberry Pi Pico v9](https://circuitpython.org/board/raspberry_pi_pico_w/)



## pico_robot directory

Code samples to run on the RPi Pico robot.

|File                   |Description                                                                                    |
|-----------------------|-----------------------------------------------------------------------------------------------|
|robot_movements.py     |Template for robotic movements for a RPi Pico Robot                                            |
|robot_wifi.py          |Template for a wifi-controlled RPi Pico Robot                                                  |
|test*.py               |Various programs to test different components                                                  |     
|lib\network.py         |Module that encapsulates wifi network functionality needed for robotics functions on a RPi Pico|
|lib\PicoRobotics.py    |Module provided by Kitronik to control their motor controller board                            |
|lib\adafruit_hcsr04.mpy|Module provided by Adafruit to control an ultrasonic sensor                                    |



## computer_control directory

Code samples to show how to control the RPi Pico robot over Wifi from a computer

|File                   |Description                                                                                 |
|-----------------------|--------------------------------------------------------------------------------------------|
|control.py             |Template code to control a RPi Pico robot over a Wifi network                               |
|kb_control.py          |Template code to control a RPi Pico robot over a Wifi network using the computer keyboard   |  
|gamepad.py             |Template code to control a RPi Pico robot over a Wifi network using a gamepad               |
|network.py             |Module that encapsulates wifi network functionality needed for robot control from a computer|
|pygame-joystick-test.py|Tool to check gamepad controls                                                              |

## pico_control directory

Code samples to show how to control the RPi Pico robot over Wifi from another RPi Pico

|File                       |Description                                                                                      |
|---------------------------|-------------------------------------------------------------------------------------------------|
|robot_remote_button.py     |Template code to control a RPi Pico robot over Wifi from another Pico using buttons as controls  |
|robot_remote_joystick_xy.py|Template to control a RPi Pico robot over Wifi from another Pico using a 2-axis analogue joystick|

## solutions directory

Here you can find possible solutions for the robot and various remote control approaches.
