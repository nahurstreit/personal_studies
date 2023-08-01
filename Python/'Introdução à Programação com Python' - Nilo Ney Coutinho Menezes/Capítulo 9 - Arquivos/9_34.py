""" ENUNCIADO:
Altere o (Capítulo 7/programa7_2.py) o jogo da forca. Dessa vez, utilize as funções de tempo para
cronometrar a duração das partidas.
"""
import time

palavra = input("Digite a palavra secreta: ").lower().strip()
inicio = time.time()
for x in range(100):
    print()
digitadas = []
acertos = []
erros = 0
while True:
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else "."
    print(senha)
    if senha == palavra:
        print("Você acertou!")
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
            print("Enforcado!")
            break
fim = time.time()

duracao = time.gmtime(fim - inicio)

def criarStringTempo():
    hora = duracao.tm_hour
    minuto = duracao.tm_min
    segundo = duracao.tm_sec

    stringFinal = ''
    if hora != 0:
        stringFinal += f"{hora} hora{'s' if hora > 1 else ''}"
    if minuto != 0:
        if len(stringFinal) > 0:
            stringFinal += ", "
        stringFinal += f"{minuto} minuto{'s' if minuto > 1 else ''}"
    if len(stringFinal) > 0:
        stringFinal += "e "
    stringFinal += f"{segundo} segundo{'s' if segundo > 1 else ''}"

    return stringFinal

print(f"Sua partida durou: {criarStringTempo()}.")