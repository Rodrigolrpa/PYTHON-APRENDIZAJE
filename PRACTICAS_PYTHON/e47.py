'''                  EJERCICIO NUMERO #47
HACER UN MENU DE OPCIONES QUE INCLUYA LA OPCION DE SALIR DEL PROGRAMA
'''
#la libreria os nos ayuda a usar el comando os.system('cls') para limpiar pantalla
import os
while True:

    print('-----------MENU-----------')
    print('Opcion 1: [1]')
    print('Limpiar terminal: [2]')
    print('Salir [5]')
    opcion = input('Inserte una opcion: ')
    if opcion == '1':
        os.system('cls')
        print("Elegiste opcion 1")

    elif opcion == '2':
        os.system('cls')

    elif opcion == '5':
        os.system('cls')
        opcion = input('Elegiste salir estas seguro? [s] si, [n] no: ')

        if opcion == 's':
            break

        else:
            os.system('cls')
            continue

    else:
        print('Opcion no valida')