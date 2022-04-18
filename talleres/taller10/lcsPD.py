import numpy as np

def lcsDP(x, y, A : str,B : str):
  tabla = np.zeros(  (x,y)  )
  for i in range(0,y): # cond parada
    tabla[0][i] = 0
  for j in range(0,x): # cond parada
    tabla[j][0] = 0
  for i in range(0,x): # cond recursiva
    for j in range(0,y):
      if A[i] == B[j]:
        if i == 0 or j == 0:
          tabla[i][j] = 1
        else:
          tabla[i][j] = 1 + tabla[i-1][j-1]
      else:
        tabla[i][j] = max(tabla[i-1][j], tabla[i][j-1] )
  return int(tabla[x-1][y-1])



def main():
  s1 = "ABC"
  s2 = "ABCD"
  x = 3
  y = 4
  print(lcsDP(x,y,s1,s2))

main()