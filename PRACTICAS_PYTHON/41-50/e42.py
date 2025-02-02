'''                 EJERCICIO NUMERO #42
            SOLICITA AL USUARIO INGRESAR UN NUMERO
N Y LUEGO IMPRIME LA SUMA DE TODOS LOS NUMEROS DESDE 1 HASTA N
            
'''
#FORMA 1
n = int(input('Ingrese un numero entero: '))
suma = 0
for i in range(n):
    suma = suma + i + 1
    #print(i+1)
print('La suma es', suma)
#FORMA 2
suma = 0
i = 1
while i <= n:
    suma += i
    i += 1
print('La suma es', suma)
    