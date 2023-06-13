import socket


class Network:
    def __init__(self):
        pass

    def createSender(self, host, port):
        # Set up a socket connection
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
        self.socket.settimeout(None)

        self.host = host
        self.port = port

    def sendMessage(self, message):
        return self.socket.sendto(str.encode(message), (self.host, self.port))

