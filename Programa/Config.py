from ListClient import ListClient
from StackDesk import StackDesk

class Config:
    def __init__(self, code=None, codempresa=None, codpunto=None, desks = StackDesk(), clients = ListClient()):
        self.__code = code
        self.__codempresa = codempresa
        self.__codpunto = codpunto
        self.__desks = desks
        self.__clients = clients

    def getCode(self):
        return self.__code

    def getCodEmpresa(self):
        return self.__codempresa
    
    def getCodPunto(self):
        return self.__codpunto

    def getDesks(self):
        return self.__desks

    def getClients(self):
        return self.__clients

    def setCodEmpresa(self, codempresa):
        self.__codempresa = codempresa

    def setCodPunto(self, codpunto):
        self.__codpunto = codpunto
    
    def setDesks(self, desks = StackDesk()):
        self.__desks = desks

    def setClients(self, clients = ListClient()):
        self.__clients = clients