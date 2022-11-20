from tkinter import *
from tkinter import messagebox

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

#? JSON
listaVertices = JSON.cargar("./data/vertices.json")

#* CARGA LA INTERFAZ GRÁFICA DE LA APLICACIÓN
def cargarGrafo():
    if grafo.getListaVertices() == []:
        vista.getCanvas().configure(bg="#ffffff")
        vista.resetear()
    
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
    else:
        print("Ya hay un grafo cargado :)")

#* LLAMA A OBSTRUIR UNA ARISTA
def obstruirCamino():
    vista.getCanvas().delete("recorrido")
    vista.getCanvas().delete("titulo-recorrido")
    if grafo == None:
        print("No hay grafo cargado")
    else:
        vista.abrirVentanaDialogo()

#* Método auxiliar
def cargarVista():
    vista.resetear()
    vista.crearVertices(listaVertices)
    vista.crearAristas()
    vista.mostrarObstrucciones()

#* LLAMADA A PROFUNDIDAD DESDE LA CASITA
def profundidad():
    grafo.visistadosCp = []
    cargarVista()
    profundidad = grafo.recorridoProfundidad("Casita")
    # print( len(grafo.getListaAristas()) )

    r = grafo.obtenerParesDeElementos(profundidad)

    recorridoMalo = grafo.comprobarObstruccionEnRecorrido(r)

    if not recorridoMalo:
        vista.getCanvas().create_text(10, 10, text="Profundidad", anchor="nw", font="Arial 20 bold", tags=["titulo-recorrido"])
        vista.crearAristasRecorrido( r, "P" )
    else:
        print("Este recorrido presenta problemas en el grafo")
        messagebox.showinfo("Ups...", "Este recorrido presenta problemas en el grafo, intenta hacer otro recorrido")
    
#* LLAMADA A AMPLITUD DESDE LA CASITA
def amplitud():
    cargarVista()
    aristas = grafo.recorridoAmplitud2("Casita") 
    l = []
    #* ["origen", "destino"] <- l
    for arista in aristas:
        l.append([arista.getOrigen(), arista.getDestino()])

    recorridoMalo = grafo.comprobarObstruccionEnRecorrido(l)
    if not recorridoMalo:
        vista.getCanvas().create_text(10, 10, text="Amplitud", anchor="nw", font="Arial 20 bold", tags=["titulo-recorrido"])
        vista.crearAristasRecorrido( l, "A" )
    else:
        print("Este recorrido presenta problemas en el grafo")
        messagebox.showinfo("Ups...", "Este recorrido presenta problemas en el grafo, intenta hacer otro recorrido")

#* LLAMADA A DIJKSTRA DESDE LA CASITA
def dijkstra():
    cargarVista()
   
    dijkstra = grafo.dijkstra("Casita")
    recorridoMalo = grafo.comprobarObstruccionEnRecorrido(dijkstra)
    if not recorridoMalo:
        vista.getCanvas().create_text(10, 10, text="Dijkstra", anchor="nw", font="Arial 20 bold", tags=["titulo-recorrido"])
        vista.crearAristasRecorrido( dijkstra, "D" )
    else:
        print("Este recorrido presenta problemas en el grafo")
        messagebox.showinfo("Ups...", "Este recorrido presenta problemas en el grafo, intenta hacer otro recorrido")

#* LLAMA AL RECORRIDO PRIM
def prim():
    cargarVista()
    prim = grafo.prim()

    recorridoMalo = grafo.comprobarObstruccionEnRecorrido(prim)
    if not recorridoMalo:
        vista.getCanvas().create_text(10, 10, text="Prim", anchor="nw", font="Arial 20 bold", tags=["titulo-recorrido"])
        vista.crearAristasRecorrido( prim, "PR" )
    else:
        print("Este recorrido presenta problemas en el grafo")
        messagebox.showinfo("Ups...", "Este recorrido presenta problemas en el grafo, intenta hacer otro recorrido")

#* RUTA MÁS CORTA DESDE LA CASITA HASTA UNA SUCURSAL ESPECÍFICA
def rutaMasCorta():
    vista.getCanvas().delete("recorrido")
    
    #TODO ruta más corta desde la casita hasta una sucursal determinada


#* CAMINO (RUTA) MÁS CORTO ENTRE TODAS LAS SUCURSALES PARTIENDO DE UN ORIGEN ESPECÍFICO
def caminoMasCorto():
    vista.getCanvas().delete("recorrido")
    
    #TODO camino más corto entre todas las sucursales partiendo de un origen específico

""""-----------------------------------------------INICIO----------------------------------------"""
def main():
    #* CREA EL MENÚ EN LA VISTA
    barraMenu = Menu(vista.getVentana())
    mnuCrear = Button(barraMenu)
    mnuObstruir = Button(barraMenu)
    menuRecorridos = Menu(barraMenu)

    menuRecorridos.add_command(label='Profundidad', command=profundidad)
    menuRecorridos.add_command(label='Amplitud (Anchura)', command=amplitud)
    menuRecorridos.add_command(label='Prim - Conexión sucursales forma más óptima', command=prim)
    menuRecorridos.add_command(label='Dijkstra - camino más corto desde la casita', command=dijkstra)
    menuRecorridos.add_command(label='Ruta más corta desde la casita hasta una sucursal determinada', command=rutaMasCorta)
    menuRecorridos.add_command(label="Camino más corto entre sucursales desde un origen", command=caminoMasCorto)

    barraMenu.add_cascade(label="Cargar grafo", menu=mnuCrear, command=cargarGrafo)
    barraMenu.add_cascade(label="Obstruir", menu=mnuObstruir, command=obstruirCamino)
    barraMenu.add_cascade(label='Recorridos', menu=menuRecorridos)

    vista.getVentana().config(menu=barraMenu)
    mainloop()

if __name__ == "__main__":
    main()