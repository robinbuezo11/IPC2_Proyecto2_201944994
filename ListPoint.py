from colorama import Fore
from AttentionPoint import AttentionPoint
from NodePoint import NodePoint

class ListPoint:
    def __init__(self):
        self.__first = NodePoint()

    def getFirst(self):
        return self.__first

    def setFirst(self, first = NodePoint()):
        self.__first = first

    def insert(self, point = AttentionPoint()):
        
        if self.__first.getPoint().getCode() == None:
            self.__first = NodePoint(point=point)
            return True

        nodeaux=self.__first
        while nodeaux.getNext():
            if nodeaux.getPoint().getCode() == point.getCode():
                print(Fore.RED + f'El punto {point.getCode()} ya existe en la lista')
                return False
            nodeaux = nodeaux.getNext()
        if nodeaux.getPoint().getCode() == point.getCode():
            print(Fore.RED + f'El punto {point.getCode()} ya existe en la lista')
            return False
        nodeaux.setNext(NodePoint(point=point))
        return True