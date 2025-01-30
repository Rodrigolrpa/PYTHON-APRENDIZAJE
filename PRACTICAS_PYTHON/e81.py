'''                  EJERCICIO NUMERO #81
ELEVAR AL CUADRADO UNA LISTA DE NUMIROS UTILIZANDO MAP()'''


def cuadrado(x):
    return x ** 2


numeros = [1,2,3,4,5]
cuadrados = list(map(cuadrado, numeros))

print(numeros)
print(cuadrados)