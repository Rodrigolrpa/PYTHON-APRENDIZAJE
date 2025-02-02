'''                         EJERCICIO NUMERO #32
 PIDE UN NUMERO Y COMPRUEBA SI EL NUMERO ES PAR O IMPAR UTILIZANDO IF Y MODULO
'''
#el modulo es el residuo de una division 
# 6%2= 0 5%2=1 si cualquier modulo de cualquier
#numero es igual a 0 entonces es divisible sobre
#ese numero
numero = int(input('Ingresa un numero: '))
if numero % 2:
    print('Tu numero es impar', numero)
else:
    print('Tu numero es par', numero)