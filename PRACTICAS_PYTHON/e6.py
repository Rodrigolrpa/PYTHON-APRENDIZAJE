'''                            EJERCICIO NUMERO #6
                CREA UNA CADENA DE TEXTO Y MUESTRA SU LONGITUD
'''
#FORMA 1.
#Captura de una palabra. 
cadena_texto = input('Ingresa una palabra: ')
#Se inicializa el contador j en 0.
j = 0
#Ciclo for para contar la longitud de la cadena de texto.
for i in cadena_texto:
    j = j + 1
# se imprime el contador que almacena la longitud de la cadena de texto.
print(f'La longitud de la palabra ingresada es de: {j}')

#FORMA 2.
#Se crea una variable que almacena la longitud de la cadena de texto
#haciendo uso de la funcion len() que calcula de forma automatica 
#la longitud de una cadena de texto.
longitud = len(cadena_texto)
print(f'La longitud de la cadena de texto forma 2 es : {longitud}')