from colorama import Fore
from AttentionPoint import AttentionPoint
from Enterprise import Enterprise
from ListConfig import ListConfig
from ListEnterprise import ListEnterprise
from ListPoint import ListPoint
from ListTransaction import ListTransaction
from ManagerXml import ManagerXml
from ServiceDesk import ServiceDesk
from StackDesk import StackDesk
from Transaction import Transaction

def main():
    
    xml = ManagerXml()
    enterprises = ListEnterprise()
    configs = ListConfig()
    testenterprise = Enterprise()
    testpoint = AttentionPoint()
    
    try:
        option = 0
        while option != 9:
            print(Fore.BLUE + '\n------------------MENU------------------')
            print(Fore.BLUE + '1) Configuración de Empresas')
            print(Fore.BLUE + '2) Selección de Empresa y Punto de Atención')
            print(Fore.BLUE + '3) Manejo de Puntos de Atención')
            print(Fore.BLUE + '9) SALIR\n')
        
            textin = input(Fore.YELLOW + "Ingrese el numero de la opción que desee ")
            if textin != '' and str.isdigit(textin):
                option = int(textin)
            else:
                option = 0

            if option == 1:
                optionxml = 0
                while optionxml != 9:
                    print(Fore.BLUE + '\n1) Limpiar sistema')
                    print(Fore.BLUE + '2) Cargar archivo con los datos del sistema')
                    print(Fore.BLUE + '3) Crear nueva empresa')
                    print(Fore.BLUE + '4) Cargar archivo de configuración inicial')
                    print(Fore.BLUE + '9) SALIR\n')

                    textinxml = input(Fore.YELLOW + "Ingrese el numero de la opción que desee ")
                    if textinxml != '' and str.isdigit(textinxml):
                        optionxml = int(textinxml)
                    else:
                        optionxml = 0

                    if optionxml == 1:
                        enterprises = ListEnterprise()
                        configs = ListConfig()
                        print(Fore.GREEN + '\nLimpieza del sistema realizada con exito')
                    elif optionxml == 2:
                        path = input(Fore.YELLOW + "\nIngrese la ruta del archivo: ")
                        enterprises = xml.readEnterprises(path=path,enterprises=enterprises)
                    elif optionxml == 3:
                        dataenterprise = input(Fore.YELLOW + "\nIngrese los datos de la empresa con el formato 'id,nombre,abreviatura' ")
                        dataenterprise = dataenterprise.split(',')
                        points = ListPoint()
                        transactions = ListTransaction()
                        if len(dataenterprise) == 3:  
                            exitpoint = 0
                            while exitpoint != 9:
                                datapoint = input(Fore.YELLOW + "\n\tIngrese los datos del punto con el formato 'id,nombre,dirección' o '9' para CONFIRMAR ")
                                if datapoint == '9':
                                    exitpoint = 9
                                else:
                                    datapoint = datapoint.split(',')
                                    desks = StackDesk()
                                    if len(datapoint) == 3:
                                        exitdesk = 0
                                        while exitdesk != 9:
                                            datadesk = input(Fore.YELLOW + "\n\t\tIngrese los datos del escritorio con el formato 'id,identificación,encargado' o '9' para CONFIRMAR ")
                                            if datadesk == '9':
                                                exitdesk = 9
                                            else:
                                                datadesk = datadesk.split(',')
                                                if len(datadesk) == 3:
                                                    desk = ServiceDesk(code=datadesk[0].strip(), id=datadesk[1].strip(), manager=datadesk[2].strip())
                                                    if desks.stack(desk=desk):
                                                        print(Fore.GREEN + '\t\tEscritorio agregado exitosamente')
                                                else:
                                                    print(Fore.RED + '\t\tLa cantidad de parametros ingresados no es la correcta')
                                        point = AttentionPoint(code=datapoint[0].strip(), name=datapoint[1].strip(), address=datapoint[2].strip(), desks=desks)
                                        if points.insert(point=point):
                                            print(Fore.GREEN + '\tPunto agregado exitosamente')
                                    else:
                                        print(Fore.RED + '\tLa cantidad de parametros ingresados no es la correcta')
                            exittrans = 0
                            while exittrans != 9:
                                datatrans = input(Fore.YELLOW + "\n\tIngrese los datos de la transacción con el formato 'id,nombre,tiempo' o '9' para CONFIRMAR ")
                                if datatrans == '9':
                                    exittrans = 9
                                else:
                                    datatrans = datatrans.split(',')
                                    if len(datatrans) == 3 and datatrans[2].strip() != '':
                                        transaction = Transaction(code=datadesk[0].strip(), name=datadesk[1].strip(), time=int(datadesk[2].strip()))
                                        if transactions.insert(transaction=transaction):
                                            print(Fore.GREEN + '\tTransacción agregada exitosamente')
                                    else:
                                        print(Fore.RED + '\tLa cantidad de parametros ingresados no es la correcta')
                            enterprise = Enterprise(code=dataenterprise[0].strip(), name=dataenterprise[1].strip(), shortname=dataenterprise[2].strip, points=points, transactions=transactions)
                            if enterprises.insert(enterprise=enterprise):
                                print(Fore.GREEN + 'Empresa agregada exitosamente')
                        else:
                            print(Fore.RED + 'La cantidad de parametros ingresados no es la correcta')
                    elif optionxml == 4:
                        path = input(Fore.YELLOW + "\nIngrese la ruta del archivo: ")
                        configs = xml.readConfigs(path=path,configs=configs)
                        configs.applyConfig(enterprises)
            elif option == 2:
                optionenterprise = 0
                while optionenterprise != 'Regresar':
                    print(Fore.CYAN + '\n------------------EMPRESAS------------------')
                    print(enterprises.toString())
                    optionenterprise = input(Fore.YELLOW + "\nIngrese código de la empresa que desee o 'Regresar' para REGRESAR ")
                    if optionenterprise != 'Regresar':
                        testenterprise = enterprises.getEnterpriseByCode(optionenterprise)
                        if testenterprise.getCode() != None:
                            optionpoint = 0
                            while optionpoint != 'Regresar':
                                print(Fore.CYAN + '\n------------------PUNTOS------------------')
                                print(testenterprise.getPoints().toString())
                                optionpoint = input(Fore.YELLOW + "\nIngrese código del punto que desee o 'Regresar' para REGRESAR ")
                                if optionpoint != 'Regresar':
                                    testpoint = testenterprise.getPoints().getPointByCode(optionpoint)
                                    if testpoint.getCode() != None:
                                        print(Fore.GREEN + 'Selección completada correctamente')
                                        print(Fore.CYAN + '\n------------------SELECCION------------------')
                                        print(testenterprise.toStringWithoutPoints())
                                        print(testpoint.toStringWithoutDesks())
                                        optionpoint = 'Regresar'
                                        optionenterprise = 'Regresar'
                                    else:
                                        print(Fore.RED + 'El código del punto ingresado no existe dentro de la lista')
                        else: 
                            print(Fore.RED + 'El código de empresa ingresado no existe dentro de la lista')
            elif option == 3:
                optionmanager = 0
                while optionmanager != 9:
                    print(Fore.BLUE + '\n1) Ver estado del punto de atención')
                    print(Fore.BLUE + '2) Activar escritorio de servicio')
                    print(Fore.BLUE + '3) Desactivar escritorio de servicio')
                    print(Fore.BLUE + '4) Atender cliente')
                    print(Fore.BLUE + '5) Solicitud de atención')
                    print(Fore.BLUE + '6) Simular actividad del punto de atención')
                    print(Fore.BLUE + '9) SALIR\n')

                    textinmanager = input(Fore.YELLOW + "Ingrese el numero de la opción que desee ")
                    if textinmanager != '' and str.isdigit(textinmanager):
                        optionmanager = int(textinmanager)
                    else:
                        optionmanager = 0

                    if optionmanager == 1:
                        if testpoint.getCode() != None:
                            testpoint.graphStatusPoint()
                            print(Fore.WHITE + 'Punto de atencion:')
                            print(Fore.MAGENTA + f'Escritorios activos: {testpoint.getDesks().getActiveDesks()}\nEscritorios inactivos: {testpoint.getDesks().getDesactiveDesks()}')
                            print(f'Clientes en espera: {testpoint.getClients().getClientsNum()}\nTiempo promedio de espera: {testpoint.getClients().getAvgTimeWait()}')
                            print(f'Tiempo maximo de espera: {testpoint.getClients().getMaxTimeWait()}\nTiempo minimo de espera: {testpoint.getClients().getMinTimeWait()}')
                            print(f'Tiempo promedio de atencion: {testpoint.getClients().getAvgAttentionTime()}\nTiempo maximo de atencion: {testpoint.getClients().getMaxAttentionTime()}')
                            print(f'Tiempo minimo de atencion: {testpoint.getClients().getMinAttentionTime()}')
                            print(testpoint.getDesks().toString())
                        else:
                            print(Fore.RED + 'No se ha seleccionado ningún punto')
    except Exception as e:
            print(Fore.RED + f'{e}')
main()