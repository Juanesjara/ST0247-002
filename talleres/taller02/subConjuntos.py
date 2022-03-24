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

def main():
    subconjuntosDeUna("abc")
    
main()