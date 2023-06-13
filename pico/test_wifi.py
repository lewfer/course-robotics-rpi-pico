# Test wifi
#
# Make sure your wifi credentials are set up in settings.toml:
#
# CIRCUITPY_WIFI_SSID="YOURWIFISSID"
# CIRCUITPY_WIFI_PASSWORD="YOURPASSWORD"
#

import network

# Create a network object
net = network.Network()

# Connect to the wifi
net.connectWifi()

#  Test network by pinging Google
ipv4 = network.ipaddress.ip_address("8.8.4.4")
print("Ping google.com: %f ms" % (network.wifi.radio.ping(ipv4)*1000))

