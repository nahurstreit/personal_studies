""" ENUNCIADO:
Escreva um programa que compare duas listas. Utilizando operações com conjuntos, imprima:
    - os valores comuns às duas listas
    - os valores que só existem na primeira
    - os valores que existem apenas na segunda
    - uma lista com os elementos não repetidos das duas listas
    - a primeira lista sem os elementos repetidos na segunda
"""

a = [5, 1, 3, -2, 1, 2, 4, 5]
b = [3, 6, -3, 7, 5, 8, 9, 1]

print("Primeira lista: ", a)
print("Segunda lista: ", b)

a_ = set(a)
b_ = set(b)

print("Valores comuns às duas listas: ", (a_ - (a_ - b_)))

print("Valores que só existem na primeira: ", a_ - b_)

print("Valores que existem apenas na segunda: ", b_ - a_)

print("Lista com os elementos não repetidos das duas listas: ", ((a_ - b_) | (b_ - a_)))
    
print("Primeira lista sem os elementos repetidos na segunda: ", a_ - b_)