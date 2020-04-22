from tkinter import *

def buscar(tabla, listaIdsTabla, textoBuscar, baseDatos):

    limpiarTabla(tabla, listaIdsTabla)
    resultados = baseDatos.buscar(textoBuscar.get())

    if(resultados != None):
        for elemento in resultados:
            listaIdsTabla.append(tabla.insert('', END, text=elemento[0], values=elemento[1:]))


def limpiarTabla(tabla, listaIdsTabla):

    if(len(listaIdsTabla) > 0):
        for elemento in listaIdsTabla:
            tabla.delete(elemento)

        listaIdsTabla.clear()


def cancelar(tabla, listaIdsTabla, listaEntrys, baseDatos):
    
    for i in range(len(listaEntrys)):
        listaEntrys[i].set('')
    
    buscar(tabla, listaIdsTabla, listaEntrys[0], baseDatos)


    
