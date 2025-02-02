'''                         EJERCICIO NUMERO #11
        CALCULA EL AREA DE UN RECTANGULO PIDE BASE Y ALTURA AL USUARIO.
'''
#Declaracion de las variables base y altura de tipo float
#para que capturen el dato ingresado de cada una.
base = float(input('Ingrese la base del rectangulo: '))
altura = float(input('Ingrese la altura del rectangulo: '))

#Se muestra en pantalla el area del rectangulo (se hace el caluclo)
#dentro del mismo print().
print(f'Area del rectangulo es: {base * altura}')