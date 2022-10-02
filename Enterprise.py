from ListPoint import ListPoint
from ListTransaction import ListTransaction

class Enterprise:
    def __init__(self, code=None, name=None, shortname=None, points = ListPoint(), transactions = ListTransaction()):
        self.__code = code
        self.__name = name
        self.__shortname = shortname
        self.__points = points
        self.__transactions = transactions

    def getCode(self):
        return self.__code
    
    def getName(self):
        return self.__name

    def getShorName(self):
        return self.__shortname

    def getPoints(self):
        return self.__points
    
    def getTransactions(self):
        return self.__transactions

    def setName(self, name):
        self.__name = name

    def setShorName(self, shortname):
        self.__shortname = shortname

    def setPoints(self, points = ListPoint):
        self.__points = points

    def setTransactions(self, transactions = ListTransaction()):
        self.__transactions = transactions

    def toStringWithoutPoints(self):
        return f'Código: {self.__code},     Nombre: {self.__name},      Abreviatura: {self.__shortname}'