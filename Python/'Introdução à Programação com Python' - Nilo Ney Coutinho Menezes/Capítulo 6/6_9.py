""" ENUNCIADO:
Modifique o (programa6_7.py) para pesquisar dois valores. Em vez de apenas p, leia outro valor v que também será procurado.
Na impressão, indique qual dos dois valores foi achado primeiro.
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
        break
    if lista[i] == v:
        v_achou = True
        break
    i += 1

if p == v and (p_achou or v_achou): print(f"Esses números serão encontrados juntos pois são iguais!")
elif p_achou: print(f"O número {p} foi encontrado primeiro!")
elif v_achou: print(f"O número {v} foi encontrado primeiro!")
else: print(f"Nenhum desses números pôde ser encontrado.")