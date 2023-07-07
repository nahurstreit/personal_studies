""" ENUNCIADO:
Escreva um programa que leia duas strings. 
Verifique se a segunda ocorre dentro da primeira e imprima a posição de início.
    Exemplo:
        1ª string: AABBEFAATT
        2ª string: BE
        Resultado: BE encontrado na posição 3 de AABBEFAATT
"""

string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")

if string2 in string1:
    print(f"{string2} encontrado na posição {string1.find(string2)} de {string1}")
else:
    print("A segunda string não está contida na primeira.")