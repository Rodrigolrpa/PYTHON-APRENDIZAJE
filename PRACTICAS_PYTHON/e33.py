'''                         EJERCICIO NUMERO #33
            DETERMINA SI UN AÑO ES BISIESTO
            REGLA DE NEGOCIO
                - DIVISIBLE POR 4.
                - NO DIVISIBLE POR 100
                - DIVISIBLE POR 400
'''
'''Aquí está la aclaración:

Si el año es divisible por 4, pero tambien ,
es divisible por 100 , entonces 
debe ser divisible también por 400 para ser bisiesto.
Entonces, para que un año sea bisiesto, 
debe cumplir una de estas situaciones:

Es divisible por 4 y no es divisible por 100.
O es divisible por 4, divisible por 100 y 
también divisible por 400.
No es necesario que se cumplan las tres 
condiciones en todos los casos, pero sí alguna de estas 
combinaciones.'''
anio = int(input('Ingrese el año: '))
if (anio % 100 != 0 and anio % 400 == 0) or anio % 4 == 0  :
    print('Es bisiesto')
else:
    print('No es bisiesto')