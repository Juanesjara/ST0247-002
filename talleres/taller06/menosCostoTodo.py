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

def cicloHamiltonianoCostoMinimo(g, o):
    list = [False]*g.size
    list[o] = True
    listCiclo = ()
    pesoMinimo = 0
    numgrafo = 0
    for j in range(1, g.size):
        arcMenosCostoso = 10000000
        for i in g.getSuccessors(o):
            if  arcMenosCostoso > g.getWeight(o, i):
                if not list [i]:
                    arcMenosCostoso = g.getWeight(o,i)
                    sucesorElegido = i
                
        pesoMinimo += arcMenosCostoso
        list[sucesorElegido] = True
        o = sucesorElegido
    print(list)
    print(arcMenosCostoso)
    return

def main():
    size = 5
    g = GraphAL(size)
    g.addArc(0,1,3)
    g.addArc(0,2,2)
    g.addArc(1,0,3)
    g.addArc(1,2,1)
    g.addArc(2,0,2)
    g.addArc(2,1,1)
    cicloHamiltonianoCostoMinimo(g, 0)



main()