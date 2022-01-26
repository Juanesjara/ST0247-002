import numpy as np
class GraphAm:

    def __init__(self, size):
        self.matriz = np.zeros( (size,size))    

    def getEdges(self):
        #aadaaaaa
        return
    
    def getWeight(self, source, destination):
        return self.matriz[source][destination]

    def addArc(self, source, destination, weight):
        self.matriz[source][destination] = weight
               

    def getSuccessors(self, vertex):
        filaVertice = self.matriz[vertex]
        respuesta = []
        for j in range(0,size):
            if respuesta.append(j) != 0:
                respuesta.append(j)
            return respuesta
    def __str__(self):

