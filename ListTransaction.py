from colorama import Fore
from NodeTransaction import NodeTransaction
from Transaction import Transaction

class ListTransaction:
    def __init__(self):
        self.__first = NodeTransaction()
        self.__time = 0

    def getFirst(self):
        return self.__first

    def setFirst(self, first = NodeTransaction()):
        self.__first = first

    def setTime(self, time):
        self.__time = time

    def insert(self, transaction = Transaction()):
        
        if self.__first.getTransaction().getCode() == None:
            self.__first = NodeTransaction(transaction=transaction)
            self.__time += transaction.getTime() * transaction.getQuantity()
            return True

        nodeaux=self.__first
        while nodeaux.getNext():
            if nodeaux.getTransaction().getCode() == transaction.getCode():
                print(Fore.RED + f'La transacción {transaction.getCode()} ya existe en la lista')
                return False
            nodeaux = nodeaux.getNext()
        if nodeaux.getTransaction().getCode() == transaction.getCode():
            print(Fore.RED + f'La transacción {transaction.getCode()} ya existe en la lista')
            return False
        nodeaux.setNext(NodeTransaction(transaction=transaction))
        self.__time += transaction.getTime() * transaction.getQuantity()
        return True

    def toString(self):
        if self.__first.getTransaction().getCode() == None:
            return Fore.RED + 'No existe ninguna transacción en la lista'
        
        nodeaux = self.__first
        string = ''
        while nodeaux:
            string += nodeaux.getTransaction().toString()
            string += '\n'
            nodeaux = nodeaux.getNext()
        return string

    def getTime(self):
        return self.__time

    def getTransactionByCode(self, code):
        nodeaux = self.__first
        while nodeaux:
            if nodeaux.getTransaction().getCode() == code:
                return nodeaux.getTransaction()
            nodeaux = nodeaux.getNext()
        return Transaction()