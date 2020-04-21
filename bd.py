from pymysql import *


class BD():

    def __conectar(self):

        self.__conexion = connect('localhost', 'gary', 'chiky', 'inventario_casa')

    def mostrar(self):

        try:

            self.__conectar()
            cursor = self.__conexion.cursor()

            cursor.execute('SELECT * FROM Producto')
            resultados = cursor.fetchall()

            for fila in resultados:
                idProducto = fila[0]
                descripcionProducto = fila[1]
                cantidadProducto = fila[2]
                unidadProducto = fila[3]
                lugarProducto = fila[4]
                #print(fila)

            self.__conexion.close()

            return resultados

        except Error as e:

            print("Error {}: {}".format(e.args[0], e.args[1]))

            return None

