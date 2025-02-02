'''                         EJERCICIO NUMERO #19
        CUENTA LAS OCURRENCIAS DE UN CARACTER EN ESPECIFICO EN UNA CADENA.
'''
#FORMA 1.
#Manera basica y simple de resolverlo 
print('----------------FORMA 1----------------')
cadena = input('Ingrese una palabra: ')
caracter = input('Ingrese un caracter: ')
contador_caracter = 0
#letra toma el valor de cada caracter que va recorriendo desde el inicio
for letra in cadena:
    #la letra en que va el ciclo es igual al caracter ingresado?
    if letra == caracter:
        contador_caracter = contador_caracter + 1
#si el contador es mayor de 0 quiere decir que hubo incidencias 
if contador_caracter > 0:
    print(f'El numero de veces que se repite el caracter: {caracter} es de: {contador_caracter}.')
else:
    print(f'El caracter {caracter} no se repitio ninguna vez.')

#FORMA 2.
#Manera basica y simple de resolverlo 
print('----------------FORMA 2----------------')

cadena1 = 'programacion'
ocurrencias = cadena1.count('a')
print('ocurrencias', ocurrencias)