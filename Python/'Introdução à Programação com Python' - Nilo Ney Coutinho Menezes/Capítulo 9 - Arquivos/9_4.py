""" ENUNCIADO:
Crie um programa que receba o nome de dois arquivos como parâmetros da linha de comando e que gere 
um arquivo de saída com as linhas do primeiro e do segundo arquivo.
"""

import sys

def copiarArquivo(arquivoOrigem, arquivoDestino):
    try:
        with open(arquivoOrigem, "r") as arqOri, open(arquivoDestino, "a") as arqDest:
            arqDest.write(f"{arquivoOrigem}:\n")
            for linha in arqOri.readlines():
                arqDest.write(f"{linha}")
    except FileNotFoundError:
        raise FileNotFoundError(f"\nErro ao ler o arquivo: '{arquivoOrigem}'")
    except Exception as erro:
        raise erro

arquivo3 = input("Nome do arquivo de texto final (sem extensão '.txt'): ")

arquivo1, arquivo2 = None, None
params = list(sys.argv)
if len(params) > 2:
    arquivo1, arquivo2 = params[1], params[2]

while True:
    try:
        if arquivo1 is None:
            arquivo1 = input("Digite o nome do primeiro arquivo de texto (sem extensão '.txt'): ")
        try:
            copiarArquivo(arquivo1 + ".txt", arquivo3 + ".txt")
        except FileNotFoundError:
            arquivo1 = None
            raise
        if arquivo2 is None and arquivo1 is not None:
            arquivo2 = input("Digite o nome do segundo arquivo de texto (sem extensão '.txt'): ")
        try:
            copiarArquivo(arquivo2 + ".txt", arquivo3 + ".txt")
        except FileNotFoundError:
            arquivo2 = None
            raise
        if arquivo1 is not None and arquivo2 is not None:
            break
    except Exception as erro:
        print(erro)

print(f"Terceiro arquivo: '{arquivo3}.txt', criado com sucesso!")