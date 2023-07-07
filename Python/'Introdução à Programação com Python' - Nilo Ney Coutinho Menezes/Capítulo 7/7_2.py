""" ENUNCIADO:
Escreva um programa que leia duas strings e gere uma terceira com os caracteres comuns às duas strings lidas.
    Exemplo:
        1ª string: AAACTBF
        2ª string: CBT
        Resultado: CBT
A ordem dos caracteres da string gerada não é importante, mas deve conter todas as letras comuns a ambas.
"""

string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")

string3 = ""

for letra in string2:
    if letra in string1:
        string3 += letra

print(f"Resultado: {string3}")