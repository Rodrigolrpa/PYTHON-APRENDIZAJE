'''       EJERCICIO NUMERO #56
LISTAR 10 NUMEROS Y CALCULAR EL CUADRADO DE 
CADA UN O E IMPRIMIRLOS UTILIZANDO FOR
'''
lista = []
lista_cuadrado = []
tamanio = int(input('Ingrese el tamaño de la lista: '))

for i in range(tamanio):
    lista.append(int(input(f'Ingrese el elemento {i+1}: ')))
    lista_cuadrado.append(lista[i] ** 2)

print(lista)
print(lista_cuadrado)