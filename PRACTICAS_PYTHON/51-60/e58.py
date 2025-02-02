'''       EJERCICIO NUMERO #58
MULTIPLICAR TODOS LOS ELEMENTOS DE UNA LISTA POR 2
'''
lista = []
lista_por_dos = []
tamanio = int(input('Ingrese el tamaño de la lista: '))

for i in range(tamanio):
    lista.append((input(f'Ingrese el elemento {i+1}: ')))
    lista_por_dos.append(lista[i] * 2)

print(lista)
print(lista_por_dos)