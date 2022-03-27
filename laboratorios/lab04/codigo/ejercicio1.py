import sys
import csv
from cmath import inf

class Graph:
    def __init__(self):
        self.size = 0
        self.vertices = [] 
        self.arcos = [] 

    def addVertice(self, vertice):
        self.vertices.append(vertice)
        self.arcos.append([])
        self.size += 1
        
    def getIndiceVertice(self, ID):
        index = 0
        for i in range(len(self.vertices)):
            if self.vertices[i][0] == ID:
                index = i
        return index

    def addArc(self, IDsource, IDdestination, length, name):
        index = self.getIndiceVertice(IDsource)
        arco = [IDdestination,length,name]
        self.arcos[index].append(arco)
        return

    def getLength(self, IDsource, IDdestination):
        index = self.getIndiceVertice(IDsource)
        arco = self.arcos[index]
        for dato in (arco):
            if dato[0] == IDdestination:
                return dato[1]      
         
    def getSuccessors(self, IDsource):
        succesores = []
        index = self.getIndiceVertice(IDsource)
        arcos = self.arcos[index]
        for (IDdestination, length, name) in arcos:
            succesores.append(IDdestination) 
        return succesores   


def distanciaMasCorta(grafo, actual, fin):
    visitado = [False] * grafo.size
    visitado[grafo.getIndiceVertice(actual)] = True
    camino = [actual]
    pesoMenor = inf
    

    
    verticeCandidato =  -1

    while(True):
        
        for sucesor in grafo.getSuccessors(actual):
            indice = grafo.getIndiceVertice(sucesor)
            peso = grafo.getLength(actual,sucesor)
            if peso<pesoMenor and not visitado[indice]:
                pesoMenor=peso
                verticeCandidato=sucesor
                
        if verticeCandidato == -1: return []
        indice = grafo.getIndiceVertice(verticeCandidato)
        visitado[indice] = True
        camino.append(verticeCandidato)
        actual = verticeCandidato
        verticeCandidato = -1
        pesoMenor = inf
        if actual == fin: break
    return camino



def main():
    grafo = Graph()
    print("Leyendo archivo.")
    with open('./puentesColgantes.txt') as file:
        reader = csv.reader(file, delimiter=' ')
        linea = 0
        leyendoVertices = False

        for fila in reader:
            if len(fila) == 0: continue
            if fila[0] == "Vertices.":
                leyendoVertices = True
                continue
            if fila[0] == "Arcos.":
                leyendoVertices = False
                continue
            if leyendoVertices: 
                grafo.addVertice([int(fila[0]), float(fila[1]), float(fila[2]),fila[3]])
            else:
                if len(fila) == 5:
                    grafo.addArc( int(fila[0]), int(fila[1]), float(fila[2]), str(fila[3]+fila[4]))
                else:
                    grafo.addArc( int(fila[0]), int(fila[1]), float(fila[2]), fila[3])
                
            linea += 1
    while(True):

        print("Ingrese ID de inicio: " )
        inicio = int(input())
        print("Ingrese ID de fin: " )
        fin = int(input())

        print("Buscando el camino con la distancia total más corta...")
        
        distancia = distanciaMasCorta(grafo,inicio,fin)
        if len(distancia) == 0:
            print("No se encontró una ruta")
        else:
            print("Camino más corto:", distancia)

main()