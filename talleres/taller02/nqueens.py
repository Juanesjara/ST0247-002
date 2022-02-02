def permutaciones(cadena):
      permutacionesAux(cadena,"")


def permutacionesAux(pregunta, respuesta):
  if len(pregunta) == 0:
    comprobarCombinacion(respuesta)
  else:
    for i in range(0,len(pregunta)):

      permutacionesAux( pregunta[0:i] + pregunta[i+1:] , respuesta+pregunta[i])

cont = 0
def comprobarCombinacion(cadena):
  for i in range(len(cadena)):
    for j in range(i+1,len(cadena)):
      if not comprobarDiagonal(i,j,int(cadena[i]), int(cadena[j])):
        return
  print(cadena)
 

def comprobarDiagonal(x1,x2,y1,y2):
    m =  (y2-y1)/(x2-x1) 
    return m != 1 and m != -1

def nreinas(n : int):
  nreinasAux(n, "")

def nreinasAux(n, combinaciones):
  cadena = ""
  for i in range(n):
    cadena += str(i)
  permutaciones(cadena)

def main():
  nreinas(8)

  
main()