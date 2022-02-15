import math
infinito = math.inf

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
        lista = self.arregloDeListas[source]
        for i in lista:
            if i[0] == destination:
                peso = i[1]
        return peso
    
    
      
    def getSuccessors(self, source):
        lista = []
        arreglo = self.arregloDeListas[source]
        for i in arreglo:
            if i[1]:
                lista.append(i[0])
        return lista
          


def costoDelMasCorto(g,o:int,d:int)->int:
  arregloDeVisitados = [False]*g.size
  return costoDelMasCortoAUX(g,o,d,arregloDeVisitados)

def costoDelMasCortoAUX(g,o:int,d:int,a:list)->int:
  a[o] = True
  if o == d:
    return 0
  else:
    elCostoDelMasCorto = math.inf
    for vecino in g.getSuccessors(o):
      if not a[vecino]:
        elCostoDelMasCortoDesdeElVecinoHastaD:int = costoDelMasCortoAUX(g,vecino,d,a)
        elCostoDelMasCortoDesdeOHastaDPasandoPorElVecino = g.getWeight(o,vecino) + elCostoDelMasCortoDesdeElVecinoHastaD
        if elCostoDelMasCortoDesdeOHastaDPasandoPorElVecino < elCostoDelMasCorto:
          elCostoDelMasCorto = elCostoDelMasCortoDesdeOHastaDPasandoPorElVecino
    return elCostoDelMasCorto

def main():
  size = 5
  g = GraphAL(size)
  g.addArc(0,1,1)
  g.addArc(0,2,3)
  g.addArc(2,3,3)
  g.addArc(3,0,1)
  g.addArc(3,4,6) 
  print(g.getSuccessors(0))
  print(costoDelMasCorto(g,0,3))
  
main()