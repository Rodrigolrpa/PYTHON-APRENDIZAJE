'''                  EJERCICIO NUMERO #84
CALCULAR EL CUADRADO DE LA SUMA DE DOS LISTAS DE NUMEROS
UTILIZANDO MAP'''

def suma(list1, list2):
    return (list1 + list2) ** 2

lista1 = [1,2,3,4]
lista2 = [5,6,7,8]

cuadrado = list(map(suma,lista1,lista2))

print(cuadrado)