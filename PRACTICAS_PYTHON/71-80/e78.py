'''                  EJERCICIO NUMERO #78
CREAR UNA CLASE PERSONA Y OTRA CLASE ESTUDIANTE.
LA CLASE PERSONA TIENE EL ATRIBUTO NOMBRE Y EL METODO MOSTRAR_NOMBRE()
LA CLASE ESTUDIANTE DEBE HEREDAR DE LA CLASE PERSONA Y UTILIZAR EL METODO MOSTRAR_NOMBNRE()
DE LA CLASE PERSONA'''

class Persona:

    def __init__(self, nombre):
        self.nombre = nombre
    
    def mostrar_nombre(self):
        print(self.nombre)

class Estudiante(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)
    
    def mostrar(self):
        super().mostrar_nombre()
    
estudiante1 = Estudiante('Rodrigo')
estudiante1.mostrar_nombre()