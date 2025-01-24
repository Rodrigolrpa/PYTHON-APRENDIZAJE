class Persona:
    
    def __init__(self, nombre, edad):
        self.__nombre = nombre #atributo privado
        self.__edad = edad
    
    def obtener_nombre(self):
        return self.__nombre
    

persona1 = Persona('Rodrigo', 34)
print(persona1.obtener_nombre())
    
