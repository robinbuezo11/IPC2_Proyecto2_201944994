from Transaction import Transaction

class NodeTransaction:
    def __init__(self, transaction = Transaction(), next = None):
        self.__transaction = transaction
        self.__next = next

    def getTransaction(self):
        return self.__transaction

    def getNext(self):
        return self.__next

    def setNext(self, next):
        self.__next = next