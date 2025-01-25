'''                         EJERCICIO NUMERO #2
                CALCULA EL AREA DE UN CIRCULO CON UN RADIO DADO.
'''

#Importacion de la libreria math para hacer uso del valor "pi".
import math

#Captura del radio que lo convierte de string por default a float en una variable llamada radio. 
radio = float(input('Ingrese el radio del circulo: '))

#Calculo del area del circulo haciendo uso la libreria math.
area_circulo = math.pi * radio ** 2

#Se muestra en pantalla el area del circulo con el radio dado anteriormente.
print(f'El area del circulo de radio: {radio} es: {area_circulo}')