'''                EJERCICIO NUMERO #43
            SOLICITA AL USUARIO INGRESAR UN NUMERO N E
            IMPRIME EL FACTORIAL DE ESE NUMERO.
            5! = 5 X 4 X 3 X 2 X 1 = 120
'''
numero = int(input('Ingrese un numero entero: '))
factorial = 1
i = 1
while i <= numero:
    factorial = factorial * i
    i += 1
print(factorial)
'''#FACTORIAL
for i in range(1, numero):
    print(i)
    factorial = factorial * i
print(factorial)'''
'''#FORMA 2
fact = 1
i = 1
while i <= n:
    fact = factorial * i
    i = i + 1
print('El factorial es:', fact)
#DISTINTAS MANERAS DE USAR UN FOR'''

'''
# Itera de 0 a 4
for i in range(5):  
    print(i)

# Itera de 3 a 7
for i in range(3, 8):  
    print(i)

# Itera de 0 a 8 con paso de 2
for i in range(0, 10, 2):  
    print(i)

#itera desde manzana hasta cereza 
frutas = ['manzana', 'banana', 'cereza']
for fruta in frutas:
    print(fruta)

#Itera desde H hasta a
mensaje = "Hola"
for letra in mensaje:
    print(letra)

#Itera las claves del diccionario
diccionario = {'a': 1, 'b': 2, 'c': 3}
for clave in diccionario:
    print(clave)

#Itera sobre claves y valores del diccionario
for clave, valor in diccionario.items():
    print(f'Clave: {clave}, Valor: {valor}')

# variable igual a la iteracion de una variable
cuadrados = [x**2 for x in range(5)]
print(cuadrados)
#Continua para brincarse a la siguiente iteracion y break para salir
for i in range(5):
    if i == 2:
        continue  # Salta la iteración cuando i es 2
    print(i)

'''
