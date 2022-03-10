from cmath import inf
from sre_compile import dis
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
     
def actualizarLaTabla(g,v,distancias,predecesores) -> None:
    losVecinosDeV = g.getSuccessors(v)
    for vecino in losVecinosDeV:
        elPesoDeVAlVecino = g.getWeight(v,vecino)
        if distancias[v] + elPesoDeVAlVecino < distancias[vecino]: 
            distancias[vecino] = distancias[v] + elPesoDeVAlVecino
            predecesores[vecino] = v

def elMasCercaQueNoEsteVisitado(g,v,visitados) -> int:
    losVecinosDeV = g.getSuccessors(v)
    elPesoDelMasCerca, elMasCerca = inf, 0
    for vecino in losVecinosDeV:
        peso = g.getWeight(v,vecino)
        if peso <= elPesoDelMasCerca and not visitados[vecino]:
            elPesoDelMasCerca, elMasCerca = peso, vecino
    return elMasCerca

def dijkstra(g,s : int) -> list:
  distancias =  [inf]*g.size
  predecesores = [-1]*g.size
  visitados = [False]*g.size
  distancias[s], visitados[s] = 0, True
  v = s
  for _ in range(1,g.size+1):
    v = elMasCercaQueNoEsteVisitado(g,v,visitados)
    visitados[v] = True
    actualizarLaTabla(g,v,distancias,predecesores)
  return (distancias, predecesores)


def main():
    g=GraphAL(6)
    g.addArc(0,1,2)
    g.addArc(0,2,4)
    g.addArc(1,2,1)
    g.addArc(1,3,7)
    g.addArc(2,4,3) 
    g.addArc(4,3,2) 
    g.addArc(3,5,1)
    g.addArc(4,5,5) 

    print(dijkstra(g,0))
main()