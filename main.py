from colorama import Fore
from ListConfig import ListConfig
from ListEnterprise import ListEnterprise
from ManagerXml import ManagerXml

def main():
    
    xml = ManagerXml()
    enterprises = ListEnterprise()
    configs = ListConfig()
    
    option = 0
    while option != 9:
        print(Fore.BLUE + '\n------------------MENU------------------')
        print(Fore.BLUE + '1) Cargar XML')
        print(Fore.BLUE + '2) ')
        print(Fore.BLUE + '3) ')
        print(Fore.BLUE + '9) SALIR\n')
        
        try:
            textin = input(Fore.YELLOW + "Ingrese el numero de la opción que desee ")
            if textin != '':
                option = int(textin)
            else:
                option = 0
        except Exception as e:
            print(Fore.RED + f'{e}')

        if option == 1:
            
            optionxml = 0
            while optionxml != 9:
                print(Fore.BLUE + '\n1) Empresa')
                print(Fore.BLUE + '2) Configuración')
                print(Fore.BLUE + '9) SALIR\n')

                try:
                    textinxml = input(Fore.YELLOW + "Ingrese el numero del XML que desee cargar ")
                    if textinxml != '':
                        optionxml = int(textinxml)
                    else:
                        optionxml = 0
                except Exception as e:
                    print(Fore.RED + f'{e}')

                if optionxml == 1:
                    try:
                        path = input(Fore.YELLOW + "Ingrese la ruta del archivo: ")
                        enterprises = xml.readEnterprises(path=path,enterprises=enterprises)
                    except Exception as e:
                        print(Fore.RED + f'{e}')
                elif optionxml == 2:
                    try:
                        path = input(Fore.YELLOW + "Ingrese la ruta del archivo: ")
                        configs = xml.readConfigs(path=path,configs=configs)
                    except Exception as e:
                        print(Fore.RED + f'{e}')
main()