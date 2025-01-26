'''                  EJERCICIO NUMERO #45
MOSTRAR LOS NUMEROS DEL 1 AL 100, PERO REMPLAZANDO LOS MULTIPLOS DE 3 POR
'FIZZ' Y LOS MULTIPLOS DE 5 POR 'BUZZ':
'''
lista = []
numero = 1

for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        lista.append('FIZZBUZZ')
    elif i % 3 == 0:
        lista.append('FIZZ')
    elif i % 5 == 0:
        lista.append('BUZZ')  
    else:
        lista.append(numero)
        
    numero = numero + 1
print(lista)