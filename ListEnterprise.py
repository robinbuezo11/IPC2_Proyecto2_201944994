from colorama import Fore
from Enterprise import Enterprise
from NodeEnterprise import NodeEnterprise

class ListEnterprise:
    def __init__(self):
        self.__first = NodeEnterprise()

    def getFirst(self):
        return self.__first

    def setFirst(self, first = NodeEnterprise()):
        self.__first = first

    def insert(self, enterprise = Enterprise()):
        
        if self.__first.getEnterprise().getCode() == None:
            self.__first = NodeEnterprise(enterprise=enterprise)
            return True

        nodeaux=self.__first
        while nodeaux.getNext():
            if nodeaux.getEnterprise().getCode() == enterprise.getCode():
                print(Fore.RED + f'La empresa {enterprise.getCode()} ya existe en la lista')
                return False
            nodeaux = nodeaux.getNext()
        if nodeaux.getEnterprise().getCode() == enterprise.getCode():
            print(Fore.RED + f'La empresa {enterprise.getCode()} ya existe en la lista')
            return False
        nodeaux.setNext(NodeEnterprise(enterprise=enterprise))
        return True