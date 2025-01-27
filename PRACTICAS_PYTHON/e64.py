'''                   EJERCICIO NUMERO #60
ESCRIBE UNA FUNCION PARA VERIFICAR SI UN NUMERO ES PAR O IMPAR
'''

#Hacer uso de try: realiza lo que esta debajo y except
#lo que hace es realizar lo de abajo en caso de un ValueError
def par_impar(numero):
    if numero % 2 == 0:
        print('El numero', numero, 'es par')
    else:
        print('El numero', numero, 'es impar')
try:
    par_impar(int(input('Ingrese un numero entero: ')))
except ValueError:
    print('Por favor, ingrese un numero entero valido.')