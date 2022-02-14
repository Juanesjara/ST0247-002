def esBicolorable(listArc):
    col1 = []
    col2 = []
    for i in range(len(listArc)):
        if listArc[i][0] not in col1 and listArc[i][0] not in col2:
            col1.append(listArc[i][0])
            if listArc[i][1] in col1:
                return("NOT BICOLOREABLE")
            else:
                col2.append(listArc[i][1])
        elif listArc[i][0] in col1:
            if listArc[i][1] in col1:
                return("NOT BICOLOREABLE")
            else:
                col2.append(listArc[i][1])
        elif listArc[i][0] in col2:
            if listArc[i][1] in col2:
                return("NOT BICOLOREABLE")
            else:
                col1.append(listArc[i][1])
    return("BICOLOREABLE")



def main():
    id = 1
    listAns = []
    while id != 0:
        numVer = int(input())
        if numVer == 0:
            id = 0
        else:
            numArc = int(input())
            listArc = []
            for i in range(numArc):
                m, n = map(int, input().split())
                listArc.append((m, n))
            listAns.append(esBicolorable(listArc))
    for i in listAns:
        print(i)

main()

