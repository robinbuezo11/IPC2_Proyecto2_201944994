class Transaction:
    def __init__(self, code=None, name=None, time=None):
        self.__code = code
        self.__name = name
        self.__time = time

    def getCode(self):
        return self.__code

    def getTime(self):
        return self.__time

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name
    
    def setTime(self, time):
        self.__time = time
