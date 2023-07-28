""" ENUNCIADO:
Crie um programa que leia os arquivos "pares.txt" e "impares.txt" e que crie um só arquivo "pareseimpares.txt"
com todas as linhas dos outros dois arquivos, de forma a preservar a ordem numérica.
"""

def lerArquivo(arquivo):
    try:
        with open(arquivo, "r") as arq:
            for linha in arq.readlines():
                if linha.strip() != "":
                    yield int(linha)
    except Exception:
        raise Exception(f"Problema ao ler o arquivo: '{arquivo}'.\nVerifique se o mesmo existe no mesmo diretório desse programa")

pares = lerArquivo("pares.txt")
impares = lerArquivo("impares.txt")

try:
    with open("pareseimpares.txt", "w") as arquivoFinal:
        par = next(pares)
        impar = next(impares)
        while par is not None or impar is not None:
            if par < impar:
                arquivoFinal.write(f"{par}\n")
                par = next(pares)
            else:
                arquivoFinal.write(f"{impar}\n")
                impar = next(impares)
except Exception as erro:
    print(erro)