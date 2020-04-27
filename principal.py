from bd import *
from tkinter import *
from tkinter import messagebox, ttk


class App():

    def __init__(self):

        #Declaración de contenedores y variables

        self.baseDatos = BD()

        self.ventana = Tk()
        self.ventana.title('Tabla de productos')
        self.ventana.minsize(1000, 500)
        self.ventana.geometry('1000x500+500+300')

        if sys.platform.startswith('win'):
            self.ventana.iconbitmap(default='iconos/icono.ico')
        else:
            self.ventana.iconphoto(True, PhotoImage(file='iconos/icono.png'))

        self.pestanias = ttk.Notebook(self.ventana)
        self.frameProductos = Frame(self.pestanias)
        self.frameHistorial = Frame(self.pestanias)

        self.frameBuscar = Frame(self.frameProductos)
        self.frameTabla = Frame(self.frameProductos)
        self.frameDetalles = Frame(self.frameProductos)
        self.frameOpciones = Frame(self.frameProductos)

        self.frameBuscarHistorial = Frame(self.frameHistorial)
        self.frameTablaHistorial = Frame(self.frameHistorial)

        self.textoBuscar = StringVar()
        self.textoId = StringVar()
        self.textoDescripcion = StringVar()
        self.textoCantidad = StringVar()
        self.textoUnidades = StringVar()
        self.textoLugar = StringVar()
        self.textoCambio = StringVar()
        self.opcionRadioButton = IntVar()

        self.textoBuscarHistorial = StringVar()

        self.tuplaTextoEntrys = (self.textoBuscar, self.textoId, self.textoDescripcion, self.textoCantidad, self.textoUnidades, self.textoLugar)
        self.listaIdsTabla = []
        self.listaIdsTablaHistorial = []

        ####################

        #Declaración de widgets:

        #En el notebook pestanias:

        self.pestanias.add(self.frameProductos, text='Productos')
        self.pestanias.add(self.frameHistorial, text='Historial')

        #En el frame Productos: ----------

        #En el frame buscar:

        self.lblBuscar = Label(self.frameBuscar, text='Buscar:')
        self.entryBuscar = Entry(self.frameBuscar, textvariable=self.textoBuscar)
        self.btnBuscar = Button(self.frameBuscar, text='Buscar', command=self.buscar)
        self.btnCancelar = Button(self.frameBuscar, text='Cancelar', command=self.cancelar)
        self.entryBuscar.bind('<Return>', self.buscar)

        #En el frame tabla:

        self.tabla = ttk.Treeview(self.frameTabla, selectmode=BROWSE, columns=('#1', '#2', '#3', '#4'))
        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='Descripción')
        self.tabla.heading('#2', text='Cantidad')
        self.tabla.heading('#3', text='Unidades')
        self.tabla.heading('#4', text='Lugar')
        self.tabla.column("#0", width=50, stretch=False)
        self.tabla.column("#2", width=100, stretch=False)
        self.tabla.column("#3", width=120, stretch=False)
        self.scrollTabla = ttk.Scrollbar(self.frameTabla, orient=VERTICAL, command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=self.scrollTabla.set)
        self.tabla.bind('<Button-1>', self.seleccionTabla)

        #En el frame detalle:

        self.SeparadorHorizontalDetalle = ttk.Separator(self.frameDetalles, orient=HORIZONTAL)
        self.SeparadorVerticalDetalle = ttk.Separator(self.frameDetalles, orient=VERTICAL)
        self.lblDetalles = Label(self.frameDetalles, text='Detalles de la selección:')
        self.lblId = Label(self.frameDetalles, text='ID:')
        self.entryId = Entry(self.frameDetalles, textvariable=self.textoId, state=DISABLED)
        self.lblDescripcion = Label(self.frameDetalles, text='Descripción:')
        self.entryDescripcion = Entry(self.frameDetalles, textvariable=self.textoDescripcion)
        self.lblCantidad = Label(self.frameDetalles, text='Cantidad:')
        self.entryCantidad = Entry(self.frameDetalles, textvariable=self.textoCantidad, state=DISABLED)
        self.lblUnidades = Label(self.frameDetalles, text='Unidades:')
        self.entryUnidades = Entry(self.frameDetalles, textvariable=self.textoUnidades)
        self.lblLugar = Label(self.frameDetalles, text='Lugar:')
        self.entryLugar = Entry(self.frameDetalles, textvariable=self.textoLugar)
        self.lblCambio = Label(self.frameDetalles, text='Cambio:')
        self.entryCambio = Entry(self.frameDetalles, textvariable=self.textoCambio, width=6)
        self.btnRealizarOperacion = Button(self.frameDetalles, text='Actualizar', command=self.realizarOperacion)

        #En el frame opciones:

        self.separadorHorizontalOpciones = ttk.Separator(self.frameOpciones, orient=HORIZONTAL)
        self.lblOpciones = Label(self.frameOpciones, text='Opciones:')
        self.rdbActualizar = Radiobutton(self.frameOpciones, text='Actualizar', value=0,
                                         variable=self.opcionRadioButton, command=self.seleccionRbdActualizar)
        self.rdbAniadir = Radiobutton(self.frameOpciones, text='Añadir', value=1, variable=self.opcionRadioButton, command=self.seleccionRbdAniadir)
        self.rdbEliminar = Radiobutton(self.frameOpciones, text='Eliminar', value=2,
                                       variable=self.opcionRadioButton, command=self.seleccionRbdEliminar)

        #En el frame historial: ----------

        #En el frame buscar historial:

        self.lblBuscarHistorial = Label(self.frameBuscarHistorial, text='Buscar:')
        self.entryBuscarHistorial = Entry(self.frameBuscarHistorial, textvariable=self.textoBuscarHistorial)
        self.btnBuscarHistorial = Button(self.frameBuscarHistorial, text='Buscar', command=self.buscarHistorial)
        self.btnCancelarHistorial = Button(self.frameBuscarHistorial, text='Cancelar', command=self.cancelarHistorial)
        self.entryBuscarHistorial.bind('<Return>', self.buscarHistorial)

        #En el frame tabla historial:

        self.tablaHistorial = ttk.Treeview(self.frameTablaHistorial, selectmode=BROWSE, columns=('#1', '#2', '#3', '#4', '#5', '#6', '#7'))
        self.tablaHistorial.heading('#0', text='Acción')
        self.tablaHistorial.heading('#1', text='Revisión')
        self.tablaHistorial.heading('#2', text='Fecha y hora')
        self.tablaHistorial.heading('#3', text='ID')
        self.tablaHistorial.heading('#4', text='Descripción')
        self.tablaHistorial.heading('#5', text='Cantidad')
        self.tablaHistorial.heading('#6', text='Unidades')
        self.tablaHistorial.heading('#7', text='Lugar')
        self.tablaHistorial.column("#0", width=80, stretch=False)
        self.tablaHistorial.column("#1", width=80, stretch=False)
        self.tablaHistorial.column("#2", width=150, stretch=False)
        self.tablaHistorial.column("#3", width=50, stretch=False)
        self.tablaHistorial.column("#5", width=100, stretch=False)
        self.tablaHistorial.column("#6", width=120, stretch=False)
        self.scrollTablaHistorial = ttk.Scrollbar(self.frameTablaHistorial, orient=VERTICAL, command=self.tablaHistorial.yview)
        self.tablaHistorial.configure(yscrollcommand=self.scrollTablaHistorial.set)

        ####################

        #Grid() de los contenedores y widgets:

        self.pestanias.grid(row=0, column=0, sticky=NSEW, padx=5, pady=5)
        self.frameBuscar.grid(row=0, column=0, sticky=EW, padx=5, pady=5)
        self.frameTabla.grid(row=1, column=0, sticky=NSEW, padx=5, pady=5)
        self.frameDetalles.grid(row=3, column=0, sticky=EW, padx=5)
        self.frameOpciones.grid(row=2, column=0, sticky=EW, padx=5)
        self.frameBuscarHistorial.grid(row=0, column=0, sticky=EW, padx=5, pady=5)
        self.frameTablaHistorial.grid(row=1, column=0, sticky=NSEW, padx=5, pady=5)

        Grid.columnconfigure(self.ventana, 0, weight=1)
        Grid.rowconfigure(self.ventana, 0, weight=1)
        Grid.columnconfigure(self.frameProductos, 0, weight=1)
        Grid.rowconfigure(self.frameProductos, 1, weight=1)
        Grid.columnconfigure(self.frameHistorial, 0, weight=1)
        Grid.rowconfigure(self.frameHistorial, 1, weight=1)

        Grid.columnconfigure(self.frameBuscar, 1, weight=1)
        Grid.columnconfigure(self.frameTabla, 0, weight=1)
        Grid.rowconfigure(self.frameTabla, 0, weight=1)
        Grid.columnconfigure(self.frameDetalles, 1, weight=1)
        Grid.columnconfigure(self.frameOpciones, 4, weight=1)

        Grid.columnconfigure(self.frameBuscarHistorial, 1, weight=1)
        Grid.columnconfigure(self.frameTablaHistorial, 0, weight=1)
        Grid.rowconfigure(self.frameTablaHistorial, 0, weight=1)

        #En el frame Productos ----------

        #En el frame buscar:

        self.lblBuscar.grid(row=0, column=0)
        self.entryBuscar.grid(row=0, column=1, sticky=EW)
        self.btnBuscar.grid(row=0, column=2)
        self.btnCancelar.grid(row=0, column=3)

        #En el frame tabla:

        self.tabla.grid(row=0, column=0, sticky=NSEW)
        self.scrollTabla.grid(row=0, column=1, sticky=NS)

        #En el frame detalles:

        self.SeparadorHorizontalDetalle.grid(row=0, column=0, columnspan=5, sticky=EW)
        self.SeparadorVerticalDetalle.grid(row=0, column=2, rowspan=7, sticky=NS)
        self.lblDetalles.grid(row=1, column=0, columnspan=2)
        self.lblId.grid(row=2, column=0)
        self.entryId.grid(row=2, column=1, columnspan=1, sticky=EW)
        self.lblDescripcion.grid(row=3, column=0)
        self.entryDescripcion.grid(row=3, column=1, columnspan=1, sticky=EW)
        self.lblCantidad.grid(row=4, column=0)
        self.entryCantidad.grid(row=4, column=1, columnspan=1, sticky=EW)
        self.lblUnidades.grid(row=5, column=0)
        self.entryUnidades.grid(row=5, column=1, columnspan=1, sticky=EW)
        self.lblLugar.grid(row=6, column=0)
        self.entryLugar.grid(row=6, column=1, columnspan=1, sticky=EW)
        self.lblCambio.grid(row=4, column=3)
        self.entryCambio.grid(row=4, column=4)
        self.btnRealizarOperacion.grid(row=1, column=3, rowspan=2, columnspan=2, sticky=NSEW)

        #En el frame opciones:

        self.separadorHorizontalOpciones.grid(row=0, column=0, columnspan=5, sticky=EW)
        self.lblOpciones.grid(row=1, column=0)
        self.rdbActualizar.grid(row=1, column=1)
        self.rdbAniadir.grid(row=1, column=2)
        self.rdbEliminar.grid(row=1, column=3)

        #En el frame historial ----------

        #En el frame buscar historial

        self.lblBuscarHistorial.grid(row=0, column=0)
        self.entryBuscarHistorial.grid(row=0, column=1, sticky=EW)
        self.btnBuscarHistorial.grid(row=0, column=2)
        self.btnCancelarHistorial.grid(row=0, column=3)

        #En el frame tabla historial

        self.tablaHistorial.grid(row=0, column=0, sticky=NSEW)
        self.scrollTablaHistorial.grid(row=0, column=1, sticky=NS)

        ####################

        #Llenar la tabla al inicio y mostrar ventana:

        self.buscar()
        self.ventana.mainloop()

        ####################

    #Métodos de la clase:

    def realizarOperacion(self):

        if self.opcionRadioButton.get() == 0:  # Actualizar

            if self.tuplaTextoEntrys[1].get() != '':

                if self.verificarEntrysLlenos():

                    if self.esNumero(self.textoCambio.get() or self.textoCambio.get() == ''):
                        producto = []

                        for elemento in self.tuplaTextoEntrys[1:]:
                            producto.append(elemento.get())

                        if self.esNumero(self.textoCambio.get()):
                            producto[2] = float(producto[2])+float(self.entryCambio.get())

                        exito = self.baseDatos.actualizar(producto)

                        if exito:
                            messagebox.showinfo(title='Éxito', message='Producto actualizado correctamente')

                            for elemento in self.tuplaTextoEntrys[1:]:
                                elemento.set('')

                            self.textoCambio.set('')
                            self.buscar()

                        else:
                            messagebox.showinfo(title='Error', message='Hubo algún problema con la base de datos')

                    else:
                        messagebox.showinfo(title='Campos numéricos', message='Cambio debe ser numérico')

                else:
                    messagebox.showinfo(title='Llenar campos', message='Debe llenar todos los campos')

            else:
                messagebox.showinfo(title='Elije un producto', message='Debes elegir un producto')

        elif self.opcionRadioButton.get() == 1:  # Añadir

            if self.verificarEntrysLlenos():

                if self.esNumero(self.textoCantidad.get()):
                    producto = []

                    for elemento in self.tuplaTextoEntrys[1:]:
                        producto.append(elemento.get())

                    exito = self.baseDatos.aniadir(producto)

                    if exito:
                        messagebox.showinfo(title='Éxito', message='Producto añadido correctamente')
                        self.limpiarEntrys()
                        self.buscar()

                    else:
                        messagebox.showinfo(title='Error', message='Hubo algún problema con la base de datos')

                else:
                    messagebox.showinfo(title='Campos numéricos', message='Cantidad debe ser numérico')

            else:
                messagebox.showinfo(title='Llenar campos', message='Debe llenar todos los campos')

        elif self.opcionRadioButton.get() == 2:  # Eliminar

            idProducto = self.tuplaTextoEntrys[1].get()

            if idProducto != '':

                if messagebox.askyesno(title='Eliminar producto', message='¿Está seguro que desea eliminar el producto?', icon='warning'):
                    exito = self.baseDatos.eliminar(idProducto)

                    if exito:
                        messagebox.showinfo(title='Éxito', message='Producto eliminado correctamente')
                        self.limpiarEntrys()
                        self.buscar()

                    else:
                        messagebox.showinfo(title='Error', message='Hubo algún problema con la base de datos')

            else:
                messagebox.showinfo(title='Elije un producto', message='Debe seleccionar un producto')

    def seleccionTabla(self, evento):

        if self.opcionRadioButton.get() != 1:
            item = self.tabla.identify('item', evento.x, evento.y)
            values = self.tabla.item(item, 'values')

            if len(values) > 0:
                self.tuplaTextoEntrys[1].set(self.tabla.item(item, 'text'))

                i = 0
                for elemento in self.tuplaTextoEntrys[2:]:
                    elemento.set(values[i])
                    i += 1

    def buscar(self, *evento):

        self.limpiarTabla()
        resultados = self.baseDatos.buscar(self.textoBuscar.get())

        if resultados != None:
            for elemento in resultados:
                self.listaIdsTabla.append(self.tabla.insert('', END, text=elemento[0], values=elemento[1:]))

    def limpiarTabla(self):

        if len(self.listaIdsTabla) > 0:
            for elemento in self.listaIdsTabla:
                self.tabla.delete(elemento)

            self.listaIdsTabla.clear()

    def cancelar(self, *evento):

        self.limpiarEntrys()
        self.buscar()

    def limpiarEntrys(self):
        for elemento in self.tuplaTextoEntrys:
            elemento.set('')

        self.textoCambio.set('')

    def seleccionRbdActualizar(self):

        self.limpiarEntrys()
        self.btnRealizarOperacion.config(text='Actualizar')

        self.entryDescripcion.config(state=NORMAL)
        self.entryCantidad.config(state=DISABLED)
        self.entryUnidades.config(state=NORMAL)
        self.entryLugar.config(state=NORMAL)
        self.entryCambio.config(state=NORMAL)

    def seleccionRbdAniadir(self):

        self.limpiarEntrys()
        self.btnRealizarOperacion.config(text='Añadir')

        self.entryDescripcion.config(state=NORMAL)
        self.entryCantidad.config(state=NORMAL)
        self.entryUnidades.config(state=NORMAL)
        self.entryLugar.config(state=NORMAL)
        self.entryCambio.config(state=DISABLED)

    def seleccionRbdEliminar(self):

        self.limpiarEntrys()
        self.btnRealizarOperacion.config(text='Eliminar')

        self.entryDescripcion.config(state=DISABLED)
        self.entryCantidad.config(state=DISABLED)
        self.entryUnidades.config(state=DISABLED)
        self.entryLugar.config(state=DISABLED)
        self.entryCambio.config(state=DISABLED)

    def verificarEntrysLlenos(self):

        resultado = True

        for entry in self.tuplaTextoEntrys[2:]:
            if entry.get() == '':
                resultado = False
                break

        return resultado

    def esNumero(self, string):
        try:
            float(string)
            return True
        except ValueError:
            return False

    def buscarHistorial(self, *evento):

        if self.textoBuscarHistorial.get() != '':

            self.limpiarTablaHistorial()
            resultados = self.baseDatos.buscarHistorial(self.textoBuscarHistorial.get())

            if resultados != None:
                for elemento in resultados:
                    self.listaIdsTablaHistorial.append(self.tablaHistorial.insert('', END, text=elemento[0], values=elemento[1:]))

        else:

            self.limpiarTablaHistorial()

    def cancelarHistorial(self):

        self.textoBuscarHistorial.set('')
        self.limpiarTablaHistorial()

    def limpiarTablaHistorial(self):

        if len(self.listaIdsTablaHistorial) > 0:
            for elemento in self.listaIdsTablaHistorial:
                self.tablaHistorial.delete(elemento)

            self.listaIdsTablaHistorial.clear()

    ####################

#Función main:


if __name__ == "__main__":
    app = App()

####################
