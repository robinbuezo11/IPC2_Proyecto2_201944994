class ServiceDesk:
    def __init__(self, code=None, id=None, manager=None, active=False):
        self.__code = code
        self.__id = id
        self.__manager = manager
        self.__active = active

    def getCode(self):
        return self.__code
    
    def getId(self):
        return self.__id
    
    def getManager(self):
        return self.__manager

    def getActive(self):
        return self.__active

    def setId(self, id):
        self.__id = id

    def setManager(self, manager):
        self.__manager = manager

    def setActive(self, active):
        self.__active = active