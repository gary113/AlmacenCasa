from bd import *
from funciones import *
from tkinter import ttk

def seleccionTabla(evento):
    item = tabla.identify('item',evento.x,evento.y)
    print("you clicked on", tabla.item(item,'text'))


#Declaración de contenedores y variables

baseDatos = BD()

ventana = Tk()
ventana.title('Tabla de productos')
ventana.minsize(800, 300)
ventana.geometry('+500+300')
primerFrame = Frame(ventana)
segundoFrame = Frame(ventana)
tercerFrame = Frame(ventana)

textoBuscar = StringVar()
textoId = StringVar()
textoDescripcion = StringVar()
textoCantidad = StringVar()
textoUnidades = StringVar()
textoLugar = StringVar()
listaEntrys = (textoBuscar, textoId, textoDescripcion, textoCantidad, textoUnidades, textoLugar)
listaIdsTabla = []

####################

#Declaración de widgets:

#En el primer frame:

lblBuscar = Label(primerFrame, text='Buscar:')
entryBuscar = Entry(primerFrame, textvariable=textoBuscar)
btnBuscar = Button(primerFrame, text='Buscar', command=lambda: buscar(tabla, listaIdsTabla, textoBuscar, baseDatos))
btnCancelar = Button(primerFrame, text='Cancelar', command=lambda: cancelar(tabla, listaIdsTabla, listaEntrys, baseDatos))

#En el segundo frame:

tabla = ttk.Treeview(segundoFrame, selectmode=BROWSE, columns=('#1', '#2', '#3', '#4'))
tabla.heading('#0', text='ID')
tabla.heading('#1', text='Descripción')
tabla.heading('#2', text='Cantidad')
tabla.heading('#3', text='Unidades')
tabla.heading('#4', text='Lugar')
tabla.column("#0", width=50, stretch=False)
tabla.column("#2", width=100, stretch=False)
tabla.column("#3", width=150, stretch=False)
scrollTabla = ttk.Scrollbar(segundoFrame, orient=VERTICAL, command=tabla.yview)
tabla.configure(yscrollcommand=scrollTabla.set)
tabla.bind('<Button-1>', seleccionTabla)

#En el tercer frame:

Separador = ttk.Separator(tercerFrame, orient=HORIZONTAL)
lblDetalles = Label(tercerFrame, text='Detalles de la selección:')
lblId = Label(tercerFrame, text='ID:')
entryId = Entry(tercerFrame, textvariable=textoId)
lblDescripcion = Label(tercerFrame, text='Descripción:')
entryDescripcion = Entry(tercerFrame, textvariable=textoDescripcion)
lblCantidad = Label(tercerFrame, text='Cantidad:')
entryCantidad = Entry(tercerFrame, textvariable=textoCantidad)
lblUnidades = Label(tercerFrame, text='Unidades:')
entryUnidades = Entry(tercerFrame, textvariable=textoUnidades)
lblLugar = Label(tercerFrame, text='Lugar:')
entryLugar = Entry(tercerFrame, textvariable=textoLugar)

####################

#Grid() de los contenedores y widgets:

Grid.columnconfigure(ventana, 0, weight=1)
Grid.rowconfigure(ventana, 1, weight=1)

Grid.columnconfigure(primerFrame, 1, weight=1)
Grid.columnconfigure(segundoFrame, 0, weight=1)

Grid.rowconfigure(segundoFrame, 0, weight=1)

Grid.columnconfigure(tercerFrame, 1, weight=1)

#En el primer frame:

primerFrame.grid(row=0, column=0, sticky=EW)

lblBuscar.grid(row=0, column=0)
entryBuscar.grid(row=0, column=1, sticky=EW)
btnBuscar.grid(row=0, column=2)
btnCancelar.grid(row=0, column=3)

#En el segundo frame:

segundoFrame.grid(row=1, column=0, sticky=NSEW)

tabla.grid(row=0, column=0, sticky=NSEW)
scrollTabla.grid(row=0, column=1, sticky=NS)

#En el tercer frame:

tercerFrame.grid(row=2, column=0, sticky=EW)

Separador.grid(row=0, column=0, columnspan=2, sticky=EW)
lblDetalles.grid(row=1, column=0)
lblId.grid(row=2, column=0)
entryId.grid(row=2, column=1, sticky=EW)
lblDescripcion.grid(row=3, column=0)
entryDescripcion.grid(row=3, column=1, sticky=EW)
lblCantidad.grid(row=4, column=0)
entryCantidad.grid(row=4, column=1, sticky=EW)
lblUnidades.grid(row=5, column=0)
entryUnidades.grid(row=5, column=1, sticky=EW)
lblLugar.grid(row=6, column=0)
entryLugar.grid(row=6, column=1, sticky=EW)

####################

buscar(tabla, listaIdsTabla, textoBuscar, baseDatos)
ventana.mainloop()
