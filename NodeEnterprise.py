from Enterprise import Enterprise

class NodeEnterprise:
    def __init__(self, enterprise = Enterprise(), next = None):
        self.__enterprise = enterprise
        self.__next = next

    def getEnterprise(self):
        return self.__enterprise

    def getNext(self):
        return self.__next

    def setNext(self, next):
        self.__next = next