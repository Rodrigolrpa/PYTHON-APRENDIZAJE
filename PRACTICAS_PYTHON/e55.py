'''              EJERCICIO NUMERO #55
IMPRIMIR LOS NUMEROS PARES DEL 2 AL 10 CON EL CICLO FOR
'''
num_final = int(input('Ingrese un numero entero: '))

print('FORMA #1 CON FOR') 
for i in range(2, num_final + 2, 2):
    print(i)


print('FORMA #2 CON WHILE')
j = 2
while j<= num_final:
    print(j)
    j += 2
