from StackDesk import StackDesk
from ListClient import ListClient

class AttentionPoint:
    def __init__(self, code=None, name=None, address=None, desks = StackDesk(), clients=ListClient()):
        self.__code = code
        self.__name = name
        self.__address = address
        self.__desks = desks
        self.__clients = clients
    
    def getCode(self):
        return self.__code
    
    def getName(self):
        return self.__name

    def getAddress(self):
        return self.__address
    
    def getDesks(self):
        return self.__desks

    def getClients(self):
        return self.__clients
    
    def setName(self, name):
        self.__name = name

    def setAddress(self, address):
        self.__address = address

    def setDesks(self, desks = StackDesk()):
        self.__desks = desks

    def setClients(self, clients = ListClient()):
        self.__clients = clients

    def toStringWithoutDesks(self):
        return f'Código: {self.__code},     Nombre: {self.__name},      Dirección: {self.__address}'