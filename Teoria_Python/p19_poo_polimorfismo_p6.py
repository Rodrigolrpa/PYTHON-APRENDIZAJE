class Dispositivo:
    def reproducir():
        pass

class Television(Dispositivo):
    def reproducir(self):
        print('Cambiando de canal')

class ReproductorDVD(Dispositivo):
    def reproducir(self):
        print('Reproduciendo DVD')

def reproducir_contenido(dispositivo):
    dispositivo.reproducir()

tv = Television()
dvd = ReproductorDVD()

reproducir_contenido(tv)
reproducir_contenido(dvd)