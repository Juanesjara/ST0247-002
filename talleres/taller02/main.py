def subconjuntosDeUna(cadena):
      subconjuntosAux(cadena, "")
  
def subconjuntosAux(pregunta, respuesta):
  if len(pregunta)==0:
    print(respuesta)
    return None
  else:
    subconjuntosAux(pregunta[1:],respuesta+pregunta[0])
    subconjuntosAux(pregunta[1:],respuesta)
    return None
def permutaciones(cadena):
      permutacionesAux(cadena,"")

def permutacionesAux(pregunta, respuesta):
    if len(pregunta)==0:
        print(respuesta)
    else:
        for i in range(0,len(pregunta)):
            nuevaPregunta = pregunta[0:i]+pregunta[i+1:]
            permutacionesAux( nuevaPregunta , respuesta+pregunta[i])

def nQueens(n :int):
    texto = ""
    for i in range(n):
        texto = texto + str(i) 
    permutaciones(texto)



def subconjuntosDeUna(cadena):
      subconjuntosAux(cadena, "")
  
def subconjuntosAux(pregunta, respuesta):
  if len(pregunta)==0:
    print(respuesta)
    return None
  else:
    subconjuntosAux(pregunta[1:],respuesta+pregunta[0])
    subconjuntosAux(pregunta[1:],respuesta)
    return None

def permutaciones(cadena):
  permutacionesAux2(cadena,"")





def permutacionesAux(pregunta, respuesta):
  if len(pregunta) == 0:
    comprobarCombinacion(respuesta)
  else:
    for i in range(0,len(pregunta)):

      permutacionesAux( pregunta[0:i] + pregunta[i+1:] , respuesta+pregunta[i])

def permutacionesAux2(pregunta, respuesta):
  if len(pregunta) == 2:
    print(respuesta)
  else:
    for i in range(0,len(pregunta)):

      permutacionesAux( pregunta[0:i] + pregunta[i+1:] , respuesta+pregunta[i])

def comprobarCombinacion(cadena):
  for i in range(len(cadena)):
    for j in range(i+1,len(cadena)):
      if not comprobarDiagonal(i,j,int(cadena[i]), int(cadena[j])):
        return
  print(cadena)

def comprobarDiagonal(x1,x2,y1,y2):
  return (y2-y1)/(x2-x1) != 1 and (y2-y1)/(x2-x1) != -1

def nreinas(n : int):
  nreinasAux(n, "")

def nreinasAux(n, combinaciones):
  cadena = ""
  for i in range(n):
    cadena += str(i)
  permutaciones(cadena)




def main():        
    #subconjuntosDeUna("abc")
    #print("permutaciones")
    #permutaciones("abc")
    nreinas(8)
    
    
main()