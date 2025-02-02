'''                   EJERCICIO NUMERO #65
ESCRIBE UNA FUNCION PARA CONVERTIR GRADOS CELSIUS A FAHRENHEIT
''' 
def fahren_to_cels(celsius):
    fharenheit = ((9/5) * celsius)+32
    return fharenheit

grados = float(input('Ingrese grados celsius: '))
print('La conversion da: ',fahren_to_cels(grados))