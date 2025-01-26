'''                EJERCICIO NUMERO #35
            CALCULAR EL IMC E INTERPRETARLO
'''
#Captura e inicializacion de datos
altura = float(input('Ingrese su altura en metros (ejemplo: 1.75): '))
peso = float(input('Ingrese su peso en kg (ejemplo: 82.4): '))

#Calculo IMC e interpretarlo

imc = peso / ((altura * altura))
print('Tu IMC es:', imc)
if imc < 18.5:
    print('Tienes bajo peso')
elif imc >= 18.5 and imc < 24.9:
    print('Tienes peso normal')
elif imc >= 25 and imc < 29.9:
    print('Tienes sobrepeso')
elif imc > 30:
    print('Tienes obesidad')