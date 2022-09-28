from NodeTransaction import NodeTransaction

class ListTransaction:
    def __init__(self):
        self.__first = NodeTransaction()

    def getFirst(self):
        return self.__first

    def setFirst(self, first = NodeTransaction()):
        self.__first = first