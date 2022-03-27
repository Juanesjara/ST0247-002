import csv
from cmath import inf
from collections import deque
import sys

class Graph:
    def __init__(self):
        self.size=0
        self.vertices = []  

    def addVertice(self, cantVertices):
        for i in range(cantVertices - len(self.vertices)):
            self.vertices.append([])
        self.size = cantVertices

    def addArc(self, name, origin , destination, length, oneWay, risk):
        listaLlegada = self.vertices[origin]
        dato = (destination,length, risk, name)
        listaLlegada.append(dato)

        if oneWay == "False":
            listaLlegada = self.vertices[destination]
            dato = (origin, length, risk, name)
            listaLlegada.append(dato)

    def getLength(self, theOrigin, destination):
        laListaLlegada = self.vertices[theOrigin]
        for i in range(len(laListaLlegada)):
            dato = laListaLlegada[i]     
            theDestination = dato[0]
            theLength = dato[1]
            if theDestination == destination:
                return theLength         
        return inf

    def getHarrassmentRisk(self, theOrigin, destination):
        laListaLlegada = self.vertices[theOrigin]
        for i in range(len(laListaLlegada)):
            dato = laListaLlegada[i]      
            theDestination = dato[0]
            theRisk = dato[2]
            if theDestination == destination:
                return theRisk
        return inf

    def getSuccessors(self, source):
        succesores =[]
        laListaLlegada = self.vertices[source]
        for (destination,length, risk, name) in laListaLlegada:
            succesores.append(destination) 
        return succesores   

def getIndiceDeCoordenada(vertices, coordenada):
    for i in range(len(vertices)):
            if vertices[i] == coordenada: 
                return i
    return -1

def getCoordenaPorIndice(vertices, indice):
    if indice < len(vertices):
        return vertices[indice]
    return None

def insertarCoordenada(vertices, coordenada):
    for i in range(len(vertices)):
        if vertices[i] == coordenada: 
            return i
    vertices.append(coordenada)
    return len(vertices)-1 


def removeCharacters(string):
    characters = " ()" 
    for x in range(len(characters)):
        string = string.replace(characters[x],"")
        for x in range(len(characters)):
            string = string.replace(characters[x],"")    
    return string

def caminoMasCorto(caminos , grafo, puntoA, puntoB, visitado, riesgoMaximo, camino, sumaPonderadaRiesgoTotal = 0, distanciaTotal = 0 ):
    camino.append(puntoA)
    visitado[puntoA] = True
    if puntoA == puntoB:
        R = sumaPonderadaRiesgoTotal/distanciaTotal
        if R <= riesgoMaximo:
            if len(caminos) == 0:
                
                caminos.append( (camino, R, distanciaTotal) )
            
            else:
                if distanciaTotal < caminos[0][2]:
                   
                    caminos = [].append((camino, R, distanciaTotal))
            return
        
    succesors = grafo.getSuccessors(puntoA)

    if hanSidoVisitadosTodosLosVecinos(succesors, visitado):
        return 

    for succesor in succesors:
        if not visitado[succesor]:
            sumaPonderadaRiesgoTotalNueva = sumaPonderadaRiesgoTotal + grafo.getHarrassmentRisk(puntoA, succesor) *  grafo.getLength(puntoA, succesor)
            distanciaTotalNueva = distanciaTotal + grafo.getLength(puntoA, succesor)
            if len(caminos) != 0 and distanciaTotalNueva > caminos[0][2]:
                continue
            caminoMasCorto(caminos, grafo, succesor, puntoB,  visitado.copy(), riesgoMaximo, camino.copy(), sumaPonderadaRiesgoTotalNueva, distanciaTotalNueva)

def hanSidoVisitadosTodosLosVecinos(succesors, visitado):
    for i in succesors:
        if not visitado[i]: return False
    return True

def main():
    sys.setrecursionlimit(10000)
    grafo = Graph()
    vertices = []
    print("Leyendo archivo.")
    with open('./calles_de_medellin_con_acoso.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        linea = 0

        for fila in csv_reader:
            if linea == 10000: break
            if linea > 0:

                name = fila[0]

                coordenadaString = removeCharacters(fila[1]).split(",")
                coordenada1 = (float(coordenadaString[0]), float(coordenadaString[1]))

                coordenadaString = removeCharacters(fila[2]).split(",")
                coordenada2 = (float(coordenadaString[0]), float(coordenadaString[1]))

                length = float(fila[3])
                oneway = removeCharacters(fila[4])
                harassmentRisk = 0

                if fila[5] != "":
                    harassmentRisk = float(fila[5])

                indexVertice1 = insertarCoordenada(vertices, coordenada1)
                indexVertice2 =  insertarCoordenada(vertices, coordenada2)

                grafo.addVertice(len(vertices))
                grafo.addArc(name, indexVertice1 ,indexVertice2 , length, oneway, harassmentRisk )
            linea += 1
    
    
    print("Archivo leído en su totalidad.")
    print("Vértices totales", len(vertices))
    while(True):
        caminos = []
        print("Ingrese coordenada de inicio: " )
        inicio = int(input())
        print("Ingrese coordenada de fin: " )
        fin = int(input())

        print("Buscando el camino más corto...")
        caminoMasCorto(caminos, grafo, inicio, fin , [False]*len(vertices), inf, [])
        print("camino más corto :", caminos)


main()


