'''                  EJERCICIO NUMERO #72
CREAR UNA CLASE CIRCULO CON LOS SIGUIENTES ATRIBUTOS:
<> RADIO: RADIO DEL CIRCULO
LA CLASE DEBE TENER LOS SIGUIENTES METODOSl 
<>__INIT__(SELF, RADIO) : INICIALIZA LOS ATRIBUTOS DE LA CLASE
<>CALCULAR_AREA(SELF) : CALCULA Y DEVUELVE EL AREA DEL CIRCULO
<>CALCULAR_PERIMETRO(SELF) : CALCULA Y DEVUELVE EL PERIMETRO DEL CIRCULO'''

import math
class Circulo:
    
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        area = math.pi * self.radio ** 2
        return area
    
    def calcular_perimetro(self):
        perimetro =  2 * math.pi * self.radio
        return(perimetro)

radio = float(input('Ingrese el radio del circulo: '))
circulo = Circulo(radio)
print(circulo.calcular_area(), 'Unidades cuadradas')
print(circulo.calcular_perimetro(), 'Unidades')
