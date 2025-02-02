'''                         EJERCICIO NUMERO #15
                ORDENA UNA LISTA DE NUMEROS DE MENOR A MAYOR.
'''
#Declaracion de la lista  de numeros.
lista_numeros = [1, 5, 8, 3, 9, 4, 6]
print(lista_numeros)

#Se hace uso de la funcion sort().
'''
    FUNCIONAMIENTO DEL ALGORITMO SORT

División en sublistas pequeñas:

Divide la lista en partes más pequeñas (runs) que ya estén ordenadas o casi ordenadas.
Ordenamiento de cada sublista:

Utiliza Insertion Sort en estas pequeñas porciones para ordenarlas rápidamente.
Fusión de sublistas:

Combina (merge) las sublistas usando un enfoque similar a Merge Sort para crear una lista totalmente ordenada.'''

lista_numeros.sort()
print(lista_numeros)
