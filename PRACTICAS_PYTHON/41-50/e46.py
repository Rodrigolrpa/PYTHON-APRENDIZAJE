'''                  EJERCICIO NUMERO #46
SOLICITA AL USUARIO INGRESAR UN NUMERO Y CUENTA CUANTOS DIGITOS TIENE.
'''
numero = int(input('Ingresa un numero entero: '))
contador = 0
'''Cuando usas la división entera (//), 
el resultado es siempre un número entero, 
y si sigues aplicando la operación de división
entera a un número positivo 
o negativo, el número eventualmente se reducirá a 
0 (ya que no tiene parte decimal). '''
while numero != 0:
    numero = numero // 10
    contador = contador + 1

print('Numero de digitos', contador)