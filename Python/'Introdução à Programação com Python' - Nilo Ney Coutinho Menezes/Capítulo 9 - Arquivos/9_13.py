""" ENUNCIADO:
Crie um programa que imprima as linhas de um arquivo. Esse programa deve receber três parâmetros pela
linha de comando: o nome do arquivo, a linha inicial e a última linha a imprimir.
"""

import sys

nome_arquivo = None
linha_inicial = 0
linha_final = None

params = list(sys.argv)
if len(params) > 1:
    nome_arquivo = params[1]
if len(params) > 2:
    linha_inicial = int(params[2])
if len(params) > 3:
    linha_final = int(params[3])

while True:
    try:
        if nome_arquivo == None:
            nome_arquivo = input("Digite o nome do arquivo: ")
        if nome_arquivo.find(".txt") == -1:
            nome_arquivo += ".txt"
        with open(nome_arquivo) as arquivo:
            contarLinha = 1
            for linha in arquivo.readlines():
                if contarLinha >= linha_inicial:
                    print(linha)
                if linha_final != None:
                    if contarLinha > linha_final - 1:
                        break
                contarLinha += 1
        break
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não pôde ser encontrado, digite novamente.")
        nome_arquivo = None
        continue