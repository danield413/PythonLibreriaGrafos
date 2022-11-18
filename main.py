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

listaVertices = JSON.cargar("./data/vertices.json")

def cargarGrafo():
    vista.resetear()

    # Cargar el JSON
    
    # Ingresar los vertices
    for vertice in listaVertices:
        grafo.ingresarVertices(vertice["dato"], vertice["X"], vertice["Y"])

    # Ingresar aristas
    for vertice in listaVertices:
        for adyacente in vertice["adyacencias"]:
            grafo.ingresarArista(vertice["dato"], adyacente["destino"], adyacente["peso"])

    # verifica y convertir el grado
    grafo.convertirANoDirigido()

    cargarVista()

    #* debug
    # x = grafo.recorridoAmplitud("Casita") 
    # print(x)

    # print(x)
    # print( grafo.obtenerParesDeElementos(x) )
    # grafo.mostrarAristasOrdenadas()
    # y = grafo.recorridoProfundidad("Casita")
    # print(y)
    # print( grafo.obtenerParesDeElementos(y) )
    # print( grafo.recorridoProfundidad("Casita") )
        

def obstruirCamino():
    vista.getCanvas().delete("recorrido")
    if grafo == None:
        print("No hay grafo cargado")
    else:
        vista.abrirVentanaDialogo()

def cargarVista():
    vista.getCanvas().delete("recorrido")
    vista.crearVertices(listaVertices)
    vista.crearAristas()

def profundidad():
    cargarVista()
    vista.getCanvas().create_text(10, 10, text="Profundidad", anchor="nw", font="Arial 20 bold")
    profundidad = grafo.recorridoProfundidad("Casita")
    print(profundidad)
    vista.crearAristasRecorrido( grafo.obtenerParesDeElementos(profundidad), "P" )

def amplitud():
    cargarVista()
    vista.getCanvas().create_text(10, 10, text="Amplitud", anchor="nw", font="Arial 20 bold")
    aristas = grafo.recorridoAmplitud2("Casita") 
    l = []
    for arista in aristas:
        l.append([arista.getOrigen(), arista.getDestino()])
    vista.crearAristasRecorrido( l, "A" )

def dijkstra():
    cargarVista()
    vista.getCanvas().create_text(10, 10, text="Dijkstra", anchor="nw", font="Arial 20 bold")
    dijkstra = grafo.dijkstra("Casita")
    print(dijkstra)
    vista.crearAristasRecorrido( dijkstra, "D" )

def prim():
    cargarVista()
    vista.getCanvas().create_text(10, 10, text="Prim", anchor="nw", font="Arial 20 bold")
    prim = grafo.prim()
    print(prim)
    vista.crearAristasRecorrido( prim, "PR" )

def rutaMasCorta():
    vista.getCanvas().delete("recorrido")
    
    #TODO ruta más corta desde la casita hasta una sucursal determinada

def main():
    barraMenu = Menu(vista.getVentana())
    mnuCrear = Button(barraMenu)
    mnuObstruir = Button(barraMenu)
    menuRecorridos = Menu(barraMenu)
    mnuRutaCorta = Button(barraMenu)

    menuRecorridos.add_command(label='Profundidad', command=profundidad)
    menuRecorridos.add_command(label='Amplitud (Anchura)', command=amplitud)
    menuRecorridos.add_command(label='Prim - Conexión sucursales forma más óptima', command=prim)
    menuRecorridos.add_command(label='Dijkstra - camino más corto desde la casita', command=dijkstra)


    barraMenu.add_cascade(label="Cargar grafo", menu=mnuCrear, command=cargarGrafo )
    barraMenu.add_cascade(label="Obstruir", menu=mnuObstruir, command=obstruirCamino)
    barraMenu.add_cascade(label='Recorridos', menu=menuRecorridos)
    barraMenu.add_cascade(label="Ruta más corta", menu=mnuRutaCorta, command=rutaMasCorta )

    vista.getVentana().config(menu=barraMenu)
    mainloop()

if __name__ == "__main__":
    main()