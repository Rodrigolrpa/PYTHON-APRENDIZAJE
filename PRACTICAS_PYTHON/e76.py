'''                  EJERCICIO NUMERO #76
CREAR UNA CLASE ANIMAL CON LOS ATRIBUTOS
ESPECIE Y NOMBRE
LA CLASE DEBE TENER LOS METODOS:
INIT Y HABLAR()
EL METODO HABLAR NOS RETORNA UNA PALABRA SEGUN LA INTERPRETACION 
DEL SONIDO COMO UN PERRRO SERIA "GUAU"'''

class Animal:
    
    def __init__(self, especie, gato):
        self.especie = especie
        self.gato = gato

    def Hablar(self):
        if self.especie == 'perro':
            return 'GUAUU'
        elif self.especie == 'gato':
            return 'MIAUU'
        else:
            print('.....')
        

perro = Animal('perro', 'solovino')
gato = Animal('gato', 'chispas')
print(perro.Hablar())
print(gato.Hablar())