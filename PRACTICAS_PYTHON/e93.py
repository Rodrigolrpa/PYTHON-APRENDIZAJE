'''                  EJERCICIO NUMERO #93
FILTRAR NUMEROS NEGATIVOS DE UNA LISTA UTILIZANDO FILTER'''

lista = [1,2,3,4,0,-1,-2,-3,-5]

r = list(filter(lambda x : x < 0, lista))

print(r)