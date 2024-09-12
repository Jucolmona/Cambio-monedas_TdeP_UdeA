#Importar librerias para interfaz gráfica
import _tkinter
from os.path import expanduser
from tkinter.tix import NoteBook

import funciones as fn
from tkinter import *
import util

iconos = ['IMAGENES/barra-grafica.png',
          'IMAGENES/base-de-datos.png']

textoBotones = ["Gráfica Cambio vs Fecha", "Datos Estadísticos"]

#--------- Crear una Ventana -----------
v = Tk()
v.title("Cambio de monedas")
v.geometry("400x300")

#Agregación de una barra de herramientas basada en una lista de archivos con imagenes
botones = util.agregarBarra(v, iconos, textoBotones)
botones[0].configure(command=fn.graficar())
botones[1].configure(command=fn.estadisticas())


#Agregar un contenedor para la lista que permite escoger la moneda a procesar
frame = Frame(v)
frame.pack(side=TOP, fill=X)
util.agregarEtiqueta(frame, "Moneda: ", 0, 0)

#--------- Lista de Divisas -----------
monedas = fn.obtenerMonedas()
comboxMoneda = util.agregarLista(frame, opciones = monedas, columna=1, fila=0)

#-------- Agregar el panel de pestañas para mostrar los resultados -------
try:
    noteBook = NoteBook(v)
    noteBook.pack(fill=BOTH, expand=YES)
    encabezados = ["Gráfica", "Datos"]
    paneles = []
    for e in encabezados:
        frame = Frame(v)
        paneles.append(frame)
        noteBook.add(frame, text=e)
except _tkinter.TclError:
    print("Error en el notebook")
v.mainloop()