'''               EJERCICIO NUMERO #41
    IMPRIME LOS NUMEROS DEL 10 AL 1 EN ORDEN DESCENDENTE
'''
numero = int(input('Ingrese un numero: '))

'''En  python la variable i se inicializa sola en 0 y se va incrementando sola de 
1 en 1 in significa en que rango estara recorriendo el ciclo hasta llegar
al numero puesto'''
#FORMA 1
for i in range(numero):

    print(numero - i)

#FORMA 2
contador = 10
while contador > 0:
    print(contador)
    contador -= 1