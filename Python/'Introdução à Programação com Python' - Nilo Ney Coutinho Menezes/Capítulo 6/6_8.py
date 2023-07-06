""" ENUNCIADO:
Modifique o (programa6_7.py) de forma a realizar a mesma tarefa de busca, mas sem utilizar a variável achou.
Dica: observe a condição de saída do while.
"""

L = [15, 7, 27, 39]
p = int(input("Digite o valor a procurar: "))
i = 0
while L[i] != p:
    i += 1
    if i >= len(L):
        break

if i >= len(L): print(f"{p} não encontrado.")
else: print(f"{p} encontrado na posição [{i}] da lista.")
