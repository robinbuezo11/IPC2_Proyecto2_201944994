from colorama import Fore
from NodeDesk import NodeDesk
from ServiceDesk import ServiceDesk

class StackDesk:
    def __init__(self):
        self.__first = NodeDesk()
        self.__active = 0

    def getFirst(self):
        return self.__first

    def getActive(self):
        return self.__active

    def setActive(self, active):
        self.__active = active

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

    def getDesactiveDesks(self):
        if self.__first.getDesk().getCode() == None:
            return 0
        
        nodeaux = self.__first
        num = 0
        while nodeaux:
            if nodeaux.getDesk().getActive() == False:
                num += 1
            nodeaux = nodeaux.getNext()
        return num

    def toString(self):
        if self.__first.getDesk().getCode() == None:
            return Fore.RED + 'No existe ninguna empresa en la lista'
        
        nodeaux = self.__first
        string = ''
        while nodeaux:
            if nodeaux.getDesk().getActive() == True:
                string += nodeaux.getDesk().toString()
                string += '\n'
            nodeaux = nodeaux.getNext()
        return string

    def activeDesk(self):
        if self.__first.getDesk().getCode() == None:
            print(Fore.RED + 'No existe ningun escritorio en la lista')
            return False

        nodeaux = self.__first
        while nodeaux:
            if nodeaux.getDesk().getActive() == False:
                self.__active += 1
                nodeaux.getDesk().setActive(True)
                nodeaux.getDesk().setActiveNum(self.__active)
                print(Fore.GREEN + f'Escritorio {nodeaux.getDesk().getCode()} activado')
                return True
            nodeaux = nodeaux.getNext()
        print(Fore.RED + 'Todos los escritorios ya se encuentran activos')
        return False

    def desactiveDesk(self):
        if self.__active == 0:
            print(Fore.RED + 'No hay ningun escritorio activo')
            return False

        nodeaux = self.__first
        while nodeaux:
            if nodeaux.getDesk().getActiveNum() == self.__active:
                nodeaux.getDesk().setActive(False)
                print(Fore.GREEN + f'Escritorio {nodeaux.getDesk().getCode()} desactivado')
                nodeaux.getDesk().setActiveNum(None)
                self.__active -= 1
                return True
            nodeaux = nodeaux.getNext()

    def getMinClientTime(self):
        if self.__first.getDesk().getCode() == None:
            return False

        nodeaux = self.__first
        min = None
        while nodeaux:
            if nodeaux.getDesk().getClient().getDpi() is not None and min is None:
                min = nodeaux.getDesk().getClient().getTransactions().getTime()
            elif nodeaux.getDesk().getClient().getDpi() is not None and min is not None:
                if min > nodeaux.getDesk().getClient().getTransactions().getTime():
                    min = nodeaux.getDesk().getClient().getTransactions().getTime()
            nodeaux = nodeaux.getNext()
        if min is None:
            return False
        else:
            return min

    def getDesksWithClient(self):
        if self.__first.getDesk().getCode() == None:
            return 0
        
        nodeaux = self.__first
        num = 0
        while nodeaux:
            if nodeaux.getDesk().getClient().getDpi() is not None:
                num += 1
            nodeaux = nodeaux.getNext()
        return num

    def getMinAttentionTime(self):
        if self.__first.getDesk().getCode() == None:
            return 0
        
        nodeaux = self.__first
        min = 0
        while nodeaux:
            if min > nodeaux.getDesk().getAttentionMinTime() or min == 0:
                min = nodeaux.getDesk().getAttentionMinTime()
            nodeaux = nodeaux.getNext()
        return min

    def getMaxAttentionTime(self):
        if self.__first.getDesk().getCode() == None:
            return 0
        
        nodeaux = self.__first
        max = 0
        while nodeaux:
            if max > nodeaux.getDesk().getAttentionMinTime() or max == 0:
                max = nodeaux.getDesk().getAttentionMinTime()
            nodeaux = nodeaux.getNext()
        return max

    def getAvgAttentionTime(self):
        if self.__first.getDesk().getCode() == None:
            return 0
        
        nodeaux = self.__first
        time = 0
        clients = 0
        while nodeaux:
            time += nodeaux.getDesk().getAttentionsClientsTime()
            clients += nodeaux.getDesk().getClientsCount()
            nodeaux = nodeaux.getNext()
        if clients != 0:
            return time/clients
        else:
            return 0