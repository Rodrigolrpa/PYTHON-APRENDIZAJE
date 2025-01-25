'''Simular un carrito de compras con python
se requiere agregar producto y mostrar los productos
agregados, utiliza POO'''

class Tienda_online:
    def __init__(self):
        self.carrito = []
    
    def agregar_carrito(self, nombre, precio):
        producto =  {'nombre': nombre, 'precio' : precio}
        self.carrito.append(producto)
        print(f'{nombre} agregado al carrito')
    
    def mostrar_carrito(self):
        if self.carrito:
            for producto in self.carrito:
                print(f'- {producto['nombre']} - $ {producto['precio']}')
        else:
            print('Carrito vacio')

tienda = Tienda_online()
tienda.agregar_carrito('carrito', 210)
tienda.agregar_carrito('trapeador', 55.6)
tienda.mostrar_carrito()