'''                  EJERCICIO NUMERO #45
IMPRIME LA TABLA DE MULTIPLICAR DE UN NUMERO INGRESADO POR EL USUARIO
'''
numero = int(input('Ingresa un numero: '))
#Itera de 0 a 10 y i va tomando los valores de 0 a 10
for i in range(0, 11):
    print(f'{numero} X {i} = {i * numero}')