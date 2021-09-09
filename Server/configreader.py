
class Config():
    def __init__(self, location):
        self.file = open(location, "r")
        self.lines = self.file.readlines()

    def getPort(self):
        return int(self.lines[1].replace("port=", ""))

    def getHost(self):
        return self.lines[2].replace("host=", "")