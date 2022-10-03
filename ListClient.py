from colorama import Fore
from Client import Client
from NodeClient import NodeClient

class ListClient:
    def __init__(self):
        self.__first = NodeClient()
        self.__clientscount = 1

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
        return True

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

    def getAvgTimeInLine(self):
        if self.__first.getClient().getName() == None:
            return 0
        
        nodeaux = self.__first
        time=0
        num = 0
        while nodeaux:
            time += nodeaux.getClient().getTimeWait()
            num += 1
            nodeaux = nodeaux.getNext()
        return time/num

    def getMaxTimeInLine(self):
        if self.__first.getClient().getName() == None:
            return 0
        
        nodeaux = self.__first
        time=0
        while nodeaux:
            if nodeaux.getClient().getTimeWait()>time:
                time = nodeaux.getClient().getTimeWait()
            nodeaux = nodeaux.getNext()
        return time

    def getMinTimeInLine(self):
        if self.__first.getClient().getName() == None:
            return 0
        
        nodeaux = self.__first
        time=nodeaux.getClient().getTimeWait()
        while nodeaux:
            if nodeaux.getClient().getTimeWait()<time:
                time = nodeaux.getClient().getTimeWait()
            nodeaux = nodeaux.getNext()
        return time