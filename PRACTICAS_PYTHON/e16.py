'''                         EJERCICIO NUMERO #16
CALCULA 2 ELEVADO A LA POTENCIA 4 SIN UTILIZAR EL OPERADOR **'''

#FORMA 1
print('----------------FORMA 1----------------')
dos = 2
potencia_cuatro = 2 * 2 * 2 *2
print(potencia_cuatro)

#FORMA 2
print('----------------FORMA 2----------------')
numero_entero = int(input('Ingrese un numero entero: '))
potencia_numero = int(input('Ingrese el numero de la potencia: '))
resultado = 0
for i in range(numero_entero):
    while i <= potencia_numero:
        i += 1
        resultado = numero_entero * numero_entero
print(f'El numero ingresado {numero_entero} a la potencia: {potencia_numero} es: {resultado}')