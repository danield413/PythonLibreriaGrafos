class Arista():
    def __init__(self, Origen, Destino, Peso):
        self.Origen = Origen
        self.Destino = Destino
        self.Peso = Peso
 
    def getOrigen(self):
        return self.Origen

    def getDestino(self):
        return self.Destino

    def getPeso(self):
        return self.Peso

    def __str__(self) -> str:
        return ("Origen: {0} - Destino: {1} - Peso: {2} \n".format(self.Origen, self.Destino, self.Peso))
