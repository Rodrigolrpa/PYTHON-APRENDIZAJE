'''                  EJERCICIO NUMERO #74
CREAR UNA CLASE PERSONA CON LOS ATRIBUTOS:
*** NOMBRE, EDAD, DNI
CON LOS METODOS:
INIT()
ES_MAYOR_DE_EDAD() ESTE RETORNA TRUE SI ES MAYOR DE EDAD'''

class Persona:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad   = edad
        self.dni = dni
    
    def es_mayor_de_edad(self):

        if self.edad >= 18:
            print(self.nombre, 'eres mayor de edad')
        else:
            print(self.nombre, 'no eres mayor de edad')

persona = Persona('Rodrigo', 17, 190028)
persona.es_mayor_de_edad()