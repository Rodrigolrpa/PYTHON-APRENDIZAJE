class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def set_nombre(self, nombre_nuevo):
        self.nombre = nombre_nuevo

    def set_edad(self,edad_nueva):
        self.edad = edad_nueva

    def get_nombre(self):
        return self.nombre
    
    def get_edad(self):
        return self.edad
    

p1 = Persona('Rodrigo', 23)
print(p1.get_nombre())
print(p1.get_edad())

p1.set_edad(30)
print(p1.get_edad())

p1.set_nombre('Luis')
print(p1.get_nombre())