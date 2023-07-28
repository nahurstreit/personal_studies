""" ENUNCIADO:
Crie um programa que leia um arquivo e crie um dicionário em que cada chave é uma palavra e cada valor é o
número de ocorrências no arquivo.
"""

dicionario = {}

while True:
    nome_arquivo = input("Digite o nome do arquivo: ") + ".txt"
    try:
        with open(nome_arquivo) as arquivo:
            for linha in arquivo.readlines():
                linha = linha.lower().replace(",", "")
                conteudoLinha = linha.split(" ")
                for palavra in conteudoLinha:
                    if palavra not in dicionario:
                        dicionario[palavra] = 1
                    else:
                        dicionario[palavra] += 1
        break

    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado. Digite novamente.")
        continue

print(dicionario)