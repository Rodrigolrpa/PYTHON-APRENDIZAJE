#todo lo que se capture sera de tipo string
nombre = input('Ingresa tu nombre: ')
print(nombre)

resultado = 0
a = 0
b= 3

#covirtiendo la captura de datos en entero para trabajar con entero
a = int(input('escribe un numero: '))
resultado = a + b
print(resultado)

a = float(input('Escribe un numero decimal'))
b = 5.5
resultado = a + b
print(resultado)
print('El resultado es: ', resultado)
'''
la concatenacion es unicamente en cadenas de texto y se usa el +
cuando utilizas la , se hace uso de la variable tal cual es declarada.
print('El resultado es: ' + resultado)
 
'''
''' cmabio de la variable resultado de tipo float a string 
para realizar la concatenacion con + '''
print('El resultado es: ' + str(resultado)) 

#interpolacion, combinar texto sin usar el signo de +
print(f'El resultado es {resultado}') 