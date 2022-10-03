import os

from colorama import Fore
from StackDesk import StackDesk
from ListClient import ListClient

class AttentionPoint:
    def __init__(self, code=None, name=None, address=None, desks = StackDesk(), clients=ListClient()):
        self.__code = code
        self.__name = name
        self.__address = address
        self.__desks = desks
        self.__clients = clients
    
    def getCode(self):
        return self.__code
    
    def getName(self):
        return self.__name

    def getAddress(self):
        return self.__address
    
    def getDesks(self):
        return self.__desks

    def getClients(self):
        return self.__clients
    
    def setName(self, name):
        self.__name = name

    def setAddress(self, address):
        self.__address = address

    def setDesks(self, desks = StackDesk()):
        self.__desks = desks

    def setClients(self, clients = ListClient()):
        self.__clients = clients

    def toStringWithoutDesks(self):
        return f'Código: {self.__code},     Nombre: {self.__name},      Dirección: {self.__address}'

    def graphStatusPoint(self):
        text = 'digraph {fontname="Helventica,Arial,sans-serif" edge[dir=back] subgraph cluster0{fontsize=30 node[shape=plain style=filled pencolor="#00000" color="aqua" fontname="Helvetica,Arial,sans-serif"]'
        relation = ''
        contador = self.__clients.getClientsCount()-self.__clients.getClientsNum()

        if self.__clients.getFirst().getClient().getDpi() == None:
            text += 'Client[label=<<table cellspacing="0" cellpadding="20"><tr><td><b>Cola vacia</b></td></tr></table>>] label=<<b>Clientes</b>>}'
        else:
            nodeaux=self.__clients.getFirst()

            while nodeaux:
                if nodeaux.getNext():
                    transactions=nodeaux.getClient().getTransactions().toString().replace("\n","<br/>")
                    text += f'Client{contador}[label=<<table cellspacing="0" cellpadding="25"><tr><td><b>Número {contador}</b></td></tr>'
                    text += f'<tr><td>{nodeaux.getClient().getName()}<br/>DPI: {nodeaux.getClient().getDpi()}<br/>{transactions}Tiempo de Atencion: {nodeaux.getClient().getTransactions().getTime()}<br/>Tiempo en Cola: {nodeaux.getClient().getTimeWait()}</td></tr></table>>]'
                    relation += f'Client{contador}->'
                    nodeaux=nodeaux.getNext()
                    contador+=1
                else:
                    transactions=nodeaux.getClient().getTransactions().toString().replace("\n","<br/>")
                    text += f'Client{contador}[label=<<table cellspacing="0" cellpadding="25"><tr><td><b>Numero {contador}</b></td></tr>'
                    text += f'<tr><td>{nodeaux.getClient().getName()}<br/>DPI: {nodeaux.getClient().getDpi()}<br/>{transactions}Tiempo de Atencion: {nodeaux.getClient().getTransactions().getTime()}<br/>Tiempo en Cola: {nodeaux.getClient().getTimeWait()}</td></tr></table>>]'
                    relation += f'Client{contador}'
                    nodeaux=nodeaux.getNext()
                    contador+=1
            text+=relation
            text+=' label=<<b>Clientes</b>>}'
        text+=' subgraph cluster1{fontsize=30 node[shape=plain style=filled pencolor="#00000" fontname="Helvetica,Arial,sans-serif"]'
        if self.__desks.getFirst().getDesk().getCode() == None:
            text += 'Desk[label=<<table cellspacing="0" cellpadding="20"><tr><td><b>Sin escritorios</b></td></tr></table>>] label=<<b>Clientes</b>>}'
        else:
            nodeaux=self.__desks.getFirst()

            while nodeaux:
                text += f'Desk{nodeaux.getDesk().getCode()}['
                if nodeaux.getDesk().getActive() == True:  
                    text += f'color="springgreen" label=<<table cellspacing="0" cellpadding="20"><tr><td><b>Escritorio {nodeaux.getDesk().getCode()}</b></td></tr>'
                else:
                    text += f'label=<<table cellspacing="0" cellpadding="20"><tr><td><b>Escritorio {nodeaux.getDesk().getCode()}</b></td></tr>'
                text += f'<tr><td>ID: {nodeaux.getDesk().getId()}<br/>Encargado: {nodeaux.getDesk().getManager()}<br/>Cliente: {nodeaux.getDesk().getClient().getName()}<br/>DPI: {nodeaux.getDesk().getClient().getDpi()}</td></tr></table>>]'
                nodeaux=nodeaux.getNext()
            text+=' label=<<b>Escritorios</b>>}'
        text+='}'
        file = open("./estado.dot","w+")
        file.write(text)
        file.close()
        os.system(f'dot -Tpng estado.dot -o estado.png')
        print(Fore.GREEN + 'Estado creado correctamente')