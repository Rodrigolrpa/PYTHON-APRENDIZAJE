class Persona:
    #setters y getters (setters creacion de atributos y getters obtencion de atributos)
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def set_edad(self, edad):
        self.edad = edad
    
    def get_nombre(self):
        return self.nombre
    
    def get_edad(self):
        return self.edad
    
    #metodos
    def saludar(self):
        print(f'Hola que tal {self.nombre} tu edad es: {self.edad}')
#Creacion del objeto persona1 de la clase persona
persona1 = Persona()
#Llamado al metodo set_nombre con su parametro
persona1.set_nombre('Rodrigo')
#Llamado al metodo set_edad con su parametro
persona1.set_edad(23)
#Llamado al metodo saludar 
persona1.saludar()
#Se muestra en terminal el objeto creado en forma de dicionario
print(persona1.__dict__)