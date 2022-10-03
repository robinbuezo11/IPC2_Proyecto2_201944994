from Client import Client


class ServiceDesk:
    def __init__(self, code=None, id=None, manager=None, active=False, client=Client()):
        self.__code = code
        self.__id = id
        self.__manager = manager
        self.__active = active
        self.__client = client

    def getCode(self):
        return self.__code
    
    def getId(self):
        return self.__id
    
    def getManager(self):
        return self.__manager

    def getActive(self):
        return self.__active

    def getClient(self):
        return self.__client

    def setId(self, id):
        self.__id = id

    def setManager(self, manager):
        self.__manager = manager

    def setActive(self, active):
        self.__active = active

    def setClient(self, client=Client()):
        self.__client = client