'''                   EJERCICIO NUMERO #60
IMPRIMIR LA SUMA DE LOS NUMEROS PARES DEL 1 AL 10 UTILIZANDO CICLO FOR.
''' 

suma = 0

for i in range(2, 10 + 1, 2):
    suma = suma + i
    print(i)
print()
print('La suma es:', suma)