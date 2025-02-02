'''                  EJERCICIO NUMERO #96
CREAR UN EXCEPCION QUE ME AYUDA A DETERNMINAR SI EL INDICE DE UNA LISTA
ESTA FUERA DE RANGO'''

my_lista = [1,2,3]

try:
    print(my_lista[5])

except IndexError:
    print('Error, el indice no existe')