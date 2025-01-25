'''                         EJERCICIO NUMERO #12
                 CONVIERTE UN NUMERO ENTERO EN CADENA DE TEXTO
'''
#Declaracion de la variable de tipo entero que capturara el valor ingresado.
numero_entero = int(input('Ingrese un numero entero: '))

#Se muestra en pantala el tipo de dato que es la variable anterior.
print('El numero entero es de tipo: ', type(numero_entero))

#Declaracion de la variable de tipo string a la que se le asigna el valor del numero entero.
numero_entero_ct = str(numero_entero)

#Se muestra en pantalla la cadena de texto y el tipo de dato que es.
print('El numero en cadena de texto es de tipo: ', type(numero_entero_ct))
print(f'El numero entero es: {numero_entero} y en cadena de texto es: {numero_entero_ct}')