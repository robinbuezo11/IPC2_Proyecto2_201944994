from AttentionPoint import AttentionPoint

class NodePoint:
    def __init__(self, point = AttentionPoint(), next = None):
        self.__point = point
        self.__next = next

    def getPoint(self):
        return self.__point

    def getNext(self):
        return self.__next

    def setNext(self, next):
        self.__next = next