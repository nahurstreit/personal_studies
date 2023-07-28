""" ENUNCIADO
Crie um programa que leia um arquivo-texto e gere um arquivo de saída paginado.
Cada linha não deve conter mais de 76 caracteres. Cada página terá no máximo 60 linhas.
Adicione na última linha de cada página o número da página atual e o nome do arquivo original.
"""

NOME_ARQ_ORIGINAL = "arquivo-texto"
NOME_ARQ_SAIDA = "arquivo-saida"
LARGURA = 65
PAGINA = 0

def imprimirPagina():
    global LARGURA, PAGINA, fSaida

    PAGINA += 1
    fSaida.write(f"\n\n{NOME_ARQ_ORIGINAL}")
    fSaida.write(f"Pagina {PAGINA}\n\n\n".rjust(LARGURA))
    fSaida.write(f"{'-' * 76}\n\n")

with open(f"{NOME_ARQ_ORIGINAL}.txt", "r") as fOriginal:
    with open(f"{NOME_ARQ_SAIDA}.txt", "a") as fSaida:
        for linha in fOriginal.readlines():
            linhas_Pag = 0
            while len(linha) > 0:
                linhas_Pag += 1
                linha_limite = linha[:76]
                linha = linha[76:]
                fSaida.write(f"{linha_limite}\n")
                if linhas_Pag >= 60:
                    linhas_Pag = 0
                    imprimirPagina()
        imprimirPagina()