'''                       EJERCICIO NUMERO #3
                    CONCATENA DOS CADENAS DE TEXTO.
'''
#Declaracion de variables de tipo string por default que seran capturadas.
nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')

#Concatenacion de las dos cadenas de texto ingresadas (+ " " concatena un espacio en blanco).
nombre_completo = nombre + " " + apellido

#Se muestra en pantalla la concatenacion hecha anteriormente.
print(f'Hola {nombre_completo} soy VS CODE.')