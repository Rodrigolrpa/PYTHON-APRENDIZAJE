'''                  EJERCICIO NUMERO #100
CONECTARSE A UNA BASE DE DATOS MYSQL, HACER
UNA CONSULTA A UNA TABLA Y MOSTRAR LA INFORMACION
EN LA CONSOLA'''



import mysql.connector # type: ignore

class Conexion:
    def conectar(self):
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='visitas'
        )
        return conexion
    
class Visitas(Conexion):

    def consulta_select(self):
        conexion = self.conectar()
        sql = "SELECT id, paterno, fecha FROM t_visitas"
        cursor = conexion.cursor()
        cursor.execute(sql)
        registros = cursor.fetchall()
        cursor.close()
        conexion.close()
        return registros
    
    def imprimir_datos(self):
        datos = self.consulta_select()
        for fila in datos:
            print(fila)

visita = Visitas()
visita.imprimir_datos()
