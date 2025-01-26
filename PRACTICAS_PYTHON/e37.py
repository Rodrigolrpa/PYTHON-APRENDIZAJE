'''                 EJERCICIO NUMERO #35
            CALCULA EL MAXIMO DE TRES NUMEROS.
'''

a = float(input('Ingresa un numero: '))
b = float(input('Ingresa un numero: '))
c = float(input('Ingresa un numero: '))
#FORMA 1
#a es igual a b e igual a c
if a == b == c:
    print('Los numeros son iguales')
elif b > a and b > c:
    print('El segundo numero es el mayor:', b)
elif a > b and a > c:
    print('El primer numero es el mayor:', a)
else:
    print('El tercer numero es el mayor:', c)

#FORMA 2
maximo = max(a,b,c)
print('El numero maximo es:', maximo)





