#Diccionarios
diccionario1 = {
    "Clave1" : 1,
    "Clave2" : 2,
    "Clave3" : 'Hola',
    "nombre" : 'Facultad'
}
#Imprimir el diccionario
print(diccionario1)

#Imprimir un valor del diccionario
print(diccionario1["nombre"])

#Modificar un valor del diccionario
diccionario1['Clave1'] = 'Autodidacta'
print(diccionario1["Clave1"])

#Agregar un nuevo elemento
diccionario1['clave5'] = 'Hola mundo'
print(diccionario1)