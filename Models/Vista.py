from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class Vista:
    def __init__(self, grafo):

        self.grafo = grafo

        # Ventana
        self.ventana = Tk()
        self.ventana.geometry("800x600")
        self.ventana.title("Proyecto Grafos - Estruturas de Datos 2022-2")
        self.ventana.resizable(width=False, height=False)
        self.myCanvas = Canvas(self.ventana)
        self.myCanvas.pack(fill=BOTH, expand=True)
        self.myCanvas.configure(bg="#181818")

        self.urlFondo = "./images/fondo.png"
        # self.agregarFondo()
        self.imagenes = []

        self.ventanaDialogo = None
        self.lista_desplegable = None
        self.lista2_desplegable = None

        self.myCanvas.create_text(
            400,
            50,
            text="Proyecto Grafos - Estruturas de Datos 2022-2",
            font="Purisa 22 bold",
            tags=["texto"],
            fill="#00FF97",
        )
        self.myCanvas.create_text(
            400,
            100,
            text="Librería ACME",
            font="Purisa 18 bold",
            tags=["texto"],
            fill="#00FF97",
        )
        self.myCanvas.create_text(
            400,
            250,
            text="Primero debes generar el sistema!",
            font="Purisa 14 bold",
            tags=["texto"],
            fill="#0087FF",
        )

    def agregarFondo(self):
        """Pone una imagen de fondo en la ventana principal."""
        try:
            self.imagenFondo = PhotoImage(file=self.urlFondo)
            self.myCanvas.create_image(0, 0, image=self.imagenFondo, anchor="nw")
            self.myCanvas.pack(fill=BOTH, expand=True)

        except Exception as error:
            print(error)

    def getVentana(self):
        return self.ventana

    def getCanvas(self):
        return self.myCanvas

    def crearVertices(self, listaVertices):
        for vertice in listaVertices:
            self.crearVertice(
                vertice["X"], vertice["Y"], vertice["dato"], vertice["rutaImagen"]
            )

    def resetear(self):
        self.myCanvas.delete("all")
        self.crearAristas()

    def crearVertice(self, x, y, nombre, urlImagen):
        """Crea una nueva imagen de un planeta en el canvas."""
        # urlImagen = "./images/casita.png"
        self.imagenes.append(None)
        self.imagenes[len(self.imagenes) - 1] = PhotoImage(file=urlImagen)
        idImg = self.myCanvas.create_image(
            x, y, image=self.imagenes[len(self.imagenes) - 1], anchor="center"
        )
        self.myCanvas.create_text(x + 5, y - 35, text=nombre, font="Purisa 9 bold")
        return idImg

    def crearAristasRecorrido(self, recorrido, tipo):
        self.myCanvas.delete("recorrido")
        if tipo == "P":
            color = "#FF008B"
        elif tipo == "A":
            color = "#00FF00"
        elif tipo == "D":
            color = "#FF9300"
        elif tipo == "PR":
            color = "#00FFFF"
        elif tipo == "CR":
            color = "#FF0000"

        for arista in recorrido:
            origen = self.grafo.obtenerOrigen(arista[0])
            destino = self.grafo.obtenerOrigen(arista[1])
            self.crearArista(
                origen.getX(),
                origen.getY(),
                destino.getX(),
                destino.getY(),
                0,
                color,
                "recorrido",
                6,
            )

    def crearAristas(self):
        for arista in self.grafo.ListaAristas:
            origen = self.grafo.obtenerOrigen(arista.getOrigen())
            destino = self.grafo.obtenerOrigen(arista.getDestino())
            self.crearArista(
                origen.getX(),
                origen.getY(),
                destino.getX(),
                destino.getY(),
                arista.getPeso(),
            )

    def crearArista(self, x1, y1, x2, y2, peso, color="#7000FF", tag="linea", grosor=3):
        """Crea una nueva linea entre dos vertices."""
        self.myCanvas.create_line(
            x1, y1 + 25, x2, y2 + 25, fill=color, width=grosor, tags=[tag]
        )
        if peso > 0:
            self.myCanvas.create_text(
                (x1 + x2) / 2,
                ((y1 + 25 + y2 + 25) / 2) - 10,
                text=peso,
                font="Purisa 10 bold",
                tags=["peso"],
            )

    def mostrarObstrucciones(self):
        for obstruccion in self.grafo.getObstruidos():
            origen = self.grafo.obtenerOrigen(obstruccion.getOrigen())
            destino = self.grafo.obtenerOrigen(obstruccion.getDestino())
            self.mostrarObstruccion(origen, destino)

    def mostrarObstruccion(self, origen, destino):
        self.myCanvas.delete("linea")
        self.myCanvas.delete("peso")
        self.crearAristas()
        self.crearArista(
            origen.getX(),
            origen.getY(),
            destino.getX(),
            destino.getY(),
            0,
            "#000000",
            "obstruccion",
        )

    def ejecutarObstruir(self):
        origen = self.lista_desplegable.get()
        destino = self.lista2_desplegable.get()
        objetoOrigen = self.grafo.obtenerOrigen(origen)
        objetoDestino = self.grafo.obtenerOrigen(destino)

        # * verificacion si existe un camino alternativo
        existe = self.grafo.existeCaminoAlternativoAVertice(origen, destino)
        if existe:
            # print( len(self.grafo.getListaAristas()) )
            self.grafo.obstruir(origen, destino)
            # print( len(self.grafo.getListaAristas()) )
            self.ventanaDialogo.destroy()

            self.mostrarObstrucciones()
            # print(objetoOrigen.getAdyacentes())
            # print(objetoDestino.getAdyacentes())

            self.lista_desplegable = None
            self.lista2_desplegable = None
        else:
            messagebox.showinfo(
                "Error",
                "No existe un camino alternativo entre los vertices seleccionados.",
            )

    def ejecutarRuta(self):
        origen = self.lista_desplegable.get()

        objetoOrigen = self.grafo.obtenerOrigen(origen)

        vista = self.grafo.dijkstra(origen)
        self.crearAristasRecorrido(vista, "D")

        self.ventanaDialogo.destroy()
        self.mostrarObstrucciones()

        self.lista_desplegable = None
        self.lista2_desplegable = None

    def ejecutarCorto(self):
        origen = "Casita"
        destino = self.lista_desplegable.get()

        aristas = self.grafo.cortoCamino(origen, destino)
        print("Aristas del camino mas corto: ", aristas)

        # * verificacion si existe un camino alternativo
        existe = self.grafo.existeCaminoAlternativoAVertice(origen, destino)
        if existe:
            self.ventanaDialogo.destroy()
            self.crearAristasRecorrido(aristas, "CR")
        else:
            messagebox.showinfo(
                "Error",
                "No existe un camino alternativo entre los vertices seleccionados.",
            )

    def listarAdyacencias(self, event):
        lista = self.grafo.obtenerOrigen(self.lista_desplegable.get()).getAdyacentes()
        if self.lista2_desplegable != None:
            self.lista2_desplegable.config(values=lista)

    def abrirVentanaDialogo(self):
        """Crea una ventana de dialogo para ingresar datos."""
        self.ventanaDialogo = tk.Toplevel()
        self.ventanaDialogo.geometry("300x200")
        self.ventanaDialogo.title("Obstruir un camino")
        self.ventanaDialogo.resizable(width=False, height=False)

        labels = []
        for vertice in self.grafo.getListaVertices():
            if vertice.getDato() not in labels:
                labels.append(vertice.getDato())

        l1 = Label(self.ventanaDialogo, text="Selecciona el vertice origen")
        l1.pack()

        self.lista_desplegable = ttk.Combobox(self.ventanaDialogo, width=20)
        self.lista_desplegable["values"] = labels
        self.lista_desplegable.pack()

        l2 = Label(self.ventanaDialogo, text="Selecciona el vertice destino: ")
        l2.pack()

        self.lista2_desplegable = ttk.Combobox(self.ventanaDialogo, width=17)
        self.lista2_desplegable.pack()

        self.lista_desplegable.bind("<<ComboboxSelected>>", self.listarAdyacencias)

        button = Button(
            self.ventanaDialogo, text="Obstruir camino", command=self.ejecutarObstruir
        )
        button.pack()

        self.ventanaDialogo.mainloop()

    def abrirVentanaDialogoCaminoCorto(self):
        """Crea una ventana de dialogo para ingresar datos."""
        self.ventanaDialogo = None
        self.ventanaDialogo = tk.Toplevel()
        self.ventanaDialogo.geometry("300x200")
        self.ventanaDialogo.title("Camino mas corto")
        self.ventanaDialogo.resizable(width=False, height=False)

        labels = []
        for vertice in self.grafo.getListaVertices():
            if vertice.getDato() not in labels:
                labels.append(vertice.getDato())

        l1 = Label(self.ventanaDialogo, text="Selecciona el vertice origen")
        l1.pack()

        self.lista_desplegable = ttk.Combobox(self.ventanaDialogo, width=20)
        self.lista_desplegable["values"] = labels
        self.lista_desplegable.pack()

        self.lista_desplegable.bind("<<ComboboxSelected>>", self.listarAdyacencias)

        button = Button(
            self.ventanaDialogo, text="Camino más corto", command=self.ejecutarCorto
        )
        button.pack()

        self.ventanaDialogo.mainloop()

    def abrirVentanaDialogoRutaCorta(self):
        """Crea una ventana de dialogo para ingresar datos."""
        self.ventanaDialogo = None
        self.ventanaDialogo = tk.Toplevel()
        self.ventanaDialogo.geometry("300x200")
        self.ventanaDialogo.title("Camino mas corto")
        self.ventanaDialogo.resizable(width=False, height=False)

        labels = []
        for vertice in self.grafo.getListaVertices():
            if vertice.getDato() not in labels:
                labels.append(vertice.getDato())

        l1 = Label(self.ventanaDialogo, text="Selecciona el vertice origen")
        l1.pack()

        self.lista_desplegable = ttk.Combobox(self.ventanaDialogo, width=20)
        self.lista_desplegable["values"] = labels
        self.lista_desplegable.pack()

        self.lista_desplegable.bind("<<ComboboxSelected>>", self.listarAdyacencias)

        button = Button(
            self.ventanaDialogo, text="Camino más corto", command=self.ejecutarRuta
        )
        button.pack()

        self.ventanaDialogo.mainloop()
