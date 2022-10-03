from ListTransaction import ListTransaction

class Client:
    def __init__(self, dpi=None, name=None, transactions = ListTransaction(), timewait=0):
        self.__dpi = dpi
        self.__name = name
        self.__transactions = transactions
        self.__timewait = timewait

    def getDpi(self):
        return self.__dpi

    def getName(self):
        return self.__name

    def getTransactions(self):
        return self.__transactions

    def getTimeWait(self):
        return self.__timewait

    def setName(self, name):
        self.__name = name
    
    def setTransactions(self, transactions):
        self.__transactions = transactions

    def setTimeWait(self, timewait):
        self.__timewait = timewait