'''                   EJERCICIO NUMERO #66
ESCRIBE UNA FUNCION PARA CALCULAR EL PROMEDIO DE UNA LISTA DE NUMEROS
''' 
def promedio1(lista):
    suma = 0
    promedio = 0
    for i in lista:
        suma = suma + i
        promedio = suma / len(lista)
    return promedio

numeros = []
tamanio = int(input('Ingrese el tamaño de la lista: '))
for i in range(tamanio):
    elemento = int(input('Ingrese un numero entero: '))
    numeros.append(elemento)
print('El promedio de la lista dada es:', promedio1(numeros))
