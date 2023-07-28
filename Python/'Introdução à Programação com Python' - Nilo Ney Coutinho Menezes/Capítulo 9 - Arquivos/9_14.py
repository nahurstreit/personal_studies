""" ENUNCIADO:
Crie um programa que leia um arquivo-texto e elimine os espaços repetidos entre as palavras e no fim das linhas.
O arquivo de saída também não deve ter mais de uma linha em branco repetida.
"""

while True:
    try:
        nome_arquivo = input("Digite o nome do arquivo original: ")
        if nome_arquivo.find(".txt") == -1:
            nome_arquivo += ".txt"
        with open(nome_arquivo, "r") as original:
            nome_arquivoSaida = input("\nDigite o nome para o arquivo final: ")
            if nome_arquivoSaida.find(".txt") == -1:
                nome_arquivoSaida += ".txt"
            with open(nome_arquivoSaida, "a") as final:
                branco = 0
                for linha in original.readlines():
                    linha = linha.rstrip().rstrip('\n').replace("  ", "")
                    if len(linha) == 0:
                        if branco > 0:
                            continue
                        branco += 1
                    else:
                        branco = 0
                    final.write(linha + '\n')
        break
    except FileNotFoundError:
        print(f"O arquivo com nome '{nome_arquivo}' não pôde ser encontrado, digite novamente.")
        continue