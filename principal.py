from bd import *
from tkinter import *
from tkinter import messagebox, ttk


class App():

    def __init__(self):

        #Declaración de contenedores y variables

        self.baseDatos = BD()

        self.ventana = Tk()
        self.ventana.title('Tabla de productos')
        self.ventana.minsize(700, 300)
        self.ventana.geometry('+600+300')

        if sys.platform.startswith('win'):
            self.ventana.iconbitmap(default='iconos/icono.ico')
        else:
            self.ventana.iconphoto(True, PhotoImage(file='iconos/icono.png'))

        self.frameBuscar = Frame(self.ventana)
        self.frameTabla = Frame(self.ventana)
        self.frameDetalles = Frame(self.ventana)
        self.frameOpciones = Frame(self.ventana)

        self.textoBuscar = StringVar()
        self.textoId = StringVar()
        self.textoDescripcion = StringVar()
        self.textoCantidad = StringVar()
        self.textoUnidades = StringVar()
        self.textoLugar = StringVar()
        self.textoCambio = StringVar()
        self.opcionRadioButton = IntVar()

        self.tuplaTextoEntrys = (self.textoBuscar, self.textoId, self.textoDescripcion, self.textoCantidad, self.textoUnidades, self.textoLugar)
        self.listaIdsTabla = []

        ####################

        #Declaración de widgets:

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
        self.tabla.column("#3", width=150, stretch=False)
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

        ####################

        #Grid() de los contenedores y widgets:

        Grid.columnconfigure(self.ventana, 0, weight=1)
        Grid.rowconfigure(self.ventana, 1, weight=1)
        Grid.columnconfigure(self.frameBuscar, 1, weight=1)
        Grid.columnconfigure(self.frameTabla, 0, weight=1)
        Grid.rowconfigure(self.frameTabla, 0, weight=1)
        Grid.columnconfigure(self.frameDetalles, 1, weight=1)
        Grid.columnconfigure(self.frameOpciones, 4, weight=1)

        self.frameBuscar.grid(row=0, column=0, sticky=EW, padx=5, pady=5)
        self.frameTabla.grid(row=1, column=0, sticky=NSEW, padx=5, pady=5)
        self.frameDetalles.grid(row=3, column=0, sticky=EW, padx=5, pady=5)
        self.frameOpciones.grid(row=2, column=0, sticky=EW, padx=5, pady=5)

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

    ####################

#Función main:


if __name__ == "__main__":
    app = App()

####################
