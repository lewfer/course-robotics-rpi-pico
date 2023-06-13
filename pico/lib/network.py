# network.py
#
# Encapsulates wifi network functionality needed for robotics functions
#
# https://learn.adafruit.com/pico-w-wifi-with-circuitpython/pico-w-basic-wifi-test


import wifi
import os
import socketpool
import ipaddress

PORT = 5000

class Network:
    def __init__(self):
        pass

    def connectWifi(self):
        #  Connect to your SSID
        wifi.radio.connect(os.getenv('CIRCUITPY_WIFI_SSID'), os.getenv('CIRCUITPY_WIFI_PASSWORD'))

        print("Connected to WiFi...")

        self.host = wifi.radio.ipv4_address

        #  Prints MAC address 
        print("My MAC addr:", [hex(i) for i in wifi.radio.mac_address])

        #  Prints IP address 
        print("My IP address is", self.host)

    # Remove contents from settings.toml to use this
    def startWifiAccessPoint(self, ap_ssid, ap_password):
        wifi.radio.hostname = "RPiPico"

        # Start access point
        wifi.radio.start_ap(ssid=ap_ssid, password=ap_password)

        
        self.host = wifi.radio.ipv4_address_ap

        # Show access point settings
        print("Access point created with SSID: {}, password: {}".format(ap_ssid, ap_password))

        #  Prints MAC address 
        print("My MAC addr:", [hex(i) for i in wifi.radio.mac_address])

        # Show IP address
        print("IP address is", self.host)

    def createSocket(self):
        
        HOST = str(self.host)
        TIMEOUT = None

        # Create a socket pool to allow network comms
        print("1", HOST)
        pool = socketpool.SocketPool(wifi.radio)

        # Create socket bound to a port
        print("\nCreate UDP Server socket")
        self.s = pool.socket(pool.AF_INET, pool.SOCK_DGRAM)
        print("2")
        self.s.settimeout(TIMEOUT)
        print("3")
        self.s.bind((HOST, PORT))
        print("4")


    def getMessage(self):
        MAXBUF = 256
        buf = bytearray(MAXBUF)
        size, addr = self.s.recvfrom_into(buf)
        message = buf[:size].decode()
        return message
    

    def sendMessage(self, host, port, message):
        size = self.s.sendto(str.encode(message), (host, port))
        return size

