from Models.Arista import *
from Models.Vertice import *
from collections import deque
from copy import copy, deepcopy  

"""
    Clase Grafo que contiene los métodos para la creación de un grafo:
    * Ingresar vertices
    * Ingresar aristas
    * Mostrar vertices
    * Mostrar aristas
    * Numero de pozos
    * Arista mayor
    * Obtener Vertice
    * Obtener Arista
    * Promedio de peso
    * Convertir dirigido a no dirigido
    * Convertir no dirigido a dirigido
    * Mostrar aristas ordenadas
    * Fuente con mas adyacentes
    * Recorrido en Profundidad
    * Recorrido en Amplitud
    * Algoritmo de Dijkstra (Camino más corto)
    * Algoritmo de Prim
    * Algoritmo de Boruvka
    * Algoritmo de Kruskal
    * Obstruir arista
    * Desobstruir arista
    * Mostrar aristas obstruidas
    * Mostrar aristas desobstruidas
"""
class Grafo():

    def __init__(self):
        self.listaVertices = []
        self.ListaAristas = []
        self.visistadosCp = []  
        self.visitadosCa = []
        self.adyacencias = {}
        self.visitadosCKruskal = []
        self.repetidos = 0
        self.obstruidos = []  

    def getListaVertices(self):
        return self.listaVertices

    def getListaAristas(self):
        return self.ListaAristas

    def getObstruidos(self):
        lista = []
        for obstruido in self.obstruidos:
            lista.append(obstruido)        
        return lista

    def convertirANoDirigido(self):
        for arista in self.ListaAristas:
            if( not self.obtenerArista(arista.getDestino(), arista.getOrigen()) ):
                self.ingresarArista(arista.getDestino(), arista.getOrigen(), arista.getPeso())

    def ingresarVertices(self, dato, x = 0, y = 0):
        if not self.verificarExisteVertice(dato, self.listaVertices):
            self.listaVertices.append(Vertice(dato, x, y))

    def verificarExisteVertice(self, dato, lista) -> bool:
        for i in range(len(lista)):
            if dato == lista[i].getDato():
                return True
        return False

    def mostrarVertices(self):
        for i in range(len(self.listaVertices)):
            print("Vertice: {0} - Adyacencias: {1}".format(self.listaVertices[i].getDato(),
            self.listaVertices[i].getAdyacentes()))

    def getGrado(self):
        cont = 0
        for i in range(len(self.listaVertices)):
            cont += 1
        return cont

    def ingresarArista(self, origen, destino, peso):
        # Verificar si existe el origen y el destino y no este ya la arista
        if not self.verificarExisteArista(origen, destino, self.ListaAristas):
            if self.verificarExisteVertice(origen, self.listaVertices) and self.verificarExisteVertice(destino, self.listaVertices):
                # Ingreso la arista
                self.ListaAristas.append(Arista(origen, destino, peso)) 
                # Ingreso la adyacencia en el vertice origen
                self.obtenerOrigen(origen).getAdyacentes().append(destino) #adyacencias

    def obtenerOrigen(self, origen) -> Vertice:
        for vertice in self.listaVertices:
            if vertice.getDato() == origen:
                return vertice
        return None

    def verificarExisteArista(self, origen, destino, lista) -> bool:
        for i in range(len(lista)):
            if origen == lista[i].getOrigen() and destino == lista[i].getDestino():
                return True
        return False

    def mostrarAristas(self):
        for i in range(len(self.ListaAristas)):
            print("Origen: {0} - Destino: {1} - Peso: {2}".format(self.ListaAristas[i].getOrigen(), self.ListaAristas[i].getDestino(), self.ListaAristas[i].getPeso()))
        return self.ListaAristas

    def numeroPozos(self):
        cont = 0
        for i in (self.listaVertices):
            if(i.getAdyacentes() == []):
                cont += 1
        return cont
                
    def lleganAristas(self, vertice):
        for arista in self.ListaAristas:
            if arista.getDestino() == vertice.getDato():
                return True
        return False

    def aristaMayor(self) -> Arista:
        mayor = self.ListaAristas[0]
        for arista in self.ListaAristas:
            if arista.getPeso() > mayor.getPeso():
                mayor = arista
        return mayor

    def promedioPeso(self):
        cont = 0
        for arista in self.ListaAristas:
            cont += arista.getPeso()
        return cont/len(self.ListaAristas)

    def obtenerArista(self, origen, destino) -> Arista:
        for arista in self.ListaAristas:
            if (arista.getOrigen() == origen and arista.getDestino() == destino):
                return arista
        return None

    #* a diferencia del de arriba, este retorna la arista si existe, pero no importa el orden de los parametros (origen, destino) o (destino, origen), este método lo usa Dijkstra
    def obtenerArista2(self, origen, destino) -> Arista:
        for arista in self.ListaAristas:
            if (arista.getOrigen() == origen and arista.getDestino() == destino) or (arista.getOrigen() == destino and arista.getDestino() == origen):
                return arista
        return None
    
    def mostrarAristasOrdenadas(self):
        lista = self.ListaAristas
        lista.sort(key=lambda x: x.getPeso())
        
        # for i in range(len(lista)):
        #     print("Origen: {0} - Destino: {1} - Peso: {2}".format(lista[i].getOrigen(), lista[i].getDestino(), lista[i].getPeso()))

        return lista

    def fuenteConMasAdyacentes(self):
        lista = []
        for vertice in self.listaVertices:
            if(vertice.getAdyacentes() != [] and not self.lleganAristas(vertice)):
                lista.append(vertice)

        lista.sort(key=lambda x: len(x.getAdyacentes()), reverse=True)
        if(lista != []):
            return lista[0]
        else: return None

    def obtenerParesDeElementos(self, listaElementos):
        '''Retorna una lista fragmentada en pares (función recursiva). Ejemplo: 
        [1,2,3,4,5] => [[1,2], [2,3], [3,4], [4,5]]'''
        if len(listaElementos) == 2:
            return [listaElementos]

        # Obtener el par de elementos para este entorno
        parDeEsteEntorno = [listaElementos[0], listaElementos[1]]

        # Quitar el primer elemento de la lista
        listaElementos.pop(0)

        # Obtener las demás listas de pares
        listasDeParesDeElementos = self.obtenerParesDeElementos(listaElementos)

        # Agregar el par de este entorno junto a los demás pares
        listasDeParesDeElementos.insert(0, parDeEsteEntorno)

        # Retornar la lista total con los pares de elementos
        return listasDeParesDeElementos
        
    def recorridoProfundidad(self, dato): 
        if( dato in self.visistadosCp ):
            return
        else:
            vertice = self.obtenerOrigen(dato)
            if( vertice != None ):
                self.visistadosCp.append(vertice.getDato())
                for dato in vertice.getAdyacentes():
                    self.recorridoProfundidad(dato)

        return self.visistadosCp

    def recorridoAmplitud(self, dato):
        cola = deque()
        vertice = self.obtenerOrigen(dato)
        if( vertice != None ):
            cola.append(vertice)
            self.visitadosCa.append(dato)
            while( cola ):
                elemento = cola.popleft()
                for dato in elemento.getAdyacentes():
                    if( not dato in self.visitadosCa ):
                        vertice = self.obtenerOrigen(dato)
                        cola.append(vertice)
                        self.visitadosCa.append(dato)

        return self.visitadosCa

    def ordenamiento(self, copiaAristas):
        for i in range(len(copiaAristas)):
            for j in range(len(copiaAristas)):
                if(copiaAristas[i].getPeso() < copiaAristas[j].getPeso()):
                    temp = copiaAristas[i]
                    copiaAristas[i] = copiaAristas[j]
                    copiaAristas[j] = temp
    
    """Algoritmo PRIM"""
    """Recorrido de Grafo"""
    def prim(self):
        copiaAristas = copy(self.ListaAristas)
        conjunto = [] #* Vertices que voy visitando
        aristasTemp = [] #* Posibles candidatos, aristas en amarillo
        aristasPrim = [] #* Aristas prim, aristas en verde (Finales)

        self.ordenamiento(copiaAristas) #* Ordeno las aristas por peso
        menor = copiaAristas[0] 
        self.dirigido(copiaAristas) #* si es dirigido, lo convierto a dirigido
        conjunto.append(menor.getOrigen()) #* vertice para empezar

        terminado = False
        while(not terminado):
            #* Empieza el algoritmo y termina cuando el conjunto de vertices visitados sea igual a la cantidad de vertices visitados
            self.algoritmo(copiaAristas, conjunto, aristasTemp, aristasPrim)
            if(len(self.listaVertices) == len(conjunto)):
                terminado = True
        
        #* Muestro las aristas finales de Prim
        lista = []
        for i in range(len(aristasPrim)):
            lista.append([aristasPrim[i].getOrigen(), aristasPrim[i].getDestino()])
        print(lista)
        return lista

    def algoritmo(self, copiaAristas, conjunto, aristasTemp, aristasPrim):
        ciclo = False

        #* Se recorren los vertices visitados y se buscan las aristas temporales
        for vertice in conjunto:
            self.agregarAristasTemporales(copiaAristas, aristasTemp, vertice)
        #* se toma la arista temporal con menor peso
        candidata = self.candidataPrim(aristasTemp)
        
        if(candidata != None):
            #* Si hay un ciclo marcamos como True
            if(candidata.getOrigen() in conjunto and candidata.getDestino() in conjunto):
                ciclo = True
            
            #* Si no hay ciclo añado la arista a las aristas finales
            #* y verifico si sus vertices ya han sido visitados y sino lo(s) agrego al conjunto 
            if(ciclo == False):
                aristasPrim.append(candidata)
                if(not candidata.getOrigen() in conjunto):
                    conjunto.append(candidata.getOrigen())
                if(not candidata.getDestino() in conjunto):
                    conjunto.append(candidata.getDestino())
    
    #* Devuelve la arista candidata con menor peso (La más conveniente)
    def candidataPrim(self, aristasTemp):
        if(len(aristasTemp) > 0):
            menor = aristasTemp[len(aristasTemp)-1]
            for arista in aristasTemp:
                if arista.getPeso() < menor.getPeso():
                    menor = arista

            aristasTemp.pop(aristasTemp.index(menor))
            return menor
        return None

    #* Agrega las aristas temporales a la lista de aristas temporales basandonos en el vertice actual
    def agregarAristasTemporales(self, copiaAristas, aristasTemp, vertice):
        #* Verifica y añade aristas temporales
        for arista in copiaAristas:
           if(arista.getOrigen() == vertice or arista.getDestino() == vertice): #* verifica la adyacencia
                aristasTemp.append(arista) #* agrega a la lista de temporales, lista amarilla
                copiaAristas.pop(copiaAristas.index(arista)) #* elimino la arista original

    #* Si no es dirigido, lo convierte 
    def dirigido(self, copiaAristas):
        for elemento in copiaAristas:
            for i in range(len(copiaAristas)):
                if(elemento.getOrigen() == copiaAristas[i].getDestino() and elemento.getDestino() == copiaAristas[i].getOrigen()):
                    copiaAristas.pop(i)
                    break

    """ALGORITMO DE DIJKSTRA"""
    """Menor camino desde un vértice origen a un vértice destino"""
    def dijkstra(self, origen, VerticesAux = []):
        marcados = []  # la lista de los que ya hemos visitado
        caminos = []  # la lista final
        direcciones = [] #* <--- Lista de direcciones de los caminos
        # iniciar los valores en infinito
        for v in self.listaVertices:
            caminos.append(float("inf"))
            marcados.append(False)
            VerticesAux.append(None)
            if v.dato == origen:
                #? O == Origen
                caminos[self.listaVertices.index(v)] = 0
                VerticesAux[self.listaVertices.index(v)] = v.getDato()
        while not self.todosMarcados(marcados):
            aux = self.menorNoMarcado(caminos, marcados)  # obtuve el menor no marcado
            if aux is None:
                break
            indice = self.listaVertices.index(aux)  # indice del menor no marcado
            marcados[indice] = aux.getDato()  # marco como visitado
            valorActual = caminos[indice]
            for vAdya in aux.getAdyacentes():
                indiceNuevo = self.listaVertices.index(self.obtenerOrigen(vAdya))
                arista = self.obtenerArista2(vAdya, aux.dato)
                if caminos[indiceNuevo] > valorActual + arista.getPeso():
                    caminos[indiceNuevo] = valorActual + arista.getPeso()
                    # caminos[indiceNuevo] = {
                    #     "peso": valorActual + arista.getPeso(),
                    #     "origen": aux.dato,
                    #     "destino": self.obtenerOrigen(vAdya).dato
                    # }
                    direcciones.append([aux.dato, self.obtenerOrigen(vAdya).dato])

                    VerticesAux[indiceNuevo] = self.listaVertices[indice].getDato()
        print(marcados)
        print(caminos)
        print(direcciones)
        return direcciones

    def menorNoMarcado(self, caminos, marcados):
        verticeMenor = None
        caminosAux = sorted(caminos)
        copiacaminos = copy(caminos)
        bandera = True
        contador = 0
        while bandera:
            menor = caminosAux[contador]
            if marcados[copiacaminos.index(menor)] == False:
                verticeMenor = self.listaVertices[copiacaminos.index(menor)]
                bandera = False
            else:
                copiacaminos[copiacaminos.index(menor)] = "x"
                contador = contador + 1
        return verticeMenor

    def todosMarcados(self, marcados):
        for j in marcados:
            if j is False:
                return False
        return True

    """ALGORITMO KRUSKAL"""
    """Recorrido de Grafo"""
    def quick_sort(self, array):
        lenght = len(array)
        if lenght <= 1:
            return array
        else:
            pivot = array.pop()

        items_greater = []
        items_lower = []

        for item in array:
            if item.getPeso() > pivot.getPeso():
                items_greater.append(item)
            else:
                items_lower.append(item)
        return self.quick_sort(items_lower) + [pivot] + self.quick_sort(items_greater)

    def kruskal(self):
        copiaAristas = self.quick_sort(
            self.ListaAristas
        )  # Copia de la lista de aristas originales ordenada
        aristasKruskal = []
        listaConjuntos = []
        # self.quick_sort(copiaAristas)#Ordenamiento de la copia de aristas
        for menor in copiaAristas:
            self.operacionesConjuntos(menor, listaConjuntos, aristasKruskal)
        # Esta ordenada de menor a mayor
        lista = []
        #print("la lista de conjunto se redujo a : {0}".format(len(ListaConjuntos)))
        for dato in aristasKruskal:
            lista.append([dato.getOrigen(), dato.getDestino()])
        print(lista)
        return lista

    def operacionesConjuntos(self, menor, listaConjuntos, aristasKruskal):
        encontrados1 = -1
        encontrados2 = -1

        if not listaConjuntos:  # Si esta vacia la lista
            listaConjuntos.append({menor.getOrigen(), menor.getDestino()})
            aristasKruskal.append(menor)
        else:
            for i in range(len(listaConjuntos)):
                if (menor.getOrigen() in listaConjuntos[i]) and (
                    menor.getDestino() in listaConjuntos[i]
                ):
                    return False  ##Camino ciclico

            for i in range(len(listaConjuntos)):
                if menor.getOrigen() in listaConjuntos[i]:
                    encontrados1 = i
                if menor.getDestino() in listaConjuntos[i]:
                    encontrados2 = i

            if encontrados1 != -1 and encontrados2 != -1:
                if (
                    encontrados1 != encontrados2
                ):  # Si pertenecen a dos conjuntos diferentes
                    # debo unir los dos conjuntos
                    # print(encontrados1," ",encontrados2)
                    listaConjuntos[encontrados1].update(
                        listaConjuntos[encontrados2]
                    )  # Uno los dos conjuntos
                    listaConjuntos[encontrados2].clear()  # Elimino el conjunto
                    aristasKruskal.append(menor)

            if (
                encontrados1 != -1 and encontrados2 == -1
            ):  # Si el origen esta unido a un conjunto
                # listaConjuntos[encontrados1].add(menor.getOrigen())
                listaConjuntos[encontrados1].add(menor.getDestino())
                aristasKruskal.append(menor)

            if (
                encontrados1 == -1 and encontrados2 != -1
            ):  # Si el destino esta unido a un conjunto
                listaConjuntos[encontrados2].add(menor.getOrigen())
                # listaConjuntos[encontrados2].add(menor.getDestino())
                aristasKruskal.append(menor)

            if encontrados1 == -1 and encontrados2 == -1:
                listaConjuntos.append({menor.getOrigen(), menor.getDestino()})
                aristasKruskal.append(menor)


    """ALGORITMO BORUVKA"""
    """Recorrido de Grafo"""
    def boruvka(self):
        copiaNodos = deepcopy(self.listaVertices)  # copia de los nodos
        copiaAristas = deepcopy(self.ListaAristas)  # copia de las aristas

        AristasBorukvka = []
        ListaConjuntos = []
        bandera = True
        cantidad = 0
        while(cantidad > 1 or bandera):
            for Nodo in copiaNodos:
                self.operacionesConjuntosB(
                    Nodo, ListaConjuntos, AristasBorukvka, copiaAristas)
            bandera = False
            cantidad = self.cantidadConjuntos(ListaConjuntos)

        cadena = []
        for dato in AristasBorukvka:
            cadena.append([dato.getOrigen(), dato.getDestino()])
        print(cadena)
        return cadena

    def cantidadConjuntos(self, ListaConjuntos):
        cantidad = 0
        for conjunto in ListaConjuntos:
            if len(conjunto) > 0:
                cantidad = cantidad+1
        return cantidad

    def operacionesConjuntosB(self, Nodo, ListaConjuntos, AristasBorukvka, copiaAristas):
        encontrado1 = -1
        encontrado2 = -1
        menor = self.buscarMenor(Nodo, copiaAristas)

        if not menor == None:  # si no esta vacio
            if not ListaConjuntos:  # si esta vacia
                ListaConjuntos.append({menor.getOrigen(), menor.getDestino()})
                AristasBorukvka.append(menor)
            else:
                for i in range(len(ListaConjuntos)):
                    if (menor.getOrigen() in ListaConjuntos[i]) and (menor.getDestino() in ListaConjuntos[i]):
                        return False  # Camino ciclico

                for i in range(len(ListaConjuntos)):
                    if menor.getOrigen() in ListaConjuntos[i]:
                        encontrado1 = i
                    if menor.getDestino() in ListaConjuntos[i]:
                        encontrado2 = i

                if encontrado1 != -1 and encontrado2 != -1:
                    if encontrado1 != encontrado2:  # si pertenecen a dos conjuntos diferentes
                        # debo unir los dos conjuntos
                        ListaConjuntos[encontrado1].update(
                            ListaConjuntos[encontrado2])
                        # elimino el conjunto
                        ListaConjuntos[encontrado2].clear()
                        AristasBorukvka.append(menor)

                if encontrado1 != -1 and encontrado2 == -1:  # si va unido por un conjunto
                    ListaConjuntos[encontrado1].update({menor.getOrigen()})
                    ListaConjuntos[encontrado1].update({menor.getDestino()})
                    AristasBorukvka.append(menor)

                if encontrado1 == -1 and encontrado2 != -1:  # si va unido por un conjunto
                    ListaConjuntos[encontrado2].update({menor.getOrigen()})
                    ListaConjuntos[encontrado2].update({menor.getDestino()})
                    AristasBorukvka.append(menor)

                if encontrado1 == -1 and encontrado2 == -1:  # si no existe en los conjuntos
                    ListaConjuntos.append(
                        {menor.getOrigen(), menor.getDestino()})
                    AristasBorukvka.append(menor)

    def buscarMenor(self, Nodo, copiaAristas):
        temp = []
        for adyacencia in Nodo.getAdyacentes():
            for Arista in copiaAristas:
                # busco las aristas de esa lista de adyacencia
                if Arista.getOrigen() == Nodo.getDato() and Arista.getDestino() == adyacencia:
                    temp.append(Arista)
        if temp:  # si no esta vacia
            # una vez obtenga todas las aristas, saco la menor
            self.ordenamiento(temp)  # ordeno las aristas
            # elimin ese destino porque ya lo voy a visitar
            # print("{0}-{1}:{2}".format(temp[0].getOrigen(),
            #       temp[0].getDestino(), temp[0].getPeso()))

            Nodo.getAdyacentes().remove(temp[0].getDestino())
            return temp[0]  # es la menor

        return None
    
    #* Obstruir una arista
    def obstruir(self, datoOrigen, datoDestino):
        # copiaAristas = copy(self.ListaAristas)
        for arista in range(len(self.ListaAristas)):
            if self.ListaAristas[arista].getOrigen() == datoOrigen and self.ListaAristas[arista].getDestino() == datoDestino:
                # Agregamos la arista a obstruidos
                self.obstruidos.append(self.ListaAristas[arista])
                self.eliminarAdyacencia(datoOrigen, datoDestino)
                # Eliminamos a la arista de la copia
                del self.ListaAristas[arista]
                self.obstruir(datoDestino, datoOrigen)
                break

    #* Eliminar adyacencia de un vértice origen
    def eliminarAdyacencia(self, datoOrigen, datoDestino):
        for vertice in range(len(self.listaVertices)):
            if datoOrigen == self.listaVertices[vertice].getDato():
                indice = self.listaVertices[vertice].getAdyacentes().index(
                    datoDestino)
                self.listaVertices[vertice].getAdyacentes().pop(indice)
                break
    
    #* Desobstruir una arista
    def desobstruir(self, origen, destino):
        for i in range(len(self.obstruidos)):
            if self.obstruidos[i].getOrigen() == origen and self.obstruidos[i].getDestino() == destino:
                self.ingresarArista(
                    origen, destino, self.obstruidos[i].getPeso())
                del self.obstruidos[i]
                self.desobstruir(destino, origen)
                break

   