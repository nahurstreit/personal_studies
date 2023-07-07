""" ENUNCIADO:
Escreva um programa que leia três strings. Imprima o resultado da substituição na primeira,
dos caracteres da segunda pelos da terceira.
    Exemplo:
        1ª string: AATTCGAA
        2ª string: TG
        3ª string: AC
        Resultado: AAAACCAA
"""

string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")
string3 = input("Digite a terceira string: ")

if len(string2) != len(string3):
    print("Você digitou caracteres insuficientes para substituição.")
    print("A segunda e terceira strings devem ter o mesmo tamanho.")
else:
    string1_list = list(string1)
    for e in enumerate(string2):
        posicao, letra = e
        if letra in string1:
            while string1.find(letra) != -1:
                string1_list[string1.find(letra)] = string3[posicao]
                string1 = "".join(string1_list)
                
    print(f"Resultado: {string1}")