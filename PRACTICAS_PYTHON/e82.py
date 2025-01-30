'''                  EJERCICIO NUMERO #82
CONVERTIR UNA LISTA DE CADENAS QUE SEAN NUMEROS A ENTEROS UTILIZANDO MAP'''

def convertir_entero(cadena):
    return int(cadena)

lista = ['1', '2', '3', '4']

enteros = list(map(convertir_entero, lista))
print(lista)
print(enteros)
