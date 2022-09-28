from NodeConfig import NodeConfig

class ListConfig:
    def __init__(self):
        self.__first = NodeConfig()

    def getFirst(self):
        return self.__first

    def setFirst(self, first = NodeConfig()):
        self.__first = first