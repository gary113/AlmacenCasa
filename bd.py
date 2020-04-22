from pymysql import *


class BD():

    def __conectar(self):

        self.__conexion = connect('localhost', 'gary', 'chiky', 'inventario_casa')

    def buscarTodo(self):

        try:

            self.__conectar()
            cursor = self.__conexion.cursor()
            sql='SELECT * FROM Producto'

            cursor.execute(sql)
            resultados = cursor.fetchall()

            self.__conexion.close()

            return resultados

        except Error as e:

            print("Error {}: {}".format(e.args[0], e.args[1]))

            return None

    def buscar(self,textoBuscar):
        
        if(textoBuscar==''):

            return self.buscarTodo()

        else:

            try:

                self.__conectar()
                cursor = self.__conexion.cursor()

                sql='''SELECT * FROM Producto WHERE
                    id_producto LIKE "%{0}%" OR
                    descripcion_producto LIKE "%{0}%" OR
                    cantidad_producto LIKE "%{0}%" OR
                    unidad_producto LIKE "%{0}%" OR
                    lugar_producto LIKE "%{0}%"'''.format(textoBuscar)

                cursor.execute(sql)
                resultados = cursor.fetchall()

                self.__conexion.close()

                return resultados

            except Error as e:

                print("Error {}: {}".format(e.args[0], e.args[1]))

                return None

