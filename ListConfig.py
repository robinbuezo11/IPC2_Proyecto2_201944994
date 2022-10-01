from colorama import Fore
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
            return True

        nodeaux=self.__first
        while nodeaux.getNext():
            if nodeaux.getConfig().getCode() == config.getCode():
                print(Fore.RED + f'La configuración {config.getCode()} ya existe en la lista')
                return False
            nodeaux = nodeaux.getNext()
        if nodeaux.getConfig().getCode() == config.getCode():
            print(Fore.RED + f'La configuración {config.getCode()} ya existe en la lista')
            return False
        nodeaux.setNext(NodeConfig(config=config))
        return True