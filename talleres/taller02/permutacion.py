def permutaciones(cadena):
  permutacionesAux(cadena,"")

def permutacionesAux(pregunta, respuesta):
    if len(pregunta)==len(respuesta):
        print(respuesta)
    else:
      for i in range(0,len(pregunta)):
        permutacionesAux( pregunta , respuesta+pregunta[i])


def main():        
    permutaciones("abc")
main()