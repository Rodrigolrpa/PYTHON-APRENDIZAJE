'''              EJERCICIO NUMERO #49
SIMULAR UN LANZAMIENTO DE DADO HASTA OBTENER UN 6
'''
#Se importan las librerias os para limpiar pantalla
#random para generar un numero random con parametros
#time para poner un temporizador para pausar la ejecucion del codigo
import os
import random
import time

while True:

    print('-----------MENU-----------')
    print('Lanzar dado: [1]')
    print('Salir [5]')
    opcion = input('Inserte una opcion: ')

    if opcion == '1':
        while True:
            os.system('cls')
            print("---LANZANDO DADO---")
            moneda = random.randint(1, 6)
            time.sleep(2)  # Pausa el programa por 2 segundos

            if moneda == 1:
                print('Salio 1.')
                time.sleep(1)  # Pausa el programa por 1 segundos

            elif moneda == 2:
                print('Salio 2')
                time.sleep(1)

            elif moneda == 3:
                print('Salio 3')
                time.sleep(1)

            elif moneda == 4:
                print('Salio 4')
                time.sleep(1)

            elif moneda == 5:
                print('Salio 5')
                time.sleep(1)

            else:
                print('FELICIDADES SALIO 6')
                time.sleep(1)
                break
    

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