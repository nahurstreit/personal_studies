""" ENUNCIADO:
Modifique o programa usando for.
    Programa - Adição de elementos à lista
        L = []
        while True:
            n = int(input("Digite um número (0 sai): "))
            if n == 0:
                break
            L.append(n)
        x = 0
        while x < len(L):
            print(L[x])
            x += 1
"""

L = []
while True:
    n = int(input("Digite um número (0 sai): "))
    if n == 0:
        break
    L.append(n)
for i in L:
    print(i)