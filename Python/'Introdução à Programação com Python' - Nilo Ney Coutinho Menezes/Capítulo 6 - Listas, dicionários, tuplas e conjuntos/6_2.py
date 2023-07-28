""" ENUNCIADO:
Faça um programa que leia duas listas e que gere uma terceira com os elementos das duas primeiras.
"""

L1 = []
L2 = []
L3 = []

i = 1
while True:
    num = int(input(f"Digite o {i}º número da primeira lista (0 para parar): "))
    if num == 0:
        break
    L1.append(num)
    i += 1

print("\n")
i = 1
while True:
    num = int(input(f"Digite o {i}º número da segunda lista (0 para parar): "))
    if num == 0:
        break
    L2.append(num)
    i += 1

L3.extend(L1)
L3.extend(L2)

print("\nLista 1: ")
i = 0
while i < len(L1):
    print(L1[i])
    i += 1

print("\nLista 2: ")
i = 0
while i < len(L2):
    print(L2[i])
    i += 1

print("\nLista 1 + Lista 2 = Lista 3: ")
i = 0
while i < len(L3):
    print(L3[i])
    i += 1