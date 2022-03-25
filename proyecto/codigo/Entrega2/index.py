import csv
from cmath import inf
from collections import deque


class Graph:
    def _init_(self):
        self.size=0
        self.vertices = [] # = [0,0,0,0...]      
        # for i in range(size):
        #     self.vertices[i] = deque()

    def addVertice(self, cantVertices):
        for i in range(cantVertices - len(self.vertices)):
            self.vertices.append(deque())

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
            dato = laListaLlegada[i] # O(n)       
            theDestination = dato[0]
            theLength = dato[1]
            if theDestination == destination:
                return theLength      
        # for (theDestination,theWeight) in laListaLlegada:
        #     if theDestination == destination:
        #         return theWeight      
        return inf

    def getHarrassmentRisk(self, theOrigin, destination):
        laListaLlegada = self.vertices[theOrigin]
        for i in range(len(laListaLlegada)):
            dato = laListaLlegada[i] # O(n)       
            theDestination = dato[0]
            theRisk = dato[2]
            if theDestination == destination:
                return theRisk
        return inf

    def getSuccessors(self, source):
        otraListica = deque()
        laListaLlegada = self.vertices[source]
        for (destination,length, risk, name) in laListaLlegada:
            otraListica.append(destination) 
        return otraListica   
    
def insertarCoordenada(vertices, coordena):
        for i in range(len(vertices)):
            if vertices[i] == coordena: 
                return i
        vertices.append(coordena)
        return len(vertices)-1 


def removeCharacters(string):
    characters = " ()"
    for x in range(len(characters)):
        string = string.replace(characters[x],"")
        for x in range(len(characters)):
            string = string.replace(characters[x],"")    
    return string

def caminoMasCorto(grafo, puntoA, puntoB, visitado, riesgoMaximo, sumaPonderadaRiesgoTotal = 0, distanciaTotal = 0 , camino = [], caminoCorto = []):
    visitado[puntoA] = True
    camino.append(puntoA)
    if puntoA == puntoB:
        #print("Llegué")
        R = sumaPonderadaRiesgoTotal/distanciaTotal
        if R <= riesgoMaximo:
            if (len(caminoCorto) == 0): 
                caminoCorto.append([camino, distanciaTotal, R])
            else:
                for i in caminoCorto:
                    if distanciaTotal < i[1]:
                        caminoCorto = [].append([camino, distanciaTotal, R])
                        
        # print(caminoCorto)
        return
    
    succesors = grafo.getSuccessors(puntoA)
    if hanSidoVisitadosTodosLosVecinos(succesors, visitado): 
        #print("No llegué. LLegué hasta ", puntoA)
        return []

    for succesor in succesors:
        if not visitado[succesor]:
            visitado[succesor] = True
            sumaPonderadaRiesgoTotalNueva = sumaPonderadaRiesgoTotal + grafo.getHarrassmentRisk(puntoA, succesor) *  grafo.getLength(puntoA, succesor)
            distanciaTotalNueva = distanciaTotal + grafo.getLength(puntoA, succesor)
            caminoMasCorto(grafo, succesor, puntoB,  visitado.copy(), riesgoMaximo, sumaPonderadaRiesgoTotalNueva, distanciaTotalNueva, camino.copy())

    # for index in range(len(caminos)):

    #     #print( caminos[index][2])
    #     if caminos[index][2] > 0.49:
    #         caminos.pop(index)
    #         continue
    #     # indexCaminoMasCorto = 0
    #     # for index in range(len(caminos)):
    #     #     if caminos[index][3] < caminos[indexCaminoMasCorto][3]:
    #     #         indexCaminoMasCorto = index
    #     # return caminos[indexCaminoMasCorto]        
    return caminoCorto


def hanSidoVisitadosTodosLosVecinos(succesors, visitado):
    for i in succesors:
        if not visitado[i]: return False
    return True


def main():

    grafo = Graph()
    vertices = []
    with open('calles_de_medellin_con_acoso.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        


        for row in csv_reader:
            if line_count == 0:
                #print(f'Column names are {", ".join(row)}')
                columnas = row
                line_count += 1
            else:
                name = row[0]

                string = removeCharacters(row[1])
                string2 = removeCharacters(row[2])
                coordenada1 = (float(string), float(string2))

                string = removeCharacters(row[3])
                string2 = removeCharacters(row[4])
                coordenada2 = (float(string), float(string2))

                length = float(row[5])
                oneway = removeCharacters(row[6])
                harassmentRisk = float(row[7]) 

                indexVertice1 = insertarCoordenada(vertices, coordenada1)
                indexVertice2 =  insertarCoordenada(vertices, coordenada2)
                grafo.addVertice(len(vertices))
                grafo.addArc(name, indexVertice1 ,indexVertice2 , length, oneway, harassmentRisk )


    #El usuario entrega la coordenada de inicio, la coordenada de fin y el riesgoDeAcosoMaximo

    print(caminoMasCorto(grafo, 0, 2, [False]*7, 0.49))
main()