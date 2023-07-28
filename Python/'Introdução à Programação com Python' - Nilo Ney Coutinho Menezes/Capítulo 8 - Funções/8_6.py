""" ENUNCIADO:
Reescreva o programa de forma a utilizar for em vez de while.
    Programa:
        def soma(L):
            total = 0
            x = 0
            while x < 5:
                total += 1
            return total

        L = [1, 7, 2, 9, 15]
        print(soma(L))
        print(soma([7, 9, 12, 3, 100, 20, 4]))
"""

def soma(L):
    total = 0
    for num in L:
        total += num
    return total

L = [1, 7, 2, 9, 15]
print(soma(L))
print(soma([7, 9, 12, 3, 100, 20, 4]))