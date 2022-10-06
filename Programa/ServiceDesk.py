from colorama import Fore
from Client import Client


class ServiceDesk:
    def __init__(self, code=None, id=None, manager=None, active=False, activenum = None, client=Client()):
        self.__code = code
        self.__id = id
        self.__manager = manager
        self.__active = active
        self.__activenum = activenum
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
        
    def getActiveNum(self):
        return self.__activenum

    def getClient(self):
        return self.__client

    def getClientsCount(self):
        return self.__clientscount

    def getAttentionsClientsTime(self):
        return self.__attentionclientstime

    def getAttentionMinTime(self):
        return self.__attentionmintime

    def getAttentionMaxTime(self):
        return self.__attentionmaxtime

    def setId(self, id):
        self.__id = id

    def setManager(self, manager):
        self.__manager = manager

    def setActive(self, active):
        self.__active = active
        
    def setActiveNum(self, activenum):
        self.__activenum = activenum

    def setClient(self, client=Client()):
        self.__client = client
        self.__clientscount += 1
        self.__attentionclientstime += client.getTransactions().getTime()
        if self.__attentionmaxtime < client.getTransactions().getTime():
            self.__attentionmaxtime = client.getTransactions().getTime()
        if self.__attentionmintime > client.getTransactions().getTime() or self.__attentionmintime == 0:
            self.__attentionmintime = client.getTransactions().getTime()

    def clientOut(self):
        clientout = self.__client
        self.__client = Client()
        return clientout

    def toString(self):
        text = Fore.WHITE + f'Escritorio de servicio: {self.__code}\n'
        if self.__clientscount != 0:
            prom = self.__attentionclientstime/self.__clientscount
        else:
            prom = 0
        text += Fore.MAGENTA + f'Tiempo promedio de atencion: {prom}\nTiempo maximo de atencion: {self.__attentionmaxtime}\nTiempo minimo de atencion: {self.__attentionmintime}'
        return text

    def toStringWithClients(self):
        text = Fore.WHITE + f'Escritorio de servicio: {self.__code}\n'
        if self.__clientscount != 0:
            prom = self.__attentionclientstime/self.__clientscount
        else:
            prom = 0
        text += Fore.MAGENTA + f'Clientes atendidos: {self.__clientscount}\nTiempo promedio de atencion: {prom}\nTiempo maximo de atencion: {self.__attentionmaxtime}\nTiempo minimo de atencion: {self.__attentionmintime}'
        return text