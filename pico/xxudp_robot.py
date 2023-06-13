# Test UDP receive
#
# MQTT with CircuitPython: https://learn.adafruit.com/mqtt-in-circuitpython/circuitpython-wifi-usage


import os
import wifi
import socketpool
import PicoRobotics
import time
import digitalio
import board

print()
print("Connecting to WiFi")

# Create robotics object
robot = PicoRobotics.KitronikPicoRobotics()

# Status LED
led = digitalio.DigitalInOut(board.GP2)
led.direction = digitalio.Direction.OUTPUT

try:
    # Connect to WIFI
    # -------------------------------------------------------------

    #  Connect to your SSID
    wifi.radio.connect(os.getenv('CIRCUITPY_WIFI_SSID'), os.getenv('CIRCUITPY_WIFI_PASSWORD'))

    print("Connected to WiFi...")

    #  Prints MAC address 
    print("My MAC addr:", [hex(i) for i in wifi.radio.mac_address])

    #  Prints IP address 
    print("My IP address is", wifi.radio.ipv4_address)

    led.value = True
    time.sleep(0.5)
    led.value = False

    # Create UDP listener
    # -------------------------------------------------------------

    HOST = str(wifi.radio.ipv4_address)
    PORT = 5000
    TIMEOUT = None
    MAXBUF = 256

    # Create a socket pool to allow network comms
    pool = socketpool.SocketPool(wifi.radio)

    # Create socket bound to a port
    print("\nCreate UDP Server socket")
    s = pool.socket(pool.AF_INET, pool.SOCK_DGRAM)
    s.settimeout(TIMEOUT)
    s.bind((HOST, PORT))

    # Receive messages
    buf = bytearray(MAXBUF)
    while True:
        size, addr = s.recvfrom_into(buf)
        message = buf[:size].decode()
        print(size, "bytes from", addr)
        print("Received", message, size, "bytes from", addr)
        
        led.value = True
        time.sleep(0.1)
        led.value = False
        
        splitMessage = message.split(",")
        if splitMessage[0]=="forward":
            robot.motorOn(1, "f", 100)
            robot.motorOn(2, "f", 100)
        elif splitMessage[0]=="backward":
            robot.motorOn(1, "r", 100)
            robot.motorOn(2, "r", 100)
        elif splitMessage[0]=="stop":
            robot.motorOff(1)
            robot.motorOff(2)
        elif splitMessage[0]=="servoup":
            robot.servoWrite(1, 160)
        elif splitMessage[0]=="servodown":
            robot.servoWrite(1, 20)

except Exception as e:
    print("Error", e)