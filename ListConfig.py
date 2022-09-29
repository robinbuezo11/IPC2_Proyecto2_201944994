from Config import Config
from NodeConfig import NodeConfig

class ListConfig:
    def __init__(self):
        self.__first = NodeConfig()

    def getFirst(self):
        return self.__first

    def setFirst(self, first = NodeConfig()):
        self.__first = first

    def insert(self, config = Config()):
        
        if self.__first.getConfig().getCode() == None:
            self.__first = NodeConfig(config=config)
            return

        nodeaux=self.__first
        while nodeaux.getNext():
            nodeaux = nodeaux.getNext()
        nodeaux.setNext(NodeConfig(config=config))