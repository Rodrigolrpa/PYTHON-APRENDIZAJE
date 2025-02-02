'''                      EJERCICIO NUMERO #16
        CALCULA 2 ELEVADO A LA POTENCIA 4 SIN UTILIZAR EL OPERADOR **
'''

#FORMA 1.
#Manera basica y simple de resolverlo 
print('----------------FORMA 1----------------')
dos = 2
potencia_cuatro = 2 * 2 * 2 * 2
print(potencia_cuatro)

#FORMA 2.
#Haciendo uso de ciclo while y un poco mas agradable al usuario
print('----------------FORMA 2----------------')
numero_entero = int(input('Ingrese un numero entero: '))
potencia_numero = int(input('Ingrese el numero de la potencia: '))
resultado = 1
i = 0
while i < potencia_numero:
    i += 1
    resultado = resultado * numero_entero
print(f'El numero ingresado {numero_entero} a la potencia: {potencia_numero} es: {resultado}')

#FORMA 3.
#Haciendo uso de la funcion pow((base), (potencia))
print('----------------FORMA 3----------------')

respuesta =  pow(2, 4)
print('Res =',respuesta)
