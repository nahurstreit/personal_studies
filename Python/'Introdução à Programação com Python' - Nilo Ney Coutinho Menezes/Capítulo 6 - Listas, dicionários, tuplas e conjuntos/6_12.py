""" ENUNCIADO:
Altere o programa de forma a imprimir o menor elemento da lista.
    Programa:
        L = [1, 7, 2, 4]
        maximo = L[0]
        for e in L:
            if e > maximo:
                maximo = e
        print(maximo)
"""

L = [1, 7, 2, 4]
min = L[0]
for e in L:
    if e < min:
        min = e
print(min)