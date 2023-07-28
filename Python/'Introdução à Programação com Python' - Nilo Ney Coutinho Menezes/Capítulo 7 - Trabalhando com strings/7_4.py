""" ENUNCIADO:
Escreva um programa que leia uma string e imprima quantas vezes cada caractere aparece nessa string.
    Exemplo:
        1ª string: TTAAC
        Resultado:
            T: 2x
            A: 2x
            C: 1x
"""

string = input("Digite uma string: ")

for e in set(string):
    if e == " ": continue
    i = 0
    for letra in string:
        if letra == e:
            i += 1
    print(f"{e}: {i}x")