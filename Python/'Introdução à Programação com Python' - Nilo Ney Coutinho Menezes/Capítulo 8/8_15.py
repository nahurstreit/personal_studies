""" ENUNCIADO:
Utilizando a função type, escreva uma função recursiva que imprima os elementos de uma lista.
Cada elemento deve ser impresso separadamente, um por linha.
Considere o caso de listas dentro de listas, como L = [1, [2, 3, 4, [5, 6, 7]]].
A cada nível imprima a lista mais à direita, como fazemos ao identar os blocos em Python.
Dica: envie o nível atual como parâmetro e utilize-o para calcular a quantidade de espaços em branco
à esquerda de cada elemento.
"""

import types

L = [1, [2, [3], 4, [5, [6], 7]], 8, [9]]

def printList(lista, level=0):
    for e in lista:
        if isinstance(e, list):
            printList(e, level + 1)
        elif not e is None:
            print(f"{' ' * (level * 3)}{e}")

printList(L)