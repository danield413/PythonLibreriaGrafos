class Vertice():
    def __init__(self, dato, x , y):
        self.dato = dato
        self.ListaAdyacentes = []
        self.x = x
        self.y = y

    def getDato(self):
        return self.dato

    def getX(self):
        return self.x

    def getY(self): 
        return self.y

    def setDato(self,dato):
        self.dato = dato

    def getAdyacentes(self):
        return self.ListaAdyacentes

    # def __str__(self) -> str:
    #     return ("Dato: {0} - Adyacencias: {1} \n".format(self.dato, self.ListaAdyacentes))