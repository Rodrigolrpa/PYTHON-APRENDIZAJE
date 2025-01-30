'''                  EJERCICIO NUMERO #80
OBTENER LA CANTIDAD DE MEMORIA RAM EN MI COMPUTADORA O LAPTOP'''
"Ejecutar el comando pip install psutil"

import psutil

def obtener_ram():
    memoria = psutil.virtual_memory()

    memoria_total = memoria.total / (1024 ** 3)
    return memoria_total

print(obtener_ram())