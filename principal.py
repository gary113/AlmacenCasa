from bd import *
from tkinter import *
from tkinter import ttk


class App():

    def __init__(self):

        #Declaración de contenedores y variables

        self.baseDatos = BD()

        self.ventana = Tk()
        self.ventana.title('Tabla de productos')
        self.ventana.minsize(700, 300)
        self.ventana.geometry('+500+300')
        self.primerFrame = Frame(self.ventana)
        self.segundoFrame = Frame(self.ventana)
        self.tercerFrame = Frame(self.ventana)

        self.textoBuscar = StringVar()
        self.textoId = StringVar()
        self.textoDescripcion = StringVar()
        self.textoCantidad = StringVar()
        self.textoUnidades = StringVar()
        self.textoLugar = StringVar()
        self.textoCambio = StringVar()

        self.listaEntrys = (self.textoBuscar, self.textoId, self.textoDescripcion, self.textoCantidad, self.textoUnidades, self.textoLugar)
        self.listaIdsTabla = []

        ####################

        #Declaración de widgets:

        #En el primer frame:

        self.lblBuscar = Label(self.primerFrame, text='Buscar:')
        self.entryBuscar = Entry(self.primerFrame, textvariable=self.textoBuscar)
        self.btnBuscar = Button(self.primerFrame, text='Buscar', command=self.buscar)
        self.btnCancelar = Button(self.primerFrame, text='Cancelar', command=self.cancelar)

        #En el segundo frame:

        self.tabla = ttk.Treeview(self.segundoFrame, selectmode=BROWSE, columns=('#1', '#2', '#3', '#4'))
        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='Descripción')
        self.tabla.heading('#2', text='Cantidad')
        self.tabla.heading('#3', text='Unidades')
        self.tabla.heading('#4', text='Lugar')
        self.tabla.column("#0", width=50, stretch=False)
        self.tabla.column("#2", width=100, stretch=False)
        self.tabla.column("#3", width=150, stretch=False)
        self.scrollTabla = ttk.Scrollbar(self.segundoFrame, orient=VERTICAL, command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=self.scrollTabla.set)
        self.tabla.bind('<Button-1>', self.seleccionTabla)

        #En el tercer frame:

        self.SeparadorHorizontal = ttk.Separator(self.tercerFrame, orient=HORIZONTAL)
        self.SeparadorVertical = ttk.Separator(self.tercerFrame, orient=VERTICAL)
        self.lblDetalles = Label(self.tercerFrame, text='Detalles de la selección:')
        self.lblId = Label(self.tercerFrame, text='ID:')
        self.entryId = Entry(self.tercerFrame, textvariable=self.textoId, state=DISABLED)
        self.lblDescripcion = Label(self.tercerFrame, text='Descripción:')
        self.entryDescripcion = Entry(self.tercerFrame, textvariable=self.textoDescripcion)
        self.lblCantidad = Label(self.tercerFrame, text='Cantidad:')
        self.entryCantidad = Entry(self.tercerFrame, textvariable=self.textoCantidad,state=DISABLED)
        self.lblUnidades = Label(self.tercerFrame, text='Unidades:')
        self.entryUnidades = Entry(self.tercerFrame, textvariable=self.textoUnidades)
        self.lblLugar = Label(self.tercerFrame, text='Lugar:')
        self.entryLugar = Entry(self.tercerFrame, textvariable=self.textoLugar)
        self.lblOpciones = Label(self.tercerFrame,text='Opciones:')
        self.lblCambio = Label(self.tercerFrame,text='Cambio:')
        self.entryCambio = Entry(self.tercerFrame, textvariable=self.textoCambio,width=6)
        self.btnActualizar = Button(self.tercerFrame, text='Actualizar', command=self.actualizar)

        ####################

        #Grid() de los contenedores y widgets:

        Grid.columnconfigure(self.ventana, 0, weight=1)
        Grid.rowconfigure(self.ventana, 1, weight=1)

        Grid.columnconfigure(self.primerFrame, 1, weight=1)
        Grid.columnconfigure(self.segundoFrame, 0, weight=1)

        Grid.rowconfigure(self.segundoFrame, 0, weight=1)

        Grid.columnconfigure(self.tercerFrame, 1, weight=1)

        #En el primer frame:

        self.primerFrame.grid(row=0, column=0, sticky=EW, padx=5, pady=5)

        self.lblBuscar.grid(row=0, column=0)
        self.entryBuscar.grid(row=0, column=1, sticky=EW)
        self.btnBuscar.grid(row=0, column=2)
        self.btnCancelar.grid(row=0, column=3)

        #En el segundo frame:

        self.segundoFrame.grid(row=1, column=0, sticky=NSEW, padx=5, pady=5)

        self.tabla.grid(row=0, column=0, sticky=NSEW)
        self.scrollTabla.grid(row=0, column=1, sticky=NS)

        #En el tercer frame:

        self.tercerFrame.grid(row=2, column=0, sticky=EW, padx=5, pady=5)

        self.SeparadorHorizontal.grid(row=0, column=0, columnspan=4, sticky=EW)
        self.SeparadorVertical.grid(row=0,column=2,rowspan=7,sticky=NS)
        self.lblDetalles.grid(row=1, column=0,columnspan=2)
        self.lblId.grid(row=2, column=0)
        self.entryId.grid(row=2, column=1, sticky=EW)
        self.lblDescripcion.grid(row=3, column=0)
        self.entryDescripcion.grid(row=3, column=1, sticky=EW)
        self.lblCantidad.grid(row=4, column=0)
        self.entryCantidad.grid(row=4, column=1, sticky=EW)
        self.lblUnidades.grid(row=5, column=0)
        self.entryUnidades.grid(row=5, column=1, sticky=EW)
        self.lblLugar.grid(row=6, column=0)
        self.entryLugar.grid(row=6, column=1, sticky=EW)
        self.lblOpciones.grid(row=1,column=3)
        self.lblCambio.grid(row=3,column=3)
        self.entryCambio.grid(row=4,column=3)
        self.btnActualizar.grid(row=5,column=3,rowspan=2,sticky=NSEW)
        

        ####################

        #Llenar la tabla al inicio y mostrar ventana:

        self.buscar()
        self.ventana.mainloop()

        ####################

    #Métodos de la clase:

    def actualizar(self):

        if(self.listaEntrys[1].get()!=''):

            producto=[]

            for elemento in self.listaEntrys[1:]:
                producto.append(elemento.get())

            if(self.textoCambio.get()!=''):
                producto[2]=float(producto[2])+float(self.entryCambio.get())
       
            aver=self.baseDatos.actualizar(producto)

            for elemento in self.listaEntrys[1:]:
                elemento.set('')
            
            self.textoCambio.set('')
            
            self.buscar()


    def seleccionTabla(self, evento):

        item = self.tabla.identify('item', evento.x, evento.y)
        values = self.tabla.item(item, 'values')

        if(len(values)>0):

            self.listaEntrys[1].set(self.tabla.item(item, 'text'))

            i = 0
            for elemento in self.listaEntrys[2:]:
                elemento.set(values[i])
                i += 1

    def buscar(self):

        self.limpiarTabla()
        resultados = self.baseDatos.buscar(self.textoBuscar.get())

        if(resultados != None):
            for elemento in resultados:
                self.listaIdsTabla.append(self.tabla.insert('', END, text=elemento[0], values=elemento[1:]))

    def limpiarTabla(self):

        if(len(self.listaIdsTabla) > 0):
            for elemento in self.listaIdsTabla:
                self.tabla.delete(elemento)

            self.listaIdsTabla.clear()

    def cancelar(self):

        for elemento in self.listaEntrys:
            elemento.set('')
        
        self.textoCambio.set('')

        self.buscar()

    ####################

#Función main:


if __name__ == "__main__":
    app = App()

####################
