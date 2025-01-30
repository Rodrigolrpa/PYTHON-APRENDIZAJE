'''                  EJERCICIO NUMERO #77
CREAR UNA CLASE LLAMADA PERSONA.
*CON LOS ATRIBUTOS: NOMBRE Y EDAD:
*LOS SETTERS Y GETTERS
PARA CADA UNO DE LOS ATRIBUTOS.
*MOSTRAR(): MUESTRA LOS DATOS DE LA PERSONA.
*ESMAYOREDEEDAD(): DEVUELVE UN VALOR LOGICO INDICANDO
SI ES MAYOR DE EDAD'''

class Persona:

    def __init__(self, nombre=None, edad=None):

        self._nombre = nombre
        self._edad = edad
    
    @property
    def nombre(self):
        return self._nombre 
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
    
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, nueva_edad):
        self.edad = nueva_edad

    def mostrar(self):
        print(self.__dict__)
    
    def mayor_edad(self):
        if self._edad >= 18:
            return True
        
        else:
            return False

persona1 = Persona('Rodrigo', 23)
print(persona1.mayor_edad())
persona1.mostrar()


