def hayCamino(g, o:int, d:int, visitados:list)->bool:
      if o == d:
        return True
      else:
        for vecino in g.getSuccessors(o):
            hayCaminoDelVecinoAd = hayCamino(g,vecino,d)
        if hayCaminoDelVecinoAd:
            return True
        return False #·Si nunca dio verdadero, es falso