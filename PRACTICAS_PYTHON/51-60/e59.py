'''                    EJERCICIO NUMERO #59
PEDIR AL USUARIO UN NUMERO E IMPRIMIR LA TRABLA DE MULTIPLICAR DEL MISMO
'''
numero = int(input('Ingrese un numero entero: '))

for i in range(numero+1):
    print(f'{numero} x {i} = {numero * i}.')
    print()
