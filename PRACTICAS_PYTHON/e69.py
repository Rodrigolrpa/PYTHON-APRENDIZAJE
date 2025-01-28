'''                   EJERCICIO NUMERO #69
ESCRIBE UNA FUNCION PARA CALCULAR LA TASA DE DESEMPLEO
TD = NO_DESEMPLEADOS/FUERZA_LABORALX100
''' 
def tasa_desempleo():
    no_desempleados = int(input('Ingresa el numero de desempleados: '))
    fuerza_laboral = int(input('Ingresa la fuerza laboral: '))
    td = no_desempleados / fuerza_laboral * 100
    print('La tasa de desempleo es:', td, '%')

tasa_desempleo()