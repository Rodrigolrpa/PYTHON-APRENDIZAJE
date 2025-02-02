'''                  EJERCICIO NUMERO #91
FILTRAR NUMERO PARES DE UNA LISTA UTILIZANDO FILTER'''

numeros = [1,2,3,4,5,6,7,8]

pares = list(filter(lambda x : x % 2 == 0, numeros))

print(pares)