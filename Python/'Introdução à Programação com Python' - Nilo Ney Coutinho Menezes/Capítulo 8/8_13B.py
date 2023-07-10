""" ENUNCIADO:
Altere o programa de forma que o usuário tenha três chances de acertar o número.
O programa termina se o usuário acertar ou errar três vezes
    Programa:
        import random
        n = random.randint(1, 10)
        x = int(input("Escolha um número entre 1 e 10"))
        if x == n:
            print("Você acertou!")
        else:
            print("Você errou.")
"""

import random

tentativas_QtdMax = 3
minimo = 1
maximo = 10

n = random.randint(minimo, maximo)
tentativas = 0
while True:
    try:
        x = int(input(f"Escolha um número entre {minimo} e {maximo}: "))
        if x == n:
            print("Você acertou!")
            n = random.randint(minimo, maximo)
        else:
            print("Você errou.")
        
        tentativas += 1
        if tentativas == tentativas_QtdMax: break
    except ValueError:
        print("Digite apenas números!")