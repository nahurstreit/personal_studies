""" ENUNCIADO:
Escreva um programa que leia duas strings e gere uma terceira com os caracteres que aparecem apenas em uma delas.
    Exemplo:
        1ª string: CTA
        2ª string: ABC
        3ª string: BT
A ordem dos caracteres da terceira string não é importante.
"""

string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")
string3 = ""

for letra in string1:
    if letra not in string2 and letra not in string3:
        string3 += letra

for letra in string2:
    if letra not in string1 and letra not in string3:
        string3 += letra

print(f"Resultado: {string3}" if len(string3) > 0 else "As strings são iguais.") 