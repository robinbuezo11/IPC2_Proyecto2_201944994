from ListTransaction import ListTransaction

class Client:
    def __init__(self, dpi=None, name=None, transactions = ListTransaction()):
        self.__dpi = dpi
        self.__name = name
        self.__transactions = transactions

    def getDpi(self):
        return self.__dpi

    def getName(self):
        return self.__name

    def getTransactions(self):
        return self.__transactions

    def setName(self, name):
        self.__name = name
    
    def setTransactions(self, transactions):
        self.__transactions = transactions