'''                         EJERCICIO NUMERO #24
                ELIMINA UN ELEMENTO ESPECIFICO DE UNA LISTA
'''
#Una lista puede almacenar cualquiero tipo de dato
#se hace uso del metodo remove(dato a eleminar) lo cual
#elimina la primer incidencia que encuentre.
lista = [1,2.4, True, False, 'A', 'HOla', 0, 0, 0]
lista.remove(0)
print('Resultado:', lista)

#si se quiere eliminar todas las incidencias se puede hacer uso de un ciclo
mi_lista = [1,2.4, True, False, 'A', 'HOla', 0, 0, 0]
while 0 in mi_lista:
    mi_lista.remove(0)
print(mi_lista)
