'''                  EJERCICIO NUMERO #97
HACER UNA FUNCION PARA CREAR UN ARCHIVO DE TEXTO PLANO'''

def crear_archivo(nombre_archivo):
    with open(nombre_archivo, 'w'):
        pass

crear_archivo('index.php')