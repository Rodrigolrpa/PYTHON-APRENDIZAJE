'''                  EJERCICIO NUMERO #94
FILTRAR CADENAS QUE CONTIENEN UN CARACTER ESPECIFICO USANDO FILTER'''

cadenas = ['Hola', 'Esto', 'Es', 'Una', 'Lista', 'De', 'Palabras']

r = list(filter(lambda x : 'E' in x, cadenas))

print(r)