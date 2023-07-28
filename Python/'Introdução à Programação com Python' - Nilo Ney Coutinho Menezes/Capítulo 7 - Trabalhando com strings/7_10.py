""" ENUNCIADO:
Escreva um jogo da velha para dois jogadores.
O jogo deve perguntar onde você quer jogar e alternar entre dois jogadores.
A cada jogada, verifique se a posição está livre. Verifique também quando um jogador venceu a partida.
Um jogo da velha pode ser visto como uma lista de 3 elementos, na qual cada elemento é outra lista, também com
três elementos.
    Exemplo do jogo:
         X | 0 | 
        ---+---+---
           | X | X
        ---+---+---
           |   | 0
Em que cada posição pode ser vista como um número. Confira a seguir um exemplo das posições mapeadas para a 
mesma posição de seu teclado numérico.
         7 | 8 | 9
        ---+---+---
         4 | 5 | 6
        ---+---+---
         1 | 2 | 3
"""

print("{0} Jogo da velha {0}\n".format("#"*10))
# Escolhendo o jogador inicial
print("""Definindo o jogador inicial:
[1] para X ser o primeiro
[2] para O ser o primeiro""")
escolha = int(input("Quem vai começar? Escolha: "))
a, b = "X", "O" # Tupla dos jogadores
if escolha == 2:
    a, b = b, a # Inversão das tuplas
players = [a, b] # Definição da lista players com os valores da tupla a e b
player_i = 0

print(f"""\nO jogo funciona da seguinte maneira:
Cada posição do tabuleiro será como num teclado numérico, seguindo a ordem:
      
  7  |  8  |  9
-----+-----+-----
  4  |  5  |  6
-----+-----+-----
  1  |  2  |  3
      
Alternadamente os jogadores deverão selecionar um número do teclado numérico para encaixar na posição equivalente.
Vence o jogador que fizer uma linha, ocupando 3 posições consecutivas, com um de seus símbolos (X ou O).
A linha pode ser na horizontal, vertical ou até mesmo na diagonal.
      
O jogador inicial será o símbolo: {players[player_i]}. E as jogadas serão automaticamente alternadas.
Boa sorte e bom jogo!""")

qtd_jogos = 1
novamente = True
while novamente:
    print("\n\n{0} Jogo nº {1} {0}".format(("#"*5), qtd_jogos))
    # Definição de linhas como listas
    linha1 = [" ", " ", " "]
    linha2 = [" ", " ", " "]
    linha3 = [" ", " ", " "]

    # Criando a lista com as linhas
    jogo = [linha1, linha2, linha3]

    venceu = False
    while True:
        print()
        for e in enumerate(jogo):
            num_linha, linha = e
            print(f"  {linha[0]}  |  {linha[1]}  |  {linha[2]}")
            if num_linha < 2: print("-----+-----+-----")

        if venceu: # Critério de vitória colocado aqui, e não no final, para aparecer uma última vez o jogo
            print("""
       _  ____   _____          _____   ____  _____     __   __   __      ________ _   _  _____ ______ _    _ _ 
      | |/ __ \ / ____|   /\   |  __ \ / __ \|  __ \    \ \ / /   \ \    / /  ____| \ | |/ ____|  ____| |  | | |
      | | |  | | |  __   /  \  | |  | | |  | | |__) |    \ V /     \ \  / /| |__  |  \| | |    | |__  | |  | | |
  _   | | |  | | | |_ | / /\ \ | |  | | |  | |  _  /      > <       \ \/ / |  __| | . ` | |    |  __| | |  | | |
 | |__| | |__| | |__| |/ ____ \| |__| | |__| | | \ \     / . \       \  /  | |____| |\  | |____| |____| |__| |_|
  \____/ \____/ \_____/_/    \_\_____/ \____/|_|  \_\   /_/ \_\       \/   |______|_| \_|\_____|______|\____/(_)
                                                                                                                """
        if player_i == 0 else """
       _  ____   _____          _____   ____  _____       ____     __      ________ _   _  _____ ______ _    _ _ 
      | |/ __ \ / ____|   /\   |  __ \ / __ \|  __ \     / __ \    \ \    / /  ____| \ | |/ ____|  ____| |  | | |
      | | |  | | |  __   /  \  | |  | | |  | | |__) |   | |  | |    \ \  / /| |__  |  \| | |    | |__  | |  | | |
  _   | | |  | | | |_ | / /\ \ | |  | | |  | |  _  /    | |  | |     \ \/ / |  __| | . ` | |    |  __| | |  | | |
 | |__| | |__| | |__| |/ ____ \| |__| | |__| | | \ \    | |__| |      \  /  | |____| |\  | |____| |____| |__| |_|
  \____/ \____/ \_____/_/    \_\_____/ \____/|_|  \_\    \____/        \/   |______|_| \_|\_____|______|\____/(_)
                                                                                                                 """)
            print(f"\nJogo encerrado! O jogador '{players[player_i]}' venceu o jogo!")
            print("Deseja jogar novamente? O último vencedor joga primeiro.")
            escolha = input("(S/N): ").upper()
            if escolha not in "S":
                novamente = False
            break

        while True:
            jogada = input(f"\nVez do jogador '{players[player_i]}': ")
            if jogada.isdigit():
                jogada = int(jogada)
                if jogada >= 1 and jogada <= 9: break
            print("\nJogada inválida, digite apenas NÚMEROS de 1 a 9.")
        
        # Escolhendo a posição da linha e coluna com base no número digitado
        if jogada % 3 == 0: 
            pos_linha = 3 - (jogada // 3)
            pos_coluna = 2
        else:
            pos_linha, pos_coluna = divmod(jogada, 3)
            pos_linha = 2 - pos_linha
            pos_coluna -= 1
        
        if jogo[pos_linha][pos_coluna] in players:
            print("\nPosição já ocupada! Digite outro número.")
            continue

        jogo[pos_linha][pos_coluna] = players[player_i]

        # Fazendo a verificação de possibilidades de vitória
        # Verificando a diagonal principal
        if jogo[0][0] in players:
            if jogo[0][0] == jogo[1][1] and jogo[1][1] == jogo[2][2]:
                venceu = True

        # Verificando a diagonal secundária
        if jogo[0][2] in players:
            if jogo[0][2] == jogo[1][1] and jogo[1][1] == jogo[2][0]:
                venceu = True

        # Verificando as colunas
        for i in range(2):
            if jogo[0][i] not in players:
                continue
            if jogo[0][i] == jogo[1][i] and jogo [1][i] == jogo[2][i]:
                venceu = True

        # Verificando as linhas
        for linha in jogo:
            if (linha[0] == linha[1]) and (linha[1] == linha[2]) and linha[0] in players:
                venceu = True

        # Mudando o jogador atual
        if not venceu: player_i = (player_i + 1) % 2
    
    qtd_jogos += 1
    if not novamente: print("\nJogo encerrado! Obrigado por jogar!")