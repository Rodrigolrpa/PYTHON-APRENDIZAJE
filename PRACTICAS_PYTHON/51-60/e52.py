'''      EJERCICIO NUMERO #52
SUMAR LOS NUMEROS DEL 1 AL 10 CON FOR
'''

numero = int(input('Ingrese un numero entero: '))
suma = 0
print('FORMA #2 CON FOR')
for i in range (1, numero + 1):
    suma = suma + i

print(suma)

print('FORMA #2 CON WHILE')
j = 1
suma = 0
while j <= numero:
    suma = suma + j
    j += 1

print(suma)