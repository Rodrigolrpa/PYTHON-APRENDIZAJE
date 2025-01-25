'''                     EJERCICIO DE JOSE 
        #PROBLEMA 1 MOSTRAR NUMEROS DEL 1 AL 15 NO IMPORTA COMO
        #PROBLEMA 2 DADO UN NUMERO ENTERO IMPRIMIR DESDE EL 0 HASTA EL 
        NUMERO DADO PERO UNICAMENTE PARES.
'''
#PROBLEMA 1
for i in range(15):
    print(i+1)

#PROBLEMA 2
numero = int(input('Ingrese un numero: '))
for i in range(numero+1):
    if(i%2 == 0):
        print(i)

#PROBLEMA DIFERENTE FORMA
'''range(0, numero + 1, 2):

range() genera una secuencia de números según los parámetros que se le den:
El primer valor (0) es el número de inicio de la secuencia (el bucle comenzará desde 0).
El segundo valor (numero + 1) es el número hasta el cual se generarán los números. 
Se usa numero + 1 porque range() genera números hasta el valor dado, pero no lo incluye, 
por lo que si ingresas 5, el rango será de 0 a 5.
El tercer valor (2) es el paso de la secuencia. Esto quiere decir que el bucle avanzará 
de dos en dos, generando solo los números pares.
Entonces, si el usuario ingresa, por ejemplo, 10, el range(0, 10 + 1, 2) generará los 
números 0, 2, 4, 6, 8, 10.
'''
numero = int(input('Ingrese un numero: '))
for i in range(0, numero + 1, 2):
    print(i)
