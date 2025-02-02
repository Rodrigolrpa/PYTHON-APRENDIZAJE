'''                   EJERCICIO NUMERO #68
ESCRIBE UNA FUNCION QUE PIDA POR TECLADO LA DISTANCIA Y LA VELOCIDAD PARA PODER
CALCULAR EL TIEMPO DE VIAJE
''' 
def tiempo_viaje():
    distancia = float(input('Ingrese la distancia: '))
    velocidad = float(input('Ingrese la velocidad: '))
    tiempo = distancia / velocidad
    print('El tiempo de viaje sera:', tiempo * 60 ,'minutos')

tiempo_viaje()

