from NodeEnterprise import NodeEnterprise

class ListEnterprise:
    def __init__(self):
        self.__first = NodeEnterprise()

    def getFirst(self):
        return self.__first

    def setFirst(self, first = NodeEnterprise()):
        self.__first = first