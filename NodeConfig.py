from Config import Config

class NodeConfig:
    def __init__(self, config = Config(), next = Config()):
        self.__config = config
        self.__next = next

    def getConfig(self):
        return self.__config

    def getNext(self):
        return self.__next

    def setNext(self, next):
        self.__next = next