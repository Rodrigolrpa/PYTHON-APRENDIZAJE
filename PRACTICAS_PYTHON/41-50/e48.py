'''            EJERCICIO NUMERO #48
SIMULAR UN VOLADO O LANZAMIENTO DE UNA MONEDA
'''
#Se importan las librerias os para limpiar pantalla
#random para generar un numero random con parametros
#time para poner un temporizador para pausar la ejecucion del codigo
import os
import random
import time
while True:

    print('-----------MENU-----------')
    print('Lanzar moneda: [1]')
    print('Salir [5]')
    opcion = input('Inserte una opcion: ')
    if opcion == '1':
        os.system('cls')
        print("---LANZANDO MONEDA---")
        moneda = random.randint(1,2)
        time.sleep(2)  # Pausa el programa por 2 segundos
        if moneda == 1:
            print('Felicidades es Sello.')
        else:
            print('Felicidades es Aguila')
        time.sleep(2)  # Pausa el programa por 2 segundos

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