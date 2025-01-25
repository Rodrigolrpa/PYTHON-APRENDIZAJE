#cuidar la identacion para no tener problemas de sintaxys

def saludar():
    print('Hola')

#mandar llamar a la funcion
saludar()
saludar()
saludar()

def sumar(numero1,numero2):
    resultado = numero1 +numero2
    print(resultado)

sumar(1,2)
sumar(22,3.3)
sumar(1,2)

def restar(numero1, numero2):
    #return numero1 - numero2
    return "La resta es " + str(numero1 - numero2)
resta = restar(8,4)
print(resta)