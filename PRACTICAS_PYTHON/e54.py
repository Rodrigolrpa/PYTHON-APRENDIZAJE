'''                  EJERCICIO NUMERO #45
IMPRIMIR LOS CARACTERES DE UNA CADENA UTILIZANDO EL CICLO FOR
'''

cadena = input('Ingrese una cadena: ')
print('FORMA #2 CON FOR') 
for caracter in cadena:
    print(caracter)

print('FORMA #2 CON WHILE')
j = 0
while j < len(cadena):
    print(cadena[j])
    j += 1