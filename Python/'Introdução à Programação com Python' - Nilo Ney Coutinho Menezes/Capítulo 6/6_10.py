""" ENUNCIADO:
Modifique o exercício anterior (6_9.py) de forma a pesquisar p e v em toda a lista e informando ao usuário
a posição onde 'p' e a posição onde 'v' foram encontrados
"""

lista = list(range(1,100))

p = int(input("Digite o primeiro valor a ser procurado: "))
v = int(input("Digite o segundo valor a ser procurado: "))

p_achou = False
v_achou = False

i = 0
while i < len(lista):
    if lista[i] == p:
        p_achou = True
        p_pos = i
    if lista[i] == v:
        v_achou = True
        v_pos = i
    i += 1

if p_achou: print(f"\nO número {p} foi encontrado na posição {p_pos}.")
else: print(f"\nO número {p} não foi encontrado.")
if v_achou: print(f"E o número {v}{' também ' if p_pos == v_pos else ' '}foi encontrado na posição {v_pos}.")
else: print(f"E o número {v}{' também ' if p_achou == v_achou else ' '}não foi encontrado.")