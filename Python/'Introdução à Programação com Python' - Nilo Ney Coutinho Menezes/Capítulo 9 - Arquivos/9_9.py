""" ENUNCIADO:
Crie um programa que receba uma lista de nomes de arquivo e os imprima, um por um.
"""

lidos = 0
while True:
    nome_arquivo = input(f"Digite o nome do {'próximo ' if lidos > 0 else ''}arquivo de texto ou Enter para encerrar o programa: ")
    if len(nome_arquivo) == 0:
        break
    nome_arquivo += ".txt"

    try:
        with open(nome_arquivo) as arquivo:
            print(f"Arquivo {nome_arquivo}: \n")
            for linha in arquivo.readlines():
                print(linha)
            print("\n\n")
            lidos += 1
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado, digite novamente.")
        continue

print(f"Programa encerrado com sucesso após ler {lidos} arquivos.")