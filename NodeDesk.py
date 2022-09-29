from ServiceDesk import ServiceDesk

class NodeDesk:
    def __init__(self, desk = ServiceDesk(), next = None):
        self.__desk = desk
        self.__next = next

    def getDesk(self):
        return self.__desk

    def getNext(self):
        return self.__next

    def setNext(self, next):
        self.__next = next