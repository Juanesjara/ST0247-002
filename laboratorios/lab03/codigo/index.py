import math
from collections import deque
class GraphAL:
    def __init__(self, size):
        self.arregloDeListas = [0]*size
        self.size = size
        #[size]
        #[ [], [], [], [] , [] ,[] ...]
        for i in range(0, size):
            self.arregloDeListas[i]= deque()
    def addArc(self, vertex, destination, weight):
        fila = self.arregloDeListas[vertex]
        arco = (destination,weight)
        fila.append(arco)

    def getWeight(self, source, destination):
        laListaLlegada = self.arregloDeListas[source]
        for i in range(len(laListaLlegada)):
            pareja = laListaLlegada[i] # O(n)       
            theDestination = pareja[0]
            theWeight = pareja[1]
            if theDestination == destination:
                return theWeight      
        for (theDestination,theWeight) in laListaLlegada:
            if theDestination == destination:
                return theWeight      
        return 0      

    def getSuccessors(self, source):
        otraListica = deque()
        laListaLlegada = self.arregloDeListas[source]
        for (theDestination,theWeight) in laListaLlegada:
            otraListica.append(theDestination)
        return otraListica


def costoDelMasCorto(g,o:int,d:int)->int:
    arregloDeVisitados = [False]*g.size
    return costoDelMasCortoAUX(g,o,d,arregloDeVisitados)

def costoDelMasCortoAUX(g,o:int,d:int,a:list)->int:
    a[o] = True
    if o == d:
        return 0
    else:
        elCostoDelMasCorto = math.inf
    for vecino in g.getSuccessors(o):
        if not a[vecino]:
            elCostoDelMasCortoDesdeElVecinoHastaD:int = costoDelMasCortoAUX(g,vecino,d,a)
            elCostoDelMasCortoDesdeOHastaDPasandoPorElVecino = g.getWeight(o,vecino) + elCostoDelMasCortoDesdeElVecinoHastaD
        if elCostoDelMasCortoDesdeOHastaDPasandoPorElVecino < elCostoDelMasCorto:
            elCostoDelMasCorto = elCostoDelMasCortoDesdeOHastaDPasandoPorElVecino
    return elCostoDelMasCorto

def main():
    g = GraphAL(5)
    g.addArc(0,1,10)
    g.addArc(0,2,1)
    g.addArc(2,3,2)
    g.addArc(3,0,2)
    g.addArc(3,4,3) 
    g.addArc(1,3,2)
    print(costoDelMasCorto(g,1,3))
    
main()
    