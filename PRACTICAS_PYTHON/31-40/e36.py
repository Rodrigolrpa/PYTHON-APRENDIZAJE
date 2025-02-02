'''                    EJERCICIO NUMERO #35
            PIDE UN CARACTER Y DETERMINA SI ES VOCAL
'''
caracter = input('Ingresa un caracter: ')
caracter1 = caracter.upper()
if caracter1 == 'A' or caracter1 =='E' or caracter1 =='O' or caracter1 =='U' or caracter1 =='I':
    print(f'Tu caracter es una vocal: {caracter}')
else:
    print(f'Tu caracter es una consonante: {caracter}')

#Forma 2
if caracter1 in ('A', 'E', 'I', 'O', 'U'):
    print("Es una vocal mayúscula")
