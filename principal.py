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

ventana.grid_columnconfigure(1, weight=1)

textoBuscar = StringVar()
listaTabla = []

lblBuscar = Label(ventana, text='Buscar:').grid(row=0, column=0)
entryBuscar = Entry(ventana, textvariable=textoBuscar).grid(row=0, column=1, sticky=EW)
btnBuscar = Button(ventana, text='Buscar', command=lambda: buscar(tabla, listaTabla, textoBuscar, baseDatos)).grid(row=0, column=2)
btnCancelar = Button(ventana, text='Cancelar', command=lambda: cancelar(
    tabla, listaTabla, textoBuscar, baseDatos)).grid(row=0, column=3, columnspan=2)

tabla = ttk.Treeview(ventana, selectmode='browse', columns=('Descripción', 'Cantidad', 'Unidades', 'Lugar'))
scrollTabla = ttk.Scrollbar(ventana, orient="vertical", command=tabla.yview)
tabla.configure(yscrollcommand=scrollTabla.set)
scrollTabla.grid(row=1, column=4, sticky=NS)
tabla.heading('#0', text='ID')
tabla.heading('Descripción', text='Descripción')
tabla.heading('Cantidad', text='Cantidad')
tabla.heading('Unidades', text='Unidades')
tabla.heading('Lugar', text='Lugar')

buscar(tabla, listaTabla, textoBuscar, baseDatos)

tabla.grid(row=1, column=0, columnspan=4)

# ventana2=Tk()

ventana.mainloop()
# ventana2.mainloop()
