class Transaction:
    def __init__(self, code=None, name=None, time=None, quantity=None):
        self.__code = code
        self.__name = name
        self.__time = time
        self.__quantity = quantity

    def getCode(self):
        return self.__code

    def getTime(self):
        return self.__time

    def getName(self):
        return self.__name

    def getQuantity(self):
        return self.__quantity

    def setName(self, name):
        self.__name = name
    
    def setTime(self, time):
        self.__time = time

    def setQuantity(self, quantity):
        self.__quantity = quantity
