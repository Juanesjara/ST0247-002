from collections import deque
class GraphAL:
    def __init__(self, size):
      self.arregloDeListas = [0]*size
      self.size = size
        #[size]
        #[ [], [], [], [] , [] ,[] ...]

      for i in range(0, size):
        self.arregloDeListas[i]= deque()
  
        
    def addArc(self, vertex, destination):
       fila = self.arregloDeListas[vertex-1]
       arco = (destination)
       fila.append(arco)
       fila = self.arregloDeListas[destination-1]
       arco = (vertex)
       fila.append(destination)
        

    def getSuccessors(self, source):
        otraListica = deque()
        laListaLlegada = self.arregloDeListas[source]
        for theDestination in laListaLlegada:
          otraListica.append(theDestination)
        return otraListica

def bienPintado(c:list, i:int, g)->bool:
  for vertice in range(0,i):
    elColorVertice = c[vertice]
    for sucesor in g.getSuccessors(vertice):
      if sucesor <= i:
        elColorSucesor = c[sucesor]
      if elColorVertice == elColorSucesor:
        return False
  return True

def sePuedePintarConMcolores(g, m:int)->bool:
  return pintarAUX(g, [0]*m,m,0)

def pintarAUX(g,c,m,v):
  if v == len(c):
    print(c)
    return True
  for color in range(0,m):
    c[v] = color
    if bienPintado(c, v, g):
      pudePintarIMasEnAdelante = pintarAUX(g, c, m, v+1)
      if pudePintarIMasEnAdelante:
        return True
  return False

    
def main():
  g = GraphAL(6)
  g.addArc(0, 1)
  g.addArc(1, 3)
  g.addArc(1, 6)
  g.addArc(3, 2)
  g.addArc(3, 6)
  g.addArc(2, 4)
  g.addArc(2, 5)
  g.addArc(4, 5)
  print(sePuedePintarConMcolores(g, 3))
main()