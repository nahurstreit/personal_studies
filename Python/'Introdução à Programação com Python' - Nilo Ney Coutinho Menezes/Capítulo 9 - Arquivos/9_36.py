""" ENUNCIADO:
Utilizando a função os.walk, crie um programa que calcule o espaço ocupado por cada diretório e subdiretório,
gerando uma página html com os resultados.
"""

import os
import sys

params = list(sys.argv)
if len(params) > 1:
    diretorio_inicial = params[1]
else:
    diretorio_inicial = input("Digite o nome do diretório inicial: ")

tree = {}
try:
    for raiz, diretorios, arquivos in os.walk(diretorio_inicial):
        tree[raiz] = (diretorios, arquivos)

    stringFinal = ''
    def imprimirDiretorios(dir, nivel):
        global stringFinal
        stringFinal += f"<h{1+nivel}>{dir}(Tamanho: {calcularTamanhoDir(dir):.2f}KB):</h{1+nivel}>\n"
        stringFinal += f"<ul>\n"
        if len(tree[dir][1]) > 0:
            for arquivo in tree[dir][1]:
                caminho_completo = os.path.join(dir, arquivo)
                tamanho_arquivo = os.path.getsize(caminho_completo)
                tamanho_arquivo /= 1000
                #stringFinal += f"<li>{arquivo} - Tamanho: {tamanho_arquivo:.2f}KB</li>\n"
        if len(tree[dir][0]) > 0:
            for diretorio in tree[dir][0]:
                stringFinal += "<li>"
                imprimirDiretorios(f"{dir}\\{diretorio}", nivel + 1)
                stringFinal += "</li>"
        stringFinal += f"</ul>\n"
        return stringFinal

    def calcularTamanhoDir(dir):
        tamanho_dir = 0
        if len(tree[dir][1]) > 0:
            for arquivo in tree[dir][1]:
                caminho_completo = os.path.join(dir, arquivo)
                tamanho_arquivo = os.path.getsize(caminho_completo)
                tamanho_arquivo /= 1000
                tamanho_dir += tamanho_arquivo
        if len(tree[dir][0]) > 0:
            for diretorio in tree[dir][0]:
                tamanho_dir += calcularTamanhoDir(f"{dir}\\{diretorio}")
        return tamanho_dir

    def gerarHmtl():
        with open("diretoriosTamanho.html", "w", encoding="utf-8") as arquivo:
            arquivo.write(f"""
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="UTF-8" />
            <title>title</title>
        </head>
        <body>
            <ul>
    {imprimirDiretorios(diretorio_inicial, 0)}
            </ul>
        </body>
    </html>""")

    gerarHmtl()
    print("Arquivo HTML gerado com sucesso!")
except Exception as erro:
    print(f"Erro ao achar o diretório {erro}, tente novamente.")