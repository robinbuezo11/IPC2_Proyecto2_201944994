from NodeClient import NodeClient

class ListClient:
    def __init__(self):
        self.__first = NodeClient()

    def getFirst(self):
        return self.__first

    def setFirst(self, first = NodeClient()):
        self.__first = first