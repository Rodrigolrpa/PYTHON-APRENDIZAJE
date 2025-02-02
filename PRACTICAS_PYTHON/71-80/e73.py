'''                  EJERCICIO NUMERO #73
CREA UNA CLASE LIBRO 
ATRIBUTOS:
TITULO, AUTOR, EDITORIAL, AÑO DE PUBLICACIOM
METODOS:
CONSTRUCTOR PARA INICIALIZAR LOS ATRIBUTOS'''

class Libro:
    
    def __init__(self, titulo, autor, editorial, anio_publi):
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.anio_publi = anio_publi

libro = Libro('Harry Potter', 'No se', 'No se', 'No se')
#convierte la instancia en un diccionario.
print(libro.__dict__)

