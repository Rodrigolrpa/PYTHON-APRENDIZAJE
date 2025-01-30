'''                  EJERCICIO NUMERO #83
CALCULAR LA LONGITUD DE UNA LISTA DE PALABRAS UTILIZANDO MAP'''

def longitud(lista):
    return len(lista)

lista_palabras = ['Hola', 'Esto', 'Es', 'Una', 'Lista', 'De', 'Palabras']
longitud = list(map(longitud, lista_palabras))

print(longitud)