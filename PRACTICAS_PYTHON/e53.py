'''        EJERCICIO NUMERO #53
IMPRIMIR LOS ELEMENTOS DE UNA LISTA DADA
'''
print('FORMA #2 CON FOR')
lista = []
tamanio = int(input('Ingrese el tamaño de la lista: '))
for i in range(tamanio):
    elemento = input('Ingrese un elemento a la lista: ')
    lista.append(elemento)

print(lista)
print('FORMA #2 CON WHILE')
j = 1
lista = []
while j <= tamanio:
    elemento = input('Ingrese un elemento a la lista: ')
    lista.append(elemento)
    j += 1

print(lista)

