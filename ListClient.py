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
            return

        nodeaux=self.__first
        while nodeaux.getNext():
            nodeaux.setNext(nodeaux.getNext())
        nodeaux.setNext(NodeClient(client=client))