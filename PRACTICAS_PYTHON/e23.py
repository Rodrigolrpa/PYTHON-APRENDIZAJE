'''                         EJERCICIO NUMERO #23
                    VERIFICA SI UNA PALABRA ES PALINDROMO
'''
cadena = 'ANA'
cadena_palindroma = cadena[::-1]
print(cadena_palindroma)

'''
Qué significa [::-1]:

inicio (vacío):
Al dejar el inicio vacío, Python toma la secuencia desde el 
principio de la cadena o lista (si fuera 0, eso indicaría el 
comienzo, pero como está vacío, es lo mismo).

fin (vacío):
Al dejar el fin vacío, Python tomará la secuencia hasta el final.

paso (-1):
Aquí es donde ocurre la magia. -1 indica que se debe recorrer la 
secuencia en dirección inversa, es decir, comenzando desde el último 
elemento y moviéndose hacia el primero.
'''