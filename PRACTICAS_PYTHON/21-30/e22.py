'''                         EJERCICIO NUMERO #22
                DIVIDE UNA CADENA EN UNA LISTA DE SUBCADENAS
'''
#FORMA 1
cadena = 'HOLA'

subcadena1 = cadena[0 : 2]
subcadena2 = cadena[2 : 4]
lista_cadena = [subcadena1,subcadena2]
print(lista_cadena)

#FORMA 2
cadena1 = 'Hola que tal'
division = cadena1.split()
print(division)

#FORMA 3
cadena4 = "123abc456abc789"
division4 = cadena4.split("abc")
print(division4)

'''
Metodo split()
Por defecto: Divide la cadena por espacios.

Especificando un delimitador: 
Puedes dividir usando cualquier carácter o cadena como delimitador, como ,, ;, o incluso una palabra como "abc".

Si el delimitador no se encuentra: 
Si no hay coincidencias con el delimitador, la cadena completa será devuelta como una lista con un solo elemento.'''