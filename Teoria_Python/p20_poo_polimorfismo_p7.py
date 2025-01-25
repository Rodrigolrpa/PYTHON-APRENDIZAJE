class Publicacion:
    def mostrar_contenido(self):
        pass

class Publicacion_texto(Publicacion):
    def mostrar_contenido(self):
        print('Publicacion de texto')

class Publicacion_foto(Publicacion):
    def mostrar_contenido(self):
        print('Publicacion de foto')

class Publicacion_video(Publicacion):
    def mostrar_contenido(self):
        print('Publicacion de video')

def mostrar_publicacion(publicacion):
    publicacion.mostrar_contenido(publicacion)

post_text = Publicacion_texto
post_foto = Publicacion_foto
post_video = Publicacion_video

mostrar_publicacion(post_text)
mostrar_publicacion(post_foto)
mostrar_publicacion(post_video)