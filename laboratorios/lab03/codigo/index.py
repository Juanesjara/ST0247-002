from collections import deque
import numpy as np
class GraphAL:
    def __init__(self, size):
      self.size = size
      self.arregloDeListas = [0]*size
        #[size]
        #[ [], [], [], [] , [] ,[] ...]

      for i in range(0, size):
        self.arregloDeListas[i]= deque()
  
        
    def addArc(self, vertex, destination, weight):
       fila = self.arregloDeListas[vertex-1]
       arco = (destination,weight)
       fila.append(arco)
        

    def getWeight(self, vertice, dest): 
      for i in self.arregloDeListas[vertice -1]:
        if dest == i[0]:
          return i[1]
      return None
        

    def getSuccessors(self, vertice): 
      succesors = []
      for i in self.arregloDeListas[vertice -1]:
        succesors.append(i[0])
      return succesors

    def hay_camino(self, source, dest):
      if dest not in self.getSuccessors(source):
        return False
      else:
        return True


def busquedadCaminoMasCortoBacktracking(graph, dest, source = 1):
  shortest_path = [source]
  visited = [False]*graph.size
  visited[source-1] = True
  print(visited)
  busquedadCaminoMasCortoBacktrackingAUX(graph, source, dest, shortest_path, visited)

def busquedadCaminoMasCortoBacktrackingAUX(graph, actual_index, dest, shortest_path, visited):
  if actual_index == dest:
    return shortest_path
  else:
    possible_sub_path = -1
    for i in range(0, graph.size ):
      if i != actual_index and visited[i-1] == False:
        possibble_next_vertex = i
        if graph.hay_camino(actual_index, possibble_next_vertex):
          next_vertex = possibble_next_vertex
      if graph.getWeight(actual_index, possible_sub_path) != None and graph.getWeight(actual_index, next_vertex) < graph.getWeight(actual_index, possible_sub_path):
        possible_sub_path = next_vertex
    shortest_path.append(possible_sub_path)
    return busquedadCaminoMasCortoBacktrackingAUX(graph, possible_sub_path, dest, shortest_path, visited) #cambio el sourcce para revisar uno por uno
    


size = 5
graph_list = GraphAL(size)

graph_list.addArc(1,2,2)
graph_list.addArc(2,1,2)
graph_list.addArc(2,5,5) 
graph_list.addArc(5,2,5)
graph_list.addArc(2,3,4)
graph_list.addArc(3,2,4)
graph_list.addArc(1,4,4)
graph_list.addArc(4,1,4)
graph_list.addArc(4,3,3)
graph_list.addArc(3,4,3)
graph_list.addArc(3,5,1)
graph_list.addArc(5,3,1)




print(busquedadCaminoMasCortoBacktracking(graph_list, 5))