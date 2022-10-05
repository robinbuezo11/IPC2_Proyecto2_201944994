from colorama import Fore
from Client import Client
from NodeClient import NodeClient

class ListClient:
    def __init__(self):
        self.__first = NodeClient()
        self.__clientscount = 0
        self.__clientstime = 0
        self.__mintime = 0
        self.__maxtime = 0
        self.__attentionclientstime = 0

    def getFirst(self):
        return self.__first

    def getClientsCount(self):
        return self.__clientscount

    def setFirst(self, first = NodeClient()):
        self.__first = first

    def insert(self, client = Client()):
        
        if self.__first.getClient().getDpi() == None:
            self.__first = NodeClient(client=client)
            self.__clientscount += 1
            self.__clientstime += client.getTimeWait()
            if self.__maxtime < client.getTimeWait():
                self.__maxtime = client.getTimeWait()
            if (self.__mintime > client.getTimeWait() or self.__mintime == 0) and client.getTimeWait() != 0:
                self.__mintime = client.getTimeWait()
            self.__attentionclientstime += client.getTransactions().getTime()
            return True

        nodeaux=self.__first
        while nodeaux.getNext():
            if nodeaux.getClient().getDpi() == client.getDpi():
                print(Fore.RED + f'El DPI {client.getDpi()} ya existe en la lista')
                return False
            nodeaux = nodeaux.getNext()
        if nodeaux.getClient().getDpi() == client.getDpi():
            print(Fore.RED + f'El DPI {client.getDpi()} ya existe en la lista')
            return False
        nodeaux.setNext(NodeClient(client=client))
        self.__clientscount += 1
        self.__clientstime += client.getTimeWait()
        if self.__maxtime < client.getTimeWait():
            self.__maxtime = client.getTimeWait()
        if (self.__mintime > client.getTimeWait() or self.__mintime == 0) and client.getTimeWait() != 0:
            self.__mintime = client.getTimeWait()
        self.__attentionclientstime += client.getTransactions().getTime()
        return True

    def delete(self):
        
        if self.__first.getClient().getDpi() == None:
            print(Fore.RED + 'No existe ningun cliente en la cola')
            return False

        deletenode = self.__first
        if deletenode.getNext() == None:
            self.__first = NodeClient()
            self.__clientscount -= 1
            return deletenode
        else:
            self.__first = self.__first.getNext()
            deletenode.setNext(None)
            return deletenode

    def getTime(self):
        if self.__first.getClient().getName() == None:
            return 0
        
        nodeaux = self.__first
        time = 0
        while nodeaux:
            time += nodeaux.getClient().getTransactions().getTime()
            nodeaux = nodeaux.getNext()
        return time

    def getClientsNum(self):
        if self.__first.getClient().getName() == None:
            return 0
        
        nodeaux = self.__first
        num = 0
        while nodeaux:
            num += 1
            nodeaux = nodeaux.getNext()
        return num

    def getAvgTimeWait(self, timedesk=0):
        if self.__clientscount != 0:
            return (self.__clientstime+timedesk)/self.__clientscount
        else:
            return 0
    
    def getMinTimeWait(self, timedesk=0):
        if self.__first.getClient().getDpi() is not None:
            return self.__mintime+timedesk
        else:
            return self.__mintime

    def getMaxTimeWait(self, timedesk=0):
        if self.__first.getClient().getDpi() is not None:
            return self.__maxtime+timedesk
        else:
            return self.__maxtime
