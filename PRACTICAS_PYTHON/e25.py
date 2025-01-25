'''                         EJERCICIO NUMERO #25
               GENERA UNA LISTA DE NUMEROS DEL 1 AL 200
'''
#FORMA 1 usando ciclo for y el metodo append() para asignar numeros a la lista de 1 en 1
tamanio_lista = int(input('Ingresa el tamaño de la lista: '))
lista = []
for i in range(tamanio_lista):
    i +=1
    lista.append(i)
print(lista)

#FORMA 2 hacinedo uso de la funcion list(rango(inico, fin(sin tomar en cuenta)))
numeros = list(range(1, 201))
print(numeros)