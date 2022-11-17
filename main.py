from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk

from Models.Grafo import Grafo
from Models.JSON import JSON
from Models.Vista import Vista

"""
    ? Estructuras de Datos - 2022-2 - Grafos
    * Daniel Alberto Díaz Castro
    * David Rincon Toro
    * Jhonatan David Gómez Castaño
"""

#? GRAFO
grafo = Grafo()
vista = Vista(grafo)

def cargarGrafo(boton):
    # Cargar el JSON
    listaVertices = JSON.cargar("./data/vertices.json")
    
    # Ingresar los vertices
    for vertice in listaVertices:
        grafo.ingresarVertices(vertice["dato"], vertice["X"], vertice["Y"])

    # Ingresar aristas
    for vertice in listaVertices:
        for adyacente in vertice["adyacencias"]:
            grafo.ingresarArista(vertice["dato"], adyacente["destino"], adyacente["peso"])

    # verifica y convertir el grado
    grafo.convertirANoDirigido()

    vista.crearVertices(listaVertices)
    vista.crearAristas()
       
    boton["state"] = "disabled"
        

def obstruirCamino():
    if grafo == None:
        print("No hay grafo cargado")
    else:
        vista.abrirVentanaDialogo()

def main():
    barraMenu = Menu(vista.getVentana())
    mnuCrear = Button(barraMenu)
    mnuObstruir = Button(barraMenu)
    menuRecorridos = Menu(barraMenu)
    menuRecorridos.add_command(label='Profundidad')
    menuRecorridos.add_command(label='Amplitud (Anchura)')
    menuRecorridos.add_command(label='Dijkstra - camino más corto desde la casita')

    barraMenu.add_cascade(label="Cargar grafo", menu=mnuCrear, command= lambda: cargarGrafo(mnuCrear) )
    barraMenu.add_cascade(label="Obstruir", menu=mnuObstruir, command=obstruirCamino)
    barraMenu.add_cascade(label='Recorridos', menu=menuRecorridos)

    vista.getVentana().config(menu=barraMenu)
    mainloop()

if __name__ == "__main__":
    main()