'''                  EJERCICIO NUMERO #75
CREAR UNA CLASE COCHE CON LOS ATRIBUTOS:
MARCA, MODELO, MATRICULA, KM
CON LOS METODOS:
INIT COMO CONSTRUCTOR 
AVANCZAR(KM) ESTE AUENTA EL VALOR DE KM EN LA CANTIDAD'''

class Coche:
    
    def __init__(self, marca, modelo, matricula, km):

        self.marca = marca
        self.modelo = modelo
        self.matricula = matricula
        self.km = km
    
    def avanzar(self, km):
        self.km = self.km + km
    
coche = Coche('Toyota', 'Titan', '001-002', 0)
print(coche.__dict__)
coche.avanzar(20000)
print(coche.__dict__)
        