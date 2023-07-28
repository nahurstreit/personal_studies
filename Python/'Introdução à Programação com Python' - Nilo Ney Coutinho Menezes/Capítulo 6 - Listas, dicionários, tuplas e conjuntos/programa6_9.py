""" 
Cópia do Programa 6.9 do livro (página 110 - Capítulo 6) - Pesquisa sequencial
Necessário para a resolução dos exercícios (6_8.py), (6_9.py) e (6_10.py).
"""

L = [15, 7, 27, 39]
p = int(input("Digite o valor a procurar: "))
achou = False
i = 0
while i < len(L):
    if L[i] == p:
        achou = True
        break
    i += 1
if achou:
    print(f"{p} achado na posição {i}.")
else:
    print(f"{p} não encontrado.")