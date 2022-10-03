from colorama import Fore
from NodeDesk import NodeDesk
from ServiceDesk import ServiceDesk

class StackDesk:
    def __init__(self):
        self.__first = NodeDesk()

    def getFirst(self):
        return self.__first

    def setFirst(self, first = NodeDesk()):
        self.__first = first

    def stack(self, desk = ServiceDesk()):
        stackdesk = NodeDesk(desk=desk)

        nodeaux = self.__first
        while nodeaux:
            if nodeaux.getDesk().getCode() == desk.getCode():
                print(Fore.RED + f'El escritorio {desk.getCode()} ya existe en la lista')
                return False
            nodeaux = nodeaux.getNext()

        if self.__first.getDesk().getCode() == None:
            self.__first = stackdesk
        else:
            stackdesk.setNext(self.__first)
            self.__first = stackdesk
        return True

    def unstack(self):
        if self.__first.getDesk().getCode() == None:
            print(Fore.RED + 'No existe ningún escritorio')
            return

        unstackdesk = self.__first
        if self.__first.getNext():
            self.__first = self.__first.getNext()
        else:
            self.__first = NodeDesk()
        unstackdesk.setNext(None)
        return unstackdesk

    def getActiveDesks(self):
        if self.__first.getDesk().getCode() == None:
            return 0
        
        nodeaux = self.__first
        num = 0
        while nodeaux:
            if nodeaux.getDesk().getActive() == True:
                num += 1
            nodeaux = nodeaux.getNext()
        return num