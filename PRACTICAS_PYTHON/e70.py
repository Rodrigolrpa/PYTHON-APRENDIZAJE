'''                   EJERCICIO NUMERO #70
ESCRIBE UNA FUNCION PARA CLASIFICAR SI UNA SUSTANCIA ES ACIDA, BASICA O NEUTRA A 
PARTIR DE SU PH
''' 
def clasificacion():
    ph = float(input('Ingrese el nivel de ph: '))
    if ph < 0 or ph > 14:
        print('El nivel de ph ingresado no es valido')    
    if ph >= 0 and ph <= 6.9:
        print('El nivel de ph ingresado es Acido')
    elif ph >= 7.1 and ph <= 14:
        print('El nivel de ph ingresado es Alcalino')
    elif ph == 7:
        print('El ph ingresado en neutro')

clasificacion()