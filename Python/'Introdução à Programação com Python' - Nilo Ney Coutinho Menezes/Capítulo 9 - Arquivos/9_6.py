""" ENUNCIADO:
Modifique o programa para imprimir 40 vezes o simbolo de '=' se este for o primeiro caractere da linha
de um arquivo. Adicione também a opção para parar de imprimir até que se pressione a tecla Enter cada vez
que uma linha iniciar com . (ponto) como primeiro caractere.
    Programa - Processamento de um arquivo
        LARGURA = 79
        with open("entrada.txt") as entrada:
            for linha in entrada.readlines():
                if linha[0] == ";":
                    continue
                elif linha[0] == ">":
                    print(linha[1:].rjust(LARGURA))
                elif linha[0] == "*":
                    print(linha[1:].center(LARGURA))
                else:
                    print(linha)
"""

LARGURA = 79
with open("entrada.txt") as entrada:
    for linha in entrada.readlines():
        if linha[0] == ";":
            continue
        elif linha[0] == ">":
            print(linha[1:].rjust(LARGURA))
        elif linha[0] == "*":
            print(linha[1:].center(LARGURA))
        elif linha[0] == "=":
            print(f"{'=' * 40}")
        elif linha[0] == ".":
            input("Pressione Enter para continuar a imprimir.")
            print()
        else:
            print(linha)