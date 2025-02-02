'''                  EJERCICIO NUMERO #88
VERIFICAR SI UN NUMERO ES PAR USANDO LAMBDA
'''
#FORMA 1
par = lambda numero : numero % 2 == 0

print(par(4))

#FORMA 2
par = lambda numero : 'PAR' if numero % 2 == 0 else 'IMPAR'

print(par(6))