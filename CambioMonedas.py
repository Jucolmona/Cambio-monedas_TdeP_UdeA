#Importar librerias para interfaz gráfica
from tkinter import *
import util

iconos = ['IMAGENES/barra-grafica.png',
          'IMAGENES/base-de-datos.png']

#crear una ventana
v = Tk()
v.title("Cambio de monedas")
v.geometry("400x300")

util.agregarBarra(v, iconos)


v.mainloop()