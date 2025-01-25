'''                         EJERCICIO NUMERO #10
                            INVERTIR UNA CADENA
'''

'''[::-1]: Este es el operador de slicing (rebanado) y se divide en tres partes:

Primer campo (antes de :): 
Indica el índice inicial. Si está vacío, significa "comienza desde el inicio".
Segundo campo (entre los :):
Indica el índice final. Si está vacío, significa "ve hasta el final".
Tercer campo (después de :): 
Es el paso, que define cómo avanzar por la cadena. Si es -1, 
indica que se debe recorrer la cadena hacia atrás (de derecha a izquierda).
'''

cadena = 'cadena'
invertir = cadena[::-1]

print("Cadena inversa:", invertir)