'''                  EJERCICIO NUMERO #85
CONTAR EL NUMERO DE VOCALES EN UNA LISTA DE PALABRAS UTILIZANDO MAP'''

def contador_vocales(palabras):
    return sum(1 for letra in palabras if letra.lower() in 'aeiou')
    

lista_palabras = ['Hola', 'Esto', 'Es', 'Una', 'Lista', 'De', 'Palabras']

vocales_contador = list(map(contador_vocales, lista_palabras))
print(vocales_contador)