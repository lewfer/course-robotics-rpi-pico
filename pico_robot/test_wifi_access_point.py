# Test wifi access pointon a RPi Pico
#
# Make sure your settings.toml is empty
#

import network

# Create a network object
net = network.Network()

# Create a wireless access point, providing the SSID and password
net.startWifiAccessPoint("mypico","hellorobot")


