""" ENUNCIADO:
Altere o (programa7_2.py), o jogo da forca. Utilize um arquivo em que uma palavra seja gravada a cada linha.
Use um editor de textos para gerar o arquivo. Ao iniciar o programa, utilize esse arquivo para carregar (ler) a
lista de palavras. Experimente também perguntar o nome do jogador e gerar um arquivo com o número de acertos
dos cinco melhores.
"""

import random

ARQUIVO_PALAVRAS = "palavras9_15.txt"
ARQUIVO_JOGADORES = "jogadores9_15.txt"

digitadas = []
acertos = []
erros = 0
palavras = []
jogadores = []

try:
    with open(ARQUIVO_PALAVRAS, "r") as arq_palavras:
        for linha in arq_palavras.readlines():
            palavras.append(linha)
    with open(ARQUIVO_JOGADORES, "r") as arq_jogadores:
        for linha in arq_jogadores.readlines():
            linha = linha.strip('\n')
            jogador = linha.split("-")
            jogadores.append((int(jogador[0]), jogador[1]))
except Exception as erro:
    print(erro)

palavra = random.choice(palavras).lower().strip('\n')
nome_jogador = input("Digite o nome do jogador: ")

while True:
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else "."
    print(senha)
    if senha == palavra:
        print("Você acertou!")
        jogadores.append(((len(acertos) - erros), nome_jogador))
        break
    tentativa = input("\nDigite uma letra: ").lower().strip()
    if tentativa in digitadas:
        print("Você já tentou esta letra!")
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print("Você errou!")
        print("X==:==\nX  :  ")
        print("X  0  " if erros >= 1 else "X")
        linha2 = ""
        if erros == 2:
            linha2 = "  |  "
        elif erros == 3:
            linha2 = " \|  "
        elif erros >= 4:
            linha2 = " \|/ "
        print(f"X{linha2}")
        linha3 = ""
        if erros == 5:
            linha3 = " /  "
        elif erros >= 6:
            linha3 = " / \ "
        print(f"X{linha3}")
        print("X\n===========")
        if erros == 6:
            print(f"Enforcado!\nA palavra era: {palavra}!")
            break


print("\nMelhores 5 pontuações:")
jogadores.sort(reverse=True)
rank = 5 if len(jogadores) > 5 else len(jogadores)
for i in range(rank):
    print(f"{jogadores[i][1]} - {jogadores[i][0]} pontos")

try:
    with open(ARQUIVO_JOGADORES, "w") as arq_jogadores:
        rank = 5 if len(jogadores) > 5 else len(jogadores)
        for i in range(rank):
            arq_jogadores.write(f"{jogadores[i][0]}-{jogadores[i][1]}")
            if i < (rank - 1): arq_jogadores.write("\n")
except Exception as erro:
    print(erro)