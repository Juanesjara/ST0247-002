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
      return self.arregloDeListas[source][destination] 
      
    def getSuccessors(self, source):
      otraListica = deque()
      laListaLlegada = self.arregloDeListas[source]
      for (theDestination,theWeight) in laListaLlegada:
          otraListica.append(theDestination)
      return otraListica
          

def hayCamino(g,o:int,d:int)->bool:
    tablaHashDeVisitados = [False]*g.size
    return hayCaminoAUX(g,o,d,tablaHashDeVisitados)
    
def hayCaminoAUX(g, o:int, d:int, tablaHashDeVisitados)->bool:
  tablaHashDeVisitados[o] = True #Digo que ya visité a o
  if o==d: #Si el origen es igual al destino
    return True
  else:
    for vecino in g.getSuccessors(o): #Para cada vecino en los sucesores de o
      if not tablaHashDeVisitados[vecino]: #Si no está visitado el vecino en la tabla
        hayCaminoDelVecinoAd = hayCaminoAUX(g,vecino,d, tablaHashDeVisitados)
        if hayCaminoDelVecinoAd:
          return True
    return False #·Si nunca dio verdadero, es falso

def main():
  g = GraphAL(5)
  g.addArc(0,1,10)
  g.addArc(0,2,1)
  g.addArc(2,3,2)
  g.addArc(3,0,2)
  g.addArc(3,4,3) 
  print(hayCamino(g,0,4))  
  print(hayCamino(g,1,4)) 
  print(hayCamino(g,1,2))   
  
main()
