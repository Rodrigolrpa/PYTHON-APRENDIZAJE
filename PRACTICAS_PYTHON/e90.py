'''                  EJERCICIO NUMERO #90
DUPLICAR CADA ELEMENTO DE UNA LISTA USANDO MAP Y LAMBDA'''


numeros = [1,2,3,4,5]

duplicados = list(map(lambda x : x * 2, numeros))

print(numeros)
print(duplicados)