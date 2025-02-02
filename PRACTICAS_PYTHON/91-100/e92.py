'''                  EJERCICIO NUMERO #92
FILTRAR CADENAS DE LONGITUD MAYOR QUE 3 DE UNA LISTA,  USANDO FILTER'''

cadenas = ['Hola', 'Esto', 'Es', 'Una', 'Lista', 'De', 'Palabras']

r = list(filter(lambda x : len(x) > 3, cadenas))

print(r)