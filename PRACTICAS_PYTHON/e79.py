'''                  EJERCICIO NUMERO #79
REPRESENTA UNA CUENTA BANCARIA CON DEPOSITO Y RETIRO DEBE HABER UN TITULAR Y UN SALDO
UTILIZA POO'''

class Cuenta:

    def __init__(self,titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def deposito(self,cantidad):
        self.saldo += cantidad
        print('Se deposito', cantidad)
    
    def retiro(self,cantidad):
        self.saldo -= cantidad
        print('Se retiro', cantidad)

    def mostrar(self):
        print(self.__dict__)

cuenta1 = Cuenta('Rodrigo', 1200)
cuenta1.mostrar()
cuenta1.deposito(1000)
cuenta1.mostrar()
cuenta1.retiro(850)
cuenta1.mostrar()