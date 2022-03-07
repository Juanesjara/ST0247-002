def seAtacanHastaI(tablero, i):
  for j in range(0,i+1):
    for k in range(j+1,i+1):
        if abs(tablero[j]-tablero[k]) == abs(j-k) or tablero[j]==tablero[k]:
          return True
  return False
    
def nreinas(n:int):
  lista = nreinasAUX(n,0,[0]*n)
  return lista
def nreinasAUX(n:int,c:int,t:list):
  if n == c:
    print(t) 
  else:
    for f in range(n):
      t[c] = f
      if seAtacanHastaI(t,c):
        pass
      else:
        nreinasAUX(n,c+1,t)

def main():
  nreinas(4)
main()