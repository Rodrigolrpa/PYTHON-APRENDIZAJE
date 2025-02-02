'''                  EJERCICIO NUMERO #71
CREAR UNA CLASE RECTANGULO CON LOS SIGUIENTES ATRIBUTOSñ
BASE : BASE DEL RECTANGULO
ALTURA : ALTURA DEL RECTANGULO
LA CLASE DEBE TENER LOS SIGUIENTES METODOS:
<> __INIT__(SELF, BASE, ALTURA: INICIALIZA LOS ATRIBUTOS
DE LA CLASE.
<>CALCULAR_AREA(SELF: CALCULA Y DEVUELVE EL AREA DEL RECTANGULO
<>CALCULAR_PERIMETRO(SELF): CALCULA Y DEVUELVE EL PERIMETRO DEL RECTANGULO.))'''

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        area = self.base * self.altura
        return area
    
    def calcular_perimetro(self):
        perimetro = 2 * (self.base * self.altura)
        return perimetro

rectangulo = Rectangulo(2,4)

print(rectangulo.calcular_area())
print(rectangulo.calcular_perimetro())