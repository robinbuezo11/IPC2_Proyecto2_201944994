from colorama import Fore
from ListEnterprise import ListEnterprise

def main():
    
    enterprises = ListEnterprise()
    
    option = 0
    while option != 9:
        print(Fore.BLUE + '\n------------------MENU------------------')
        print(Fore.BLUE + '1) ')
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

main()