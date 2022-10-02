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

    def toString(self):
        if self.__first.getEnterprise().getCode() == None:
            return Fore.RED + 'No existe ninguna empresa en la lista'
        
        nodeaux = self.__first
        string = ''
        while nodeaux:
            string += nodeaux.getEnterprise().toStringWithoutPoints()
            string += '\n'
            nodeaux = nodeaux.getNext()
        return string

    def getEnterpriseByCode(self, code):
        nodeaux = self.__first
        while nodeaux:
            if nodeaux.getEnterprise().getCode() == code:
                return nodeaux.getEnterprise()
            nodeaux = nodeaux.getNext()
        return Enterprise()
