from colorama import Fore
from Config import Config
from ListEnterprise import ListEnterprise
from ListTransaction import ListTransaction
from NodeConfig import NodeConfig

class ListConfig:
    def __init__(self):
        self.__first = NodeConfig()

    def getFirst(self):
        return self.__first

    def setFirst(self, first = NodeConfig()):
        self.__first = first

    def insert(self, config = Config()):
        
        if self.__first.getConfig().getCode() == None:
            self.__first = NodeConfig(config=config)
            return True

        nodeaux=self.__first
        while nodeaux.getNext():
            if nodeaux.getConfig().getCode() == config.getCode():
                print(Fore.RED + f'La configuración {config.getCode()} ya existe en la lista')
                return False
            nodeaux = nodeaux.getNext()
        if nodeaux.getConfig().getCode() == config.getCode():
            print(Fore.RED + f'La configuración {config.getCode()} ya existe en la lista')
            return False
        nodeaux.setNext(NodeConfig(config=config))
        return True

    def applyConfig(self, enterprises=ListEnterprise()):
        nodeconfig=self.__first

        while nodeconfig:
            applied = False
            nodeenterprise=enterprises.getFirst()
            while nodeenterprise and not applied:
                if nodeconfig.getConfig().getCodEmpresa() == nodeenterprise.getEnterprise().getCode():
                    nodepoint = nodeenterprise.getEnterprise().getPoints().getFirst()
                    applied = True
                    appliedpoint = False
                    while nodepoint and not appliedpoint:
                        if nodeconfig.getConfig().getCodPunto() == nodepoint.getPoint().getCode():
                            configdesk = nodeconfig.getConfig().getDesks().getFirst()
                            appliedpoint = True
                            print(Fore.WHITE + f'\nConfigurando empresa: {nodeconfig.getConfig().getCodEmpresa()}, punto: {nodeconfig.getConfig().getCodPunto()}')
                            while configdesk:
                                applieddesk = False
                                nodedesk = nodepoint.getPoint().getDesks().getFirst()
                                while nodedesk and not applieddesk:
                                    if configdesk.getDesk().getCode() == nodedesk.getDesk().getCode():
                                        nodepoint.getPoint().getDesks().setActive(nodepoint.getPoint().getDesks().getActive()+1)
                                        nodedesk.getDesk().setActive(True)
                                        nodedesk.getDesk().setActiveNum(nodepoint.getPoint().getDesks().getActive())
                                        applieddesk = True
                                    nodedesk = nodedesk.getNext()
                                if not applieddesk:
                                    print(Fore.RED + f'El escritorio {configdesk.getDesk().getCode()} no existe.')
                                configdesk = configdesk.getNext()
                            clientconfig = nodeconfig.getConfig().getClients().getFirst()
                            while clientconfig:
                                validclient = True
                                print(Fore.WHITE + f'Revisando al cliente {clientconfig.getClient().getName()}, DPI {clientconfig.getClient().getDpi()}')
                                transconfig = clientconfig.getClient().getTransactions().getFirst()
                                transactionconfig = ListTransaction()
                                while transconfig:
                                    validtrans = False
                                    nodetrans = nodeenterprise.getEnterprise().getTransactions().getFirst()
                                    while nodetrans and not validtrans:
                                        if transconfig.getTransaction().getCode() == nodetrans.getTransaction().getCode():
                                            validtrans = True
                                            print(Fore.CYAN + f'Transacción {transconfig.getTransaction().getCode()} aceptada.')
                                            transconfig.getTransaction().setName(nodetrans.getTransaction().getName())
                                            transconfig.getTransaction().setTime(nodetrans.getTransaction().getTime())
                                            transactionconfig.insert(transaction=transconfig.getTransaction())
                                        nodetrans = nodetrans.getNext()
                                    if not validtrans:
                                        print(Fore.RED + f'La transacción {transconfig.getTransaction().getCode()} no está disponible.')
                                        validclient = False
                                    transconfig = transconfig.getNext()
                                clientconfig.getClient().setTransactions(transactions=transactionconfig)
                                if validclient:
                                    nodepoint.getPoint().getClients().insert(clientconfig.getClient())
                                    print(Fore.CYAN + 'Cliente agregado correctamente')
                                    nodepoint.getPoint().callClient()
                                clientconfig = clientconfig.getNext()
                        nodepoint = nodepoint.getNext()
                    if not appliedpoint:
                        print(Fore.RED + f'El punto {nodeconfig.getConfig().getCodPunto()} no existe.')
                nodeenterprise = nodeenterprise.getNext()
            if not applied:
                print(Fore.RED + f'La empresa {nodeconfig.getConfig().getCodEmpresa()} no existe.')
            else:
                print(Fore.GREEN + 'Empresa configurada correctamente')
            nodeconfig = nodeconfig.getNext()