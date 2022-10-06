from Client import Client

class NodeClient:
    def __init__(self, client = Client(), next = None):
        self.__client = client
        self.__next = next

    def getClient(self):
        return self.__client

    def getNext(self):
        return self.__next

    def setNext(self, next):
        self.__next = next
        