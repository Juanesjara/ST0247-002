from collections import deque
from cmath import inf

class GraphAL:
    def __init__(self, size):
        self.size = size
        self.arregloDeListas = [0]*size
        for i in range(0,size):
            self.arregloDeListas[i] = deque()

    def addArc(self, vertex, edge, weight):
        fila = self.arregloDeListas[vertex]
        parejaDestinoPeso = (edge, weight)
        fila.append(parejaDestinoPeso)
    def getSuccessors(self, vertice):
        lista = []
        arreglo = self.arregloDeListas[vertice]
        for i in arreglo:
            if i[1] != 0:
                lista.append(i[0])
        return lista

    def getWeight(self, source, destination):
        arreglo = self.arregloDeListas[source]
        for i in arreglo:
            if i[0] == destination:
                peso = i[1]
        return peso
    
def algoritmoprims(grafo):
    duplas = []
    totalAcumulado= 0
    origen = 0
    verticesBusquedaMenor = []
    visitados =  [False]*grafo.size
    visitados[origen] = True
    vertice = origen
    verticesBusquedaMenor.append(vertice)
    for _ in range(grafo.size-1):
        vertice = elMasCercanoNoVisitado(grafo, visitados, verticesBusquedaMenor,duplas)
        visitados[vertice] = True
    for v in range (len(duplas)):
        print(duplas[v][0])
        totalAcumulado += grafo.getWeight(duplas[v][0], duplas[v][1])
        
    return totalAcumulado

def elMasCercanoNoVisitado(G,visitados,v,duplas):
    distanciaMin = inf
    nodoMasCerca = 0
    for j in v:
        vecinos = G.getSuccessors(j)
        for vecino in vecinos:
            if G.getWeight(j,vecino) <= distanciaMin and not visitados[vecino]:
                distanciaMin = G.getWeight(j,vecino)
                nodoMasCerca = vecino
                vertice = j
    duplas.append((vertice,nodoMasCerca))
    v.append(nodoMasCerca)
    
    return nodoMasCerca

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

    print(algoritmoprims(g))
main()