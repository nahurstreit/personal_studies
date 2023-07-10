""" ENUNCIADO:
Reescreva o programa de forma a utilizar os métodos de pesquisa em lista, vistos no Capítulo 7.
    Programa:
        def pesquise(lista, valor):
            for x, e in enumerate(lista):
                if e == valor:
                    return x
                return None
        L = [10, 20, 25, 30]
        print(pesquise(L, 25))
        print(pesquise(L, 27))
"""

def pesquise(lista, valor):
    if valor in lista:
        return lista.index(valor)
    return None

L = [10, 20, 25, 30]
print(pesquise(L, 25))
print(pesquise(L, 27))