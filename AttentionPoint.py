from StackDesk import StackDesk

class AttentionPoint:
    def __init__(self, code=None, name=None, address=None, desks = StackDesk()):
        self.__code = code
        self.__name = name
        self.__address = address
        self.__desks = desks
    
    def getCode(self):
        return self.__code
    
    def getName(self):
        return self.__name

    def getAddress(self):
        return self.__address
    
    def getDesks(self):
        return self.__desks
    
    def setName(self, name):
        self.__name = name

    def setAddress(self, address):
        self.__address = address

    def setDesks(self, desks = StackDesk()):
        self.__desks = desks