""" ENUNCIADO:
Faça um programa que percorra duas listas e gere uma terceira sem elementos repetidos.
"""

L1 = []
L2 = []
L3 = []

# Digitar a lista 1:
i = 1
while True:
    num = int(input(f"Digite o {i}º número da primeira lista (0 para parar): "))
    if num == 0:
        break
    L1.append(num)
    i += 1

print("\n")

# Digitar a lista 2:
i = 1
while True:
    num = int(input(f"Digite o {i}º número da segunda lista (0 para parar): "))
    if num == 0:
        break
    L2.append(num)
    i += 1


# Adicionar à terceira lista apenas os números únicos de L1:
i = 0
while i < len(L1):
    have = False
    j = 0
    while j < len(L3):
        if(L3[j] == L1[i]):
            have = True
            break
        j += 1

    if not have:
        L3.append(L1[i])
    i += 1

# Adicionar à terceira lista apenas os números únicos de L2 que já não foram colocados em L1:
i = 0
while i < len(L2):
    have = False
    j = 0
    while j < len(L3):
        if(L3[j] == L2[i]):
            have = True
            break
        j += 1

    if not have:
        L3.append(L2[i])
    i += 1


# Colocando em ordem crescente os valores de L3
LH = L3[:]
i = 0
while i < len(L3):
    j = 0
    bigger = len(L3) - 1
    while j < len(L3):
        if L3[i] < L3[j]:
            bigger -= 1
        j += 1
    LH[bigger] = L3[i]
    i += 1
L3 = LH[:]

# Exibindo a lista 1
print("\nLista 1: ")
i = 0
while i < len(L1):
    print(L1[i])
    i += 1

# Exibindo a lista 2
print("\nLista 2: ")
i = 0
while i < len(L2):
    print(L2[i])
    i += 1

# Exibindo a lista 3
print("\nLista 1 + Lista 2 = Lista 3: ")
i = 0
while i < len(L3):
    print(L3[i])
    i += 1