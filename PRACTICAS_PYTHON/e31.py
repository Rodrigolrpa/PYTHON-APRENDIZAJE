'''                         EJERCICIO NUMERO #31
            PIDE UN NUMERO Y VERIFICA SI ES POSITIVO, NEGATIVO O 0
'''
numero = float(input('Ingrese un numero: '))
if numero == 0:
    print(f'El numero ingresado es 0')
elif numero > 0:
    print(f'El numero ingresado es positivo: {numero}')
else:
    print(f'El numero ingresado en negativo: {numero}')