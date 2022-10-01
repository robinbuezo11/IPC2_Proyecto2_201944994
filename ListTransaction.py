from colorama import Fore
from NodeTransaction import NodeTransaction
from Transaction import Transaction

class ListTransaction:
    def __init__(self):
        self.__first = NodeTransaction()

    def getFirst(self):
        return self.__first

    def setFirst(self, first = NodeTransaction()):
        self.__first = first

    def insert(self, transaction = Transaction()):
        
        if self.__first.getTransaction().getCode() == None:
            self.__first = NodeTransaction(transaction=transaction)
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
        return True