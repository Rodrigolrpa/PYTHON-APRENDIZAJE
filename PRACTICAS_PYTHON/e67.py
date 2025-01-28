'''                   EJERCICIO NUMERO #67
ESCRIBE UNA FUNCION PARA CALCULAR EL VOLUMEN DE UN CILINDRO
''' 
import math

def volumen_cilindro(radio, altura):
    volumen = math.pi * radio ** 2 * altura
    return volumen

r = float(input('Ingrese el radio del cilindro: '))
a = float(input('Ingrese la altura del cilindro: '))

print(f'El volumen es: {volumen_cilindro(r,a)} unidades cubicas.')