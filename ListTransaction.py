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
            return

        nodeaux=self.__first
        while nodeaux.getNext():
            nodeaux = nodeaux.getNext()
        nodeaux.setNext(NodeTransaction(transaction=transaction))