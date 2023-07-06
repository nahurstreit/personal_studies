""" ENUNCIADO:
Escreva um programa que gere um dicionário por uma frase lida, e que cada chave seja um caractere e seu valor seja
o número de vezes que esse caractere foi encontrado na frase.
Exemplo: O rato roeu -> {'O': 1, 'r': 2, 'a': 1, 't': 1, 'o': 2, 'e': 1, 'u': 1}
"""

frase = input("Digite uma frase: ")

di = {}

for letra in frase:
    if letra == ' ': continue
    if letra in di:
        di[letra] += 1
    else:
        di[letra] = 1

print(di)