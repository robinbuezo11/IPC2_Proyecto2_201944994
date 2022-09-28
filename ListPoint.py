from NodePoint import NodePoint

class ListPoint:
    def __init__(self):
        self.__first = NodePoint()

    def getFirst(self):
        return self.__first

    def setFirst(self, first = NodePoint()):
        self.__first = first