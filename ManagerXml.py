from colorama import Fore
import xml.etree.ElementTree as et
from AttentionPoint import AttentionPoint
from Enterprise import Enterprise
from Client import Client
from ListClient import ListClient
from ListTransaction import ListTransaction
from ServiceDesk import ServiceDesk
from ListEnterprise import ListEnterprise
from ListPoint import ListPoint
from StackDesk import StackDesk
from Transaction import Transaction
from ListConfig import ListConfig
from Config import Config

class ManagerXml():
    def __init__(self):
        pass

    def readEnterprises(self, path, enterprises = ListEnterprise()):
        tree = et.parse(path)
        root = tree.getroot()
        try:
            for itrenterprise in root:
                enterprise = Enterprise(code=itrenterprise.attrib['id'])
                for dataenterprise in itrenterprise:
                    if dataenterprise.tag == 'nombre':
                        enterprise.setName(dataenterprise.text)
                    elif dataenterprise.tag == 'abreviatura':
                        enterprise.setShorName(dataenterprise.text)
                    elif dataenterprise.tag == 'listaPuntosAtencion':
                        points = ListPoint()
                        for itrpoint in dataenterprise:
                            point = AttentionPoint(code=itrpoint.attrib['id'])
                            for datapoint in itrpoint:
                                if datapoint.tag == 'nombre':
                                    point.setName(datapoint.text)
                                elif datapoint.tag == 'direccion':
                                    point.setAddress(datapoint.text)
                                elif datapoint.tag == 'listaEscritorios':
                                    desks = StackDesk()
                                    for itrdesk in datapoint:
                                        desk = ServiceDesk(code=itrdesk.attrib['id'])
                                        for datadesk in itrdesk:
                                            if datadesk.tag == 'identificacion':
                                                desk.setId(datadesk.text)
                                            if datadesk.tag == 'encargado':
                                                desk.setManager(datadesk.text)
                                        desks.stack(desk=desk)
                                    point.setDesks(desks=desks)
                            points.insert(point=point)
                        enterprise.setPoints(points=points)
                    elif dataenterprise.tag == 'listaTransacciones':
                        transactions = ListTransaction()
                        for itrtransaction in dataenterprise:
                            transaction = Transaction(code=itrtransaction.attrib['id'])
                            for datatransaction in itrtransaction:
                                if datatransaction.tag == 'nombre':
                                    transaction.setName(datatransaction.text)
                                elif datatransaction.tag == 'tiempoAtencion':
                                    transaction.setTime(int(datatransaction.text))
                            transactions.insert(transaction=transaction)
                        enterprise.setTransactions(transactions=transactions)
                enterprises.insert(enterprise=enterprise)
            print(Fore.GREEN + 'XML cargado exitosamente')
            return enterprises
        except Exception as e:
            print(Fore.RED + f'{e}')
    def readConfigs(self, path, configs = ListConfig()):
        tree = et.parse(path)
        root = tree.getroot()
        try:
            for itrconfig in root:
                config = Config(code=itrconfig.attrib['id'], codempresa=itrconfig.attrib['idEmpresa'], codpunto=itrconfig.attrib['idPunto'])
                for dataconfig in itrconfig:
                    if dataconfig.tag == 'escritoriosActivos':
                        desks = StackDesk()
                        for itrdesk in dataconfig:
                            desks.stack(ServiceDesk(code=itrdesk.attrib['idEscritorio']))
                        config.setDesks(desks=desks)
                    elif dataconfig.tag == 'listadoClientes':
                        clients = ListClient()
                        for itrclient in dataconfig:
                            client = Client(dpi=itrclient.attrib['dpi'])
                            for dataclient in itrclient:
                                if dataclient.tag == 'nombre':
                                    client.setName(dataclient.text)
                                elif dataclient.tag == 'listadoTransacciones':
                                    transactions = ListTransaction()
                                    for itrtransaction in dataclient:
                                        transactions.insert(Transaction(code=itrtransaction.attrib['idTransaccion'], quantity=int(itrtransaction.attrib['cantidad'])))
                                    client.setTransactions(transactions=transactions)
                                    client.setTimeWait(clients.getTime())
                            clients.insert(client=client)
                        config.setClients(clients=clients)
                configs.insert(config=config)
            print(Fore.GREEN + 'XML cargado exitosamente')
            return configs
        except Exception as e:
            print(Fore.RED + f'{e}')

