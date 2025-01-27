'''            EJERCICIO NUMERO #62
CREA UNA FUNCION PARA CALCULAR EL AREA DE UN CIRCULO
''' 
import math
def area_circulo(radio):
    area = math.pi * (radio ** 2)
    return area

print(area_circulo(float(input('Ingresa el radio del circulo: '))))
