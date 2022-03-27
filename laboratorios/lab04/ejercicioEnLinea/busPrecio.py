def horasExtra(l1:list,l2:list,k:int,extra):
    if l1 == []:
        return(extra)
    else:
        min1 = min(l1)
        max2 = max(l2)
        l1.remove(min1)
        l2.remove(max2)
        resultado = int(min1) + int(max2)
        precioExtra = resultado - k
        if precioExtra <= 0:
            return horasExtra(l1,l2,k,extra)
        else:
            return horasExtra(l1,l2,k,extra + precioExtra)

def main():
    listaRespuestas = []
    i = 1
    while(i == 1):
        n, k, c= map(int, input().split())
        if n == 0 and k == 0 and c == 0:
            for i in listaRespuestas:
                print(i)
            i = 0
        else:
            a = input()
            b = input()
            dividido1 = a.split()
            dividido2 = b.split()
            valorExtra = horasExtra(dividido1,dividido2,k,0)
            valorFinal = valorExtra * c
            listaRespuestas.append(valorFinal)

main()

