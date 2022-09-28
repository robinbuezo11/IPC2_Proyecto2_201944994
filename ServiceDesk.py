class ServiceDesk:
    def __init__(self, code=None, id=None, manager=None):
        self.__code = code
        self.__id = id
        self.__manager = manager

    def getCode(self):
        return self.__code
    
    def getId(self):
        return self.__id
    
    def getManager(self):
        return self.__manager

    def setId(self, id):
        self.__id = id

    def setManager(self, manager):
        self.__manager = manager