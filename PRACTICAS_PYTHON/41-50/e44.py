'''                EJERCICIO NUMERO #44
            GENERA UN UN NUMERO ALEATORIO ENTRE 1 Y 10.
LUEGO, PIDE AL USUARIO ADIVINAR EL NUMERO HASTA QUE LO HAGA CORRECTAMENTE
'''
import random
# inicializacion de un numero random con la funcion radint(inicio rango, fin rango)
numero_random = random.randint(1, 10)
intentos = 0
numero = 0
while numero != numero_random:
    intentos = intentos + 1
    numero = int(input('Ingrese un numero: '))
    if numero == numero_random:
        print(f'ADIVINASTE EL NUMERO!!! {numero_random} EN {intentos} INTENTO(S).')
        break
