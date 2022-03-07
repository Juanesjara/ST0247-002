def seAtacanHastaI(tablero, i):
    for j in range(0,i+1):
        for k in range(j+1,i+1):
            if abs(tablero[j]-tablero[k]) == abs(j-k) or tablero[j]==tablero[k]:
                return True
    return False
    
def nreinas(n:int):
    lista = nreinasAUX(n,0,[0]*n,tableroNreinas(n),[])
    return lista
def nreinasAUX(n:int,c:int,t:list,matriz,con:list):
    if n == c:
        con.append(t)
        return
    else:
        for f in range(n):
            if matriz[c][f] == True:
                t[c] = f
            else:
                pass
            if seAtacanHastaI(t,c):
                pass
            else:
                nreinasAUX(n,c+1,t,matriz,con)
    return len(con)

def tableroNreinas(n):
    listaLineas = []
    for linea in range(n):
        validacion = input()
        listTemporal = []
        for letra in validacion:
            if letra == '.':
                listTemporal.append(True)
            elif letra == '*':
                listTemporal.append(False)
        listaLineas.append(listTemporal)
    return listaLineas

def main():
    i = 1
    cases = 0
    respuestas = []
    while i == 1:
        n = int(input())
        if n == 0:
            i = 0
        else:
            respuestas.append(nreinas(n))
            cases = cases + 1 
    print(cases)
    for i in range(cases):
        print("Case " + str(i+1) + ":" + str(respuestas[i]))
main()