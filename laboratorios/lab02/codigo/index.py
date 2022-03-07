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
    
def comprobarDiagonal(x1,x2,y1,y2):
    m =  (y2-y1)/(x2-x1) 
    return m != 1 and m != -1

def comprobarCombinacion(cadena):
    for i in range(len(cadena)):
        for j in range(i+1,len(cadena)):
            if not comprobarDiagonal(i,j,int(cadena[i]), int(cadena[j])):
                return
    print(cadena)
  

def permutacionesCreacionLista(arc,lista):
    lista.append(arc)

def permutaciones(cadena, lista:list):
    permutacionesAux(cadena,"", lista)
    

def permutacionesAux(pregunta, respuesta, lista:list):
    if len(pregunta)==len(respuesta):
        
        final = respuesta + respuesta[0]
        
        lista.append(final)
        return
    else:
      for i in range(0,len(pregunta)):
        permutacionesAux( pregunta , respuesta+pregunta[i],lista)
        
def grafoAString(g):
    cadena = ""
    for i in range(g.size):
        cadena = cadena + str(i)
    return cadena
    
def HayCaminoHamiltoniano(g,inicio, final):
    siguientes = g.getSuccessors(int(inicio))
    if int(final) in g.getSuccessors(int(inicio)):
        return True
    else: return False
    
    


def fuerzaBruta(g):
    stringGrafo = grafoAString(g)
    listaPermutaciones = []
    permutaciones(stringGrafo, listaPermutaciones)
    listaPermutacionesConCamino = []
    for j in listaPermutaciones:
        resultado = True
        for i in range (len(j)):
            if int(i) == int(len(j))-1:
                #resultado = HayCaminoHamiltoniano(g,j[i],j[0])
                print("acabe de comparar",j[i],j[0],"resultado", resultado)
                print(resultado, "aqui compruebo el ultimo y el primero")
            else:
                resultado = HayCaminoHamiltoniano(g,j[i],j[i+1])
                #print("acabe de comparar",j[i],j[i+1],"resultado", resultado)
                #print(resultado, "aqui")
            if resultado == False:
                #print("me rompi")
                break
            else:
                continue
        if resultado == True:
            listaPermutacionesConCamino.append(j)
    print(listaPermutacionesConCamino) 
    arcMenor = ""
    pesoMax = 100000000000000000000 
    for j in listaPermutacionesConCamino:
        pesoAcum = 0
        for i in range(len(j)):
            if int(i) == int(len(j))-1:
                pesoAcum += g.getWeight((int(j[i])),(int(j[0])))
            else: 
                pesoAcum += g.getWeight((int(j[i])),(int(j[i+1])))
        if pesoAcum < pesoMax:
            pesoMax = pesoAcum
            arcMenor = j
    print("El camino con menos peso es:")
    for x in range (len(arcMenor)):
        if x < len(arcMenor)-1:
            print(arcMenor[x], "->", end=" ")
        else: 
            print(arcMenor[x])
    print(arcMenor)
            
    print("Con un peso de", pesoMax)
                
         
def main():
    size = 3
    g = GraphAL(size)
    g.addArc(0,1,3)
    g.addArc(0,2,2)
    g.addArc(1,0,3)
    g.addArc(1,2,1)
    g.addArc(2,0,2)
    g.addArc(2,1,1)
    fuerzaBruta(g)
   


main()