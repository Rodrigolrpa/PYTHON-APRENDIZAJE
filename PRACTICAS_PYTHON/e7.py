'''                            EJERCICIO NUMERO #7
                    CALCULA EL PROMEDIO DE UNA LISTA DE NUMEROS
'''
#FORMA 1
#Declaracion de una lista vacia
lista_numeros = []
#Declaracion de una variable de tipo entero que guarda la captura
#de los numeros a ingresar.
total_numeros = int(input('Ingrese el total de numeros a ingresar:' ))
#Contadores suma_numero que suma el total de numeros de la lista
# y j que es el contador de numeros de la lista
suma_numero = 0
j = 0
#Ciclo
for i in range(total_numeros):

    numero = float(input('Ingrese el primer numero: '))
    lista_numeros.append(numero)
    suma_numero = suma_numero + numero
    j = j + 1

promedio = suma_numero / j
print(f'La lista de numeros es: {lista_numeros} y el promedio es: {promedio}')

#FORMA 2

'''numeros = [2,4,6,8]
promedio = sum(numeros)/ len(numeros)

print('El promedio es:', promedio)'''