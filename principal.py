from bd import *
from tkinter import *
from tkinter import ttk


def buscar(tabla, listaTabla, textoBuscar, baseDatos):

    limpiarTabla(tabla, listaTabla)
    resultados = baseDatos.buscar(textoBuscar.get())

    if(resultados != None):
        for elemento in resultados:
            listaTabla.append(tabla.insert('', END, text=elemento[0], values=elemento[1:]))


def limpiarTabla(tabla, listaTabla):

    if(len(listaTabla) > 0):
        for elemento in listaTabla:
            tabla.delete(elemento)

        listaTabla.clear()


def cancelar(tabla, listaTabla, textoBuscar, baseDatos):
    textoBuscar.set('')
    buscar(tabla, listaTabla, textoBuscar, baseDatos)


baseDatos = BD()

ventana = Tk()
ventana.title('Tabla de productos')
ventana.geometry('+500+300')
primerFrame=Frame(ventana)
segundoFrame=Frame(ventana)
#tercerFrame=Frame(ventana)

textoBuscar = StringVar()
listaTabla = []

lblBuscar = Label(primerFrame, text='Buscar:')
entryBuscar = Entry(primerFrame, textvariable=textoBuscar)
btnBuscar = Button(primerFrame, text='Buscar', command=lambda: buscar(tabla, listaTabla, textoBuscar, baseDatos))
btnCancelar = Button(primerFrame, text='Cancelar', command=lambda: cancelar(
    tabla, listaTabla, textoBuscar, baseDatos))

tabla = ttk.Treeview(segundoFrame, selectmode='browse', columns=('#1', '#2', '#3', '#4'))
tabla.heading('#0', text='ID')
tabla.heading('#1', text='Descripción')
tabla.heading('#2', text='Cantidad')
tabla.heading('#3', text='Unidades')
tabla.heading('#4', text='Lugar')
tabla.column("#0", minwidth=0, width=50, stretch=False)
tabla.column("#2", minwidth=0, width=100, stretch=False)
tabla.column("#3", minwidth=0, width=150, stretch=False)

scrollTabla = ttk.Scrollbar(segundoFrame, orient="vertical", command=tabla.yview)
tabla.configure(yscrollcommand=scrollTabla.set)

primerFrame.pack(fill=X)
segundoFrame.pack(fill=BOTH,expand=True)

lblBuscar.pack(side=LEFT)
entryBuscar.pack(side=LEFT, fill=X,expand=True)
btnBuscar.pack(side=LEFT)
btnCancelar.pack(side=LEFT)
tabla.pack(side=LEFT,fill=BOTH,expand=True)
scrollTabla.pack(side=RIGHT,fill=Y)

buscar(tabla, listaTabla, textoBuscar, baseDatos)

# ventana2=Tk()

ventana.mainloop()
# ventana2.mainloop()
