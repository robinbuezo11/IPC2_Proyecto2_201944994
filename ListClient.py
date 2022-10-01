from colorama import Fore
from Client import Client
from NodeClient import NodeClient

class ListClient:
    def __init__(self):
        self.__first = NodeClient()

    def getFirst(self):
        return self.__first

    def setFirst(self, first = NodeClient()):
        self.__first = first

    def insert(self, client = Client()):
        
        if self.__first.getClient().getDpi() == None:
            self.__first = NodeClient(client=client)
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
        return True