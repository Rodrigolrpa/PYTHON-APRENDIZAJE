'''                         EJERCICIO NUMERO #38
            DETERMINA SI UN NUMERO ES DIVISIBLE ENTRE 5 Y 7
'''
numero = float(input('Ingresa un numero: '))
#FORMA ORIGINAL DE RESOLVER EL PROBLEMA 
if numero % 5 == numero % 7 == 0:
    print('Es divisible entre 5 y 7')
else:
    print(f'{numero} no es divisible por 5 y 7')
#PROBLEMA A RESOLVER UNICAMENTE SI QUIERES SABER SI ES DIVISIBLE
#POR % O POR 7
if numero % 5 == 0:
    print(f'{numero} es divisible por 5')
else:
    print(f'{numero} no es divisible por 5')

if numero % 7 == 0:
    print(f'{numero} es divisible por 7')
else:
    print(f'{numero} no es divisible por 7')

#FORMA 2
for divisor in [5, 7]:
    if numero % divisor == 0:
        print(f'{numero} es divisible por {divisor}')
    else:
        print(f'{numero} no es divisible por {divisor}')
