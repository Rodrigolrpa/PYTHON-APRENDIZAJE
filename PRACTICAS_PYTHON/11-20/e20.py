'''                         EJERCICIO NUMERO #20
                ENCUNETRA Y MUESTRA EL ULTIMO CARACTER DE UNA CADENA
'''
#FORMA 1.
#captura de un dato, ciclo for para que recorra la cadena y se guarde
#el ultimo caracter en la variable caracter de manera automatica
#pass es para que no requiera tener codigo debido a que no se ocupa
cadena = input('Ingrese una palabra: ')
for caracter in cadena:
    pass

print(caracter)
'''
El índice -1:

En Python, puedes usar índices negativos para acceder a los elementos de una cadena (o cualquier lista o secuencia).
-1 se refiere al último elemento de la cadena.
Los índices negativos cuentan desde el final hacia el principio de la cadena:
-1: Último carácter.
-2: Penúltimo carácter.
-3: Antepenúltimo carácter.
Y así sucesivamente.
'''
cadena = 'Python'
ultimo_caracter = cadena[-1]
print(ultimo_caracter)