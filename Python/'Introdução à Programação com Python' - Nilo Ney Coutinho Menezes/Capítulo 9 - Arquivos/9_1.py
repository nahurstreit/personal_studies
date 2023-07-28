""" ENUNCIADO:
Escreva um programa que receba o nome de um arquivo pela linha de comando e que 
imprima todas as linhas desse arquivo.
"""

arq = input("Digite o nome do arquivo de texto: ")
arq += ".txt"

with open (arq, "r") as arquivo:
    for linha in arquivo.readlines():
        print(linha)