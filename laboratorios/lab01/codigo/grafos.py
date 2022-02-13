from collections import deque
from tokenize import Double
class Graph:
    def __init__(self, vertices):
        self.vert = vertices
        self.glist = {}
        
        for vertice in vertices:
            self.glist[vertice] = []
    def addArc(self, u, v, peso):
        self.glist[u].append(v + ": " + str(peso) + "m")
        self.glist[v].append(u + ": " + str(peso) + "m")
        
    def imprimirLista(self):
        for vertice in self.vert:
            print(vertice + "->" + str(self.glist[vertice]))
            

            
def main():
    archivosMapa = open("./pruebaMapa.txt", "r")#funciona si los archivos de los vertices y los arcos estan separados
    archivosEsquinas = open("./esquinas.txt", "r")
    aE = archivosEsquinas.read()
    a = archivosMapa.read()
    separado =a.split("\n")
    listaLugares = []
    vertices = []
    dic = {}
    for texto in separado:
        textos = texto.split(" ")
        listaLugares.append(textos)
    for i in listaLugares:
       
        if len(i) == 3:
            i.append("Nombre Desconocido")
        elif(len(i) == 4):
            dic[i[0]] = i[3]
            vertices.append(i[3])
        elif(len(i) == 1):
            break
    esquinasSep = aE.split("\n")
    listaDistancias = []
    #verticesPrueba = ["house", "school", "mall"]
    grafo = Graph(vertices)
    #grafo.addArc("house", "mall", 10.4)
    #grafo.addArc("school", "mall",15.0)
    for texto2 in esquinasSep:
        textos = texto2.split(" ")
        listaDistancias.append(textos)
        grafo.addArc(dic.get(textos[0]), dic.get(textos[1]),float(textos[2]))
    grafo.imprimirLista()
    
main()
        