'''                         EJERCICIO NUMERO #29
                COMBINA DOS LISTAS EN PARES USANDO LA FUNCION ZIP()
'''

'''
Hacer pares en dos listas significa combinar elementos 
correspondientes de ambas listas para formar pares 
(habitualmente representados como tuplas). En este 
proceso, cada elemento 
de la primera lista se empareja con el elemento en 
la misma posición de la segunda lista.'''

lista1 = [1,2,3]
lista2 = ['a', 'b', 'c']
pares = list(zip(lista1, lista2))
print(pares)