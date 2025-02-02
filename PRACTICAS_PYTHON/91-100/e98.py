'''                  EJERCICIO NUMERO #98
ESCRIBIR EN UN ARCHIVO HTML HOLA QUE TAL AUTODIDACTA'''

def escribir(nombre_archivo, contenido):
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(contenido)

escribir('index.html', 'Hola que tal autodidacta')