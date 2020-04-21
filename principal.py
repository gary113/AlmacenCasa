from bd import *
from tkinter import *
from tkinter import ttk


baseDatos = BD()
resultados=baseDatos.mostrar()

ventana = Tk()

tabla=ttk.Treeview(ventana, columns=('Cantidad','Unidades','Lugar'))
tabla.heading('#0', text='Descripción')
tabla.heading('Cantidad', text='Cantidad')
tabla.heading('Unidades', text='Unidades')
tabla.heading('Lugar', text='Lugar')

if(resultados!=None):
    for elemento in resultados:
        tabla.insert('', END, text=elemento[1], values=elemento[2:])

tabla.pack()

ventana.mainloop()