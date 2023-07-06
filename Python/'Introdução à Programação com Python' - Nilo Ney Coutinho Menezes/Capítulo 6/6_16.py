""" ENUNCIADO:
Modifique o programa para ordenar a lista em ordem decrescente. 
L = [1, 2, 3, 4, 5] deve ser ordenada como L = [5, 4, 3, 2, 1].
    Programa:
        L = [7, 4, 3, 12, 8]
        fim = 5
        while fim > 1:
            trocou = False
            i = 0
            while i < fim - 1:
                if L[i] > L[i + 1]:
                    trocou = True
                    temp = L[i]
                    L[i] = L[i + 1]
                    L[i + 1] = temp
                i += 1
            if not trocou:
                break
            fim -= 1
        for e in L:
            print(e)
"""

L = [1, 2, 3, 4, 5]
fim = len(L)
while fim > 1:
    trocou = False
    i = 0
    while i < fim - 1:
        if L[i] < L[i + 1]:
            trocou = True
            temp = L[i]
            L[i] = L[i + 1]
            L[i + 1] = temp
        i += 1
    if not trocou:
        break
    fim -= 1
for e in L:
    print(e)