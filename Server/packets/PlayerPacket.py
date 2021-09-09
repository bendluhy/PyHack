import pickle

class PlayerPacket:
    def __init__(self, details, data):
        self.details = details
        self.data = data
        self.packetDetails = {
            "Details": self.details,
            "Data": self.data
        }