from Models.Grafo import Grafo

#? GRAFO
grafo = Grafo()

#? VERTICES
grafo.ingresarVertices("Manizales")
grafo.ingresarVertices("Pereira")
grafo.ingresarVertices("Tulua")
grafo.ingresarVertices("Cali")
grafo.ingresarVertices("Manizales")
grafo.ingresarVertices("Buga")
grafo.ingresarVertices("Monteria")

#? ARISTAS
#* Grafo no dirigido (las aristas tienen doble sentido y mismo peso)
grafo.ingresarArista("Monteria", "Pereira", 150)
grafo.ingresarArista("Pereira", "Monteria", 150)

grafo.ingresarArista("Manizales", "Buga", 15)
grafo.ingresarArista("Buga", "Manizales", 15)

grafo.ingresarArista("Manizales", "Pereira", 40)
grafo.ingresarArista("Pereira", "Manizales", 40)

grafo.ingresarArista("Tulua", "Manizales", 60)
grafo.ingresarArista("Manizales", "Tulua", 60)

grafo.ingresarArista("Pereira", "Tulua", 80)
grafo.ingresarArista("Tulua", "Pereira", 80)

grafo.ingresarArista("Cali", "Tulua", 110)
grafo.ingresarArista("Tulua", "Cali", 110)

grafo.ingresarArista("Cali", "Pereira", 100)
grafo.ingresarArista("Pereira", "Cali", 100)

# print( grafo.recorridoAmplitud("Manizales") )
# print( grafo.recorridoProfundidad("Manizales") )

# print( len(grafo.getListaAristas()) )
# grafo.convertirANoDirigido()
# print( len(grafo.getListaAristas()) )

# print("--------------------------------------")

# grafo.mostrarVertices()
# grafo.mostrarAristas()
# print(grafo.numeroPozos())
# grafo.mostrarVertices()
# print( grafo.aristaMayor().getPeso() )
# print(grafo.promedioPeso())
# grafo.mostrarAristasOrdenadas()
# print( grafo.fuenteConMasAdyacentes().getDato() )
# print( grafo.recorridoProfundidad("Manizales") )
# print( grafo.recorridoAmplitud("Manizales") )

# print( grafo.dijkstra("Manizales") )


# grafo.ingresarVertices("A")
# grafo.ingresarVertices("B")
# grafo.ingresarVertices("C")
# grafo.ingresarVertices("D")
# grafo.ingresarVertices("E")
# grafo.ingresarVertices("F")
# grafo.ingresarVertices("G")

# grafo.ingresarArista("A", "B", 7)
# grafo.ingresarArista("B", "A", 7)
# grafo.ingresarArista("A", "D", 5)
# grafo.ingresarArista("D", "E", 15)
# grafo.ingresarArista("D", "B", 9)
# grafo.ingresarArista("D", "F", 6)
# grafo.ingresarArista("F", "G", 11)
# grafo.ingresarArista("F", "E", 8)
# grafo.ingresarArista("B", "E", 7)
# grafo.ingresarArista("B", "C", 8)
# grafo.ingresarArista("E", "C", 5)
# grafo.ingresarArista("E", "G", 9)

# print( grafo.mostrarAristas() )
# grafo.obstruir("Manizales", "Pereira")
# grafo.obstruir("Pereira", "Manizales")
# print( grafo.mostrarAristas() )
# for i in grafo.getObstruidos():
#     print(i)

# print("\n >>>> Recorrido - Algoritmo Prim \n")
# grafo.prim()
# print("\n >>>> Recorrido - Algoritmo Boruvka \n")
# grafo.boruvka()
# print("\n >>>> Recorrido - Algoritmo Kruskal \n")
# grafo.kruskal()
print("\n >>>> Camino más corto - Algoritmo Dijkstra \n")
grafo.dijkstra("Monteria")



# print(len(grafo.mostrarAristas()))
# grafo.obstruir("Manizales", "Pereira")
# print(len(grafo.mostrarAristas()))

# print(">>>>>> prim 2 <<<<<<<<<<<<<<")
# grafo.prim()