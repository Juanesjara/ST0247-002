from cmath import inf
from collections import deque

class GraphAL:
    def __init__(self, size):
        self.size=size
        self.arregloDeListas = [0]*(size+1) # = [0,0,0,0...]      
        for i in range(size+1):
            self.arregloDeListas[i] = deque()


    def addArc(self, IDsource, IDdestination, weight):
        listaLlegada = self.arregloDeListas[IDsource]
        unaPareja = (IDdestination,weight)
        listaLlegada.append(unaPareja)

        listaLlegada = self.arregloDeListas[IDdestination]
        unaPareja = (IDsource,weight)
        listaLlegada.append(unaPareja)

        

    def getWeight(self, IDsource, IDdestination):
        laListaLlegada = self.arregloDeListas[IDsource]
        for i in range(len(laListaLlegada)):
            pareja = laListaLlegada[i] # O(n)       
            theDestination = pareja[0]
            theWeight = pareja[1]
            if theDestination == IDdestination:
                return theWeight      
        for (theDestination,theWeight) in laListaLlegada:
            if theDestination == IDdestination:
                return theWeight      
        return 0    
    def getSuccessors(self, source):
        otraListica = deque()
        laListaLlegada = self.arregloDeListas[source]
        for (theDestination,theWeight) in laListaLlegada:
            otraListica.append(theDestination) 
        return otraListica   


def caminoMasCorto(grafo, verticeFinal):
    visitado = [False] * grafo.size
    actual = 1
    camino = [actual]
    pesoMenor = inf
    verticeCandidato =  0
    while(True):
        for sucesor in grafo.getSuccessors(actual):
            peso = grafo.getWeight(actual,sucesor)
            if peso<pesoMenor and not visitado[sucesor-1]:
                pesoMenor=peso
                verticeCandidato=sucesor
        if verticeCandidato == actual: return -1
        visitado[actual-1] = True
        camino.append(verticeCandidato)
        actual = verticeCandidato
        pesoMenor = inf
        if verticeCandidato == verticeFinal: break
    return camino

def main():
    # vertices = 5
    # cantArcos = 6

    # grafo = GraphAL(vertices)
    # grafo.addArc(1,2,2)
    # grafo.addArc(2,3,4)
    # grafo.addArc(1,4,1)
    # grafo.addArc(4,3,3)

    #print(grafo.getSuccessors(5))    
    str1 = input("")
    vertices = int(str1[0:1])
    grafo = GraphAL(vertices)

    cantArcos = int(str1[1:2])
    for i in range(cantArcos):
        strTemp = input("")
        a = int(strTemp[0:1])
        b = int(strTemp[1:2])
        w = int(strTemp[2:3])
        grafo.addArc(a,b,w)
    
    print("Camino más corto: ")
    print(caminoMasCorto(grafo, vertices))
main()