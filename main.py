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
vista = Vista()

def cargarGrafo():
    # Cargar el JSON
    listaVertices = JSON.cargar("./data/vertices.json")
    
    # Ingresar los vertices
    for vertice in listaVertices:
        grafo.ingresarVertices(vertice["dato"], vertice["X"], vertice["Y"])

    # Ingresar aristas
    for vertice in listaVertices:
        for adyacente in vertice["adyacencias"]:
            grafo.ingresarArista(vertice["dato"], adyacente["destino"], adyacente["peso"])

    #* Identificar si es no dirigido y convertirlo a dirigido
    print("Es dirigido", grafo.esDirigido())

    # Crear grafo en tkinter
    for vertice in listaVertices:
        vista.crearVertice(vertice["X"], vertice["Y"], vertice["dato"], vertice["rutaImagen"])

    for arista in grafo.ListaAristas:
        origen = grafo.obtenerOrigen(arista.getOrigen())
        destino = grafo.obtenerOrigen(arista.getDestino())
        vista.crearArista(origen.getX(), origen.getY(), destino.getX(), destino.getY(), arista.getPeso())

def main():
    barraMenu = Menu(vista.getVentana())
    mnuCrear = Button(barraMenu)
    mnuObstruir = Button(barraMenu)
    menuRecorridos = Menu(barraMenu)
    menuRecorridos.add_command(label='Profundidad')
    menuRecorridos.add_command(label='Amplitud (Anchura)')
    menuRecorridos.add_command(label='Dijkstra - camino más corto desde la casita')

    barraMenu.add_cascade(label="Cargar grafo", menu=mnuCrear, command=cargarGrafo)
    barraMenu.add_cascade(label="Obstruir", menu=mnuObstruir)
    barraMenu.add_cascade(label='Recorridos', menu=menuRecorridos)

    vista.getVentana().config(menu=barraMenu)
    mainloop()

if __name__ == "__main__":
    main()