from lib2to3.pytree import Node
from NodeDesk import NodeDesk

class StackDesk:
    def __init__(self):
        self.__first = NodeDesk()

    def getFirst(self):
        return self.__first

    def setFirst(self, first = NodeDesk()):
        self.__first = first