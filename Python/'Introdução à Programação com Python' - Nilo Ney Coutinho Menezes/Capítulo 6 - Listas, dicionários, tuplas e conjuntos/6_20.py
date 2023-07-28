""" ENUNCIADO:
Escreva um programa que compare duas listas. Considere a primeira lista como a versão inicial e a segunda como
a versão após alterações. Utilizando operações com conjuntos, seu programa deverá imprimir a lista de modificações
entre essas duas versões, listando:
    - os elementos que não mudaram
    - os novos elementos
    - os elementos que foram removidos
"""

a = [-1, 3, 5, 6, 1, 2, 4, 9]
b = [-1, 8, 5, 6, 7, 3, 2, 4, 10]

print("Lista antiga: ", a)
print("Lista nova: ", b)

a_ = set(a)
b_ = set(b)

print("\nModificações")
print("Elementos que permaneceram: ", a_ - (a_ - b_))
print("Novos elementos: ", b_ - a_)
print("Elementos removidos: ", a_ - b_)