""" ENUNCIADO:
Modifique o programa do exercício (9_7.py) para também receber o número de caracteres por linha e o número de
linhas por página pela linha de comando.
"""
import sys

PAGINA = 0

nome_arq_original = "arquivo-texto"
qtd_caracteres = 76
qtd_linhas = 60
nome_arq_saida = "arquivo-saida"

params = list(sys.argv)
if len(params) > 1:
    nome_arq_original = params[1]
if len(params) > 2:
    qtd_caracteres = int(params[2])
if len(params) > 3:
    qtd_linhas = int(params[3])
if len(params) > 4:
    nome_arq_saida = params[4]

def imprimirPagina():
    global PAGINA
    PAGINA += 1

    s_pagina_atual = f"Pagina {PAGINA}"
    espacos = qtd_caracteres - len(s_pagina_atual) - len(nome_arq_original)
    espacos = espacos if espacos >= 2 else 2

    fSaida.write(f"\n\n{nome_arq_original}{' ' * espacos}{s_pagina_atual}\n")
    fSaida.write(f"{'-' * qtd_caracteres}\n\n")

with open(f"{nome_arq_original}.txt", "r") as fOriginal:
    with open(f"{nome_arq_saida}.txt", "a") as fSaida:
        linhas_Pag = 0
        complementar = False
        impressaoFinal = False
        for linha in fOriginal.readlines():
            linha = linha.strip('\n')
            if complementar:
                linha = linha_limite + linha
                complementar = False
            while len(linha) > 0:
                if len(linha) < qtd_caracteres:
                    impressaoFinal = True
                linha_limite = linha[:qtd_caracteres]
                if len(linha_limite) < qtd_caracteres:
                    complementar = True
                    break
                linha = linha[qtd_caracteres:]
                fSaida.write(f"{linha_limite}\n")
                linhas_Pag += 1
                if linhas_Pag >= qtd_linhas:
                    linhas_Pag = 0
                    imprimirPagina()
        imprimirPagina()
        if impressaoFinal:
            fSaida.write(f"{linha}\n")