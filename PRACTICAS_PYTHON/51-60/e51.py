'''       EJERCICIO NUMERO #51
IMPRIMIR LOS NUMEROS DEL 1 AL 5 CON FOR
'''
numero = int(input('Ingrese un numero entero: '))
print('FORMA #2 CON FOR')
for i in range(1, numero + 1):
    print(i)

print('FORMA #2 CON WHILE')
j = 1
while j <= numero:
    print(j)
    j += 1