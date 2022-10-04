from colorama import Fore
from Client import Client


class ServiceDesk:
    def __init__(self, code=None, id=None, manager=None, active=False, client=Client()):
        self.__code = code
        self.__id = id
        self.__manager = manager
        self.__active = active
        self.__client = client
        self.__clientscount = 0
        self.__attentionclientstime = 0
        self.__attentionmintime = 0
        self.__attentionmaxtime = 0

    def getCode(self):
        return self.__code
    
    def getId(self):
        return self.__id
    
    def getManager(self):
        return self.__manager

    def getActive(self):
        return self.__active

    def getClient(self):
        return self.__client

    def setId(self, id):
        self.__id = id

    def setManager(self, manager):
        self.__manager = manager

    def setActive(self, active):
        self.__active = active

    def setClient(self, client=Client()):
        self.__client = client
        self.__clientscount += 1
        self.__attentionclientstime += client.getTransactions().getTime()
        if self.__attentionmaxtime < client.getTransactions().getTime():
            self.__attentionmaxtime = client.getTransactions().getTime()
        if self.__attentionmintime > client.getTransactions().getTime() or self.__attentionmintime == 0:
            self.__attentionmintime = client.getTransactions().getTime()

    def toString(self):
        text = Fore.WHITE + f'Escritorio de servicio:\n'
        if self.__clientscount != 0:
            prom = self.__attentionclientstime/self.__clientscount
        else:
            prom = 0
        text += Fore.MAGENTA + f'Tiempo promedio de atencion: {prom}\nTiempo maximo de atencion: {self.__attentionmaxtime}\nTiempo minimo de atencion: {self.__attentionmintime}'
        return text