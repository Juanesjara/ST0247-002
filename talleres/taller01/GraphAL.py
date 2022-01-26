import numpy as np
from collections import deque
class GraphAL:
    def __init__(self, size):
        self.arregloDeListas = [0]*size
        for i in range(0,size):
            self.arregloDeListas[i] = deque()

    def addArc(self, vertex, destination, weight):
         fila = self.arregloDeListas[vertex]
         parejaDestinoPeso = (destination, weight)
         fila.append(parejaDestinoPeso)

    def getSuccessors(self, vertice):
    	for i in range(0,vertice):
       		successors = self.arregloDeListas
		return successors

    def getWeight(self, source, destination):
    	for i in range(0,destination):
        	wight = self.arregloDeListas
		return weight

    def __str__(self):


