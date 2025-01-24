#Para crear una clase usamos class
class Persona:
    #Metodo constructor
    def __init__(self, nombre, edad):
        #Para poder crear atributos utilizamos self
        self.nombre = nombre
        self.edad = edad
    
    #Metodo para saludar
    def saludar(self):
        print('Hola', self.nombre)

    #Metodo para decir tu edad
    def mostrar_edad(self):
        print('Tu edad es:', self.edad)

    #Metodo para saber si eres mayor de edad
    def eres_mayor_edad(self):
        if self.edad >= 18:
            print('Eres mayor de edad', self.nombre)
            return True
        else:
            print('No eres mayor de edad', self.edad)
            return False
    
    #Metodo que hace el llamado a los demas metodos
    
    def llamar_otros(self):
        self.saludar()
        self.mostrar_edad()
        self.eres_mayor_edad()

#Creacion del objeto Persona con sus parametros requeridos de los atributos
objeto_persona = Persona('Rodrigo', 18)
#Llamado al metodo saludar
objeto_persona.saludar()
#Llamado al metodo mostrar_edad
objeto_persona.mostrar_edad()
#Llamado al metodo eres_mayor_edad
mayor_si_no = objeto_persona.eres_mayor_edad()
print(mayor_si_no)

#Llamado al metodo llamar_otros (Esta linea de codigo resume las 5 lineas de codigo anterior)
objeto_persona.llamar_otros()