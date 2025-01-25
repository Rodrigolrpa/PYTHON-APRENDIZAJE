'''Creacion de la clase padre Figura la cual 
va a heredar sus atributos y metodos a sus hijos
Rectangulo y Circulo'''
class Figura:
    #constructor que inicializa la variable color
    def __init__(self, color):
        self_color = color
    #Metodo el cual sera heredado para sus hijos y sera usado ahi, pass es por default
    def area(self):
        pass

    def saludo_padre(self):
        print('Tu padre es soy yo: Figura')

'''Clase hija que hereda de su padre Figura teniendo como
metodos nuevos (area) y declarando nuevos atributos como base y altura'''
class Rectangulo(Figura):
    #se hace uso de super(). para acceder a un metodo o construtor heredado
    def __init__(self, color, base, altura):
        super().__init__(color)
        self.base = base 
        self.altura = altura
#Calculo del area haciendo uso de un metodo heredado de Figura
    def area(self):
        super().saludo_padre()
        return self.base * self.altura

'''Clase hija del padre Figura'''
class Circulo(Figura):

    def __init__(self, color, radio):
        super().__init__(color)
        self.radio = radio

#Importacion de la libreria math para acceder a la variable pi
    def area(self):
        import math
        return math.pi * self.radio ** 2

#Creacion de un objetos de las clases Rectangulo y Circulo con sus parametros
rectangulo = Rectangulo('Naranja', 4, 6)
print(f'El area del rectangulo es {rectangulo.area()}')
circulo = Circulo('Morado', 2.45)
print(f'El area del circulo es {circulo.area()}')