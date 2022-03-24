def busquedaBinaria(arreglo : list, valor: int) -> int:
    return busquedaBinariaAux(arreglo, valor, 0, len(arreglo)-1)

def busquedaBinariaAux(arreglo : list, valor : int, elIndiceDeMasALaIzquierda : int, elIndiceDeMasALaDerecha):
  mitad = (elIndiceDeMasALaDerecha + elIndiceDeMasALaIzquierda) // 2
  if elIndiceDeMasALaIzquierda > elIndiceDeMasALaDerecha:
    return -1
  if valor == arreglo[mitad]:
    return mitad
  if valor < arreglo[mitad]:
    return busquedaBinariaAux(arreglo, valor, elIndiceDeMasALaIzquierda, mitad - 1)
  else: # es mayor
    return busquedaBinariaAux(arreglo, valor, mitad + 1, elIndiceDeMasALaDerecha)
  # 1 llamados de n/2 = O(log2 n)
  
  
#https://www.youtube.com/watch?v=JSceec-wEyw


def juntarListas2(arreglo1:list, arreglo2:list):
    j = 0;
    i = 0;
    templist = []
    while i < len(arreglo1) and j<len(arreglo2):
        if(arreglo1[i]<arreglo2[j]):
            templist.append(arreglo1[i])
            i += 1
        else:
            templist.append(arreglo2[j])
            j += 1 
    templist += arreglo1[i:]
    templist += arreglo2[j:]
    return templist
def main():
    #arreglo1 = [1,4,6,7,9]
    #arreglo2 = [2,3,5,8,10,11]
    #print(juntarListas2(arreglo1, arreglo2))
    arreglo = [10,20,30,40,50,55,60]
    print(busquedaBinaria(arreglo,10))
    print(busquedaBinaria(arreglo,60))
    print(busquedaBinaria(arreglo,30))
    #print(busquedaBinaria(arreglo,0))
    print(busquedaBinaria(arreglo,80))
    #print(busquedaBinaria(arreglo,41))
main()



