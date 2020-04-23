from pymysql import *


class BD():

    def __conectar(self):

        self.__conexion = connect('localhost', 'gary', 'chiky', 'inventario_casa')

    def buscarTodo(self):

        try:

            self.__conectar()
            cursor = self.__conexion.cursor()
            sql = 'SELECT * FROM Producto;'

            cursor.execute(sql)
            resultados = cursor.fetchall()

            self.__conexion.close()

            return resultados

        except Error as e:

            print("Error {}: {}".format(e.args[0], e.args[1]))

            return None

    def buscar(self, textoBuscar):

        if(textoBuscar == ''):

            return self.buscarTodo()

        else:

            try:

                self.__conectar()
                cursor = self.__conexion.cursor()

                sql = '''SELECT * FROM Producto WHERE
                    id_producto LIKE "%{0}%" OR
                    descripcion_producto LIKE "%{0}%" OR
                    cantidad_producto LIKE "%{0}%" OR
                    unidad_producto LIKE "%{0}%" OR
                    lugar_producto LIKE "%{0}%";'''.format(textoBuscar)

                cursor.execute(sql)
                resultados = cursor.fetchall()

                self.__conexion.close()

                return resultados

            except Error as e:

                print("Error {}: {}".format(e.args[0], e.args[1]))

                return None

    def buscarId(self, idBuscar):

        try:

            self.__conectar()
            cursor = self.__conexion.cursor()

            sql = 'SELECT * FROM Producto WHERE id_producto = {};'.format(idBuscar)

            cursor.execute(sql)
            resultados = cursor.fetchall()

            self.__conexion.close()

            return resultados

        except Error as e:

            print("Error {}: {}".format(e.args[0], e.args[1]))

            return None

    def actualizar(self, producto):
        try:

            self.__conectar()
            cursor = self.__conexion.cursor()

            sql = '''UPDATE Producto SET
                descripcion_producto = %s,
                cantidad_producto = %s,
                unidad_producto = %s,
                lugar_producto = %s
                WHERE id_producto = %s;'''

            cursor.execute(sql, (producto[1], producto[2], producto[3], producto[4], producto[0]))

            self.__conexion.commit()
            self.__conexion.close()

        except Error as e:

            print("Error {}: {}".format(e.args[0], e.args[1]))
