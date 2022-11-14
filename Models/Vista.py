from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk

class Vista:

    def __init__(self):
        # Ventana
        self.ventana = Tk()
        self.ventana.geometry("800x600")
        self.ventana.title("Proyecto Grafos - Estruturas de Datos 2022-2")
        self.ventana.resizable(width=False, height=False)
        self.myCanvas = Canvas(self.ventana)
        self.myCanvas.pack(fill=BOTH, expand=True)
    
        self.urlFondo = "./images/fondo.png"
        # self.agregarFondo()
        self.imagenes = []

    def agregarFondo(self):
        '''Pone una imagen de fondo en la ventana principal.'''
        try:
            self.imagenFondo = PhotoImage(
                file=self.urlFondo)
            self.myCanvas.create_image(
                0, 0, image=self.imagenFondo, anchor="nw")
            self.myCanvas.pack(fill=BOTH, expand=True)

        except Exception as error:
            print(error)

    def getVentana(self):
        return self.ventana

    def getCanvas(self):
        return self.myCanvas
    
    def crearVertice(self, x, y, nombre, urlImagen):
        '''Crea una nueva imagen de un planeta en el canvas.'''
        # urlImagen = "./images/casita.png"
        self.imagenes.append(None)
        self.imagenes[len(
            self.imagenes)-1] = PhotoImage(file=urlImagen)
        idImg = self.myCanvas.create_image(x, y, image=self.imagenes[len(
        self.imagenes)-1], anchor="center")
        self.myCanvas.create_text(x+5, y-35, text=nombre, font="Arial 9 bold")
        return idImg

    def crearArista(self, x1, y1, x2, y2, peso):
        '''Crea una nueva linea entre dos vertices.'''
        self.myCanvas.create_line(x1, y1+25, x2, y2+25, fill="#7000FF", width=3)
        self.myCanvas.create_text((x1+x2)/2, ((y1+25+y2+25)/2)-10, text=peso, font="Helvetica 10 bold")