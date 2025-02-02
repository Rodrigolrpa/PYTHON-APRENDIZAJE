'''                         EJERCICIO NUMERO #30
                        ELIMINA DUPLICADOS EN UNA LISTA
'''
'''
set(list1):

Convierte la lista list1 en un conjunto (set).
Los conjuntos en Python no permiten elementos duplicados, por lo que cualquier duplicado en list1 será automáticamente eliminado.
list(set(list1)):

Después de crear el conjunto con set(list1), 
este conjunto (sin duplicados) se convierte
nuevamente en una lista utilizando la función list(). 
Esto es necesario 
porque un conjunto no tiene un orden definido 
ni admite indexación como las listas.'''
list1 = [1, 1, 1, 2, 2, 3, 4, 5, 5, 5]
sin_duplicados = list(set(list1))
print(sin_duplicados)
