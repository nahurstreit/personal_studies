""" ENUNCIADO:
Crie um programa que gere uma página html com links para todos os arquivos jpg e png encontrados
a partir de um diretório informado na linha de comando.
"""

import os.path
import sys

params = list(sys.argv)
if len(params) > 1:
    diretorio = params[1]
else:
    diretorio = input("Digite o nome do diretório: ")

currentPath = "."
def acharDir(pathDig=''):
    global currentPath, rollBack
    currentPath = pathDig + currentPath
    try:
        if diretorio not in os.listdir(f"{currentPath}"):
            return acharDir("../")
        else:
            currentPath = currentPath.rstrip('.')
            return currentPath+diretorio
    except FileNotFoundError:
        currentPath = None

def listarImagens(path):
    imagens = []
    if path is not None:
        conteudoDir = os.listdir(path)
        for arquivo in conteudoDir:
            if (f"{arquivo}".find(".jpg") != -1) or (f"{arquivo}".find(".png") != -1):
                imagens.append(arquivo)

    return imagens if len(imagens) > 0 else None

def criarListaImagens():
    imagens = listarImagens(acharDir())
    final_string = ''
    if currentPath is not None:
        path = os.path.abspath(currentPath)
    if imagens is not None:
        for imagem in imagens:
            final_string += f"""
            <li><a href="{path}/{diretorio}/{imagem}" target="_blank">{imagem}</a></li>"""
    else:
        final_string = """
            Não foram encontradas imagens"""
    return final_string

def gerarHmtl():
    with open("imagensNoDiretorio.html", "w", encoding="utf-8") as arquivo:
        arquivo.write(f"""
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8" />
        <title>title</title>
    </head>
    <body>
        <h1>Arquivos de imagem (JPG e PNG) dentro do diretório: {diretorio}</h1>
        <ul>{criarListaImagens()}
        </ul>
    </body>
</html>""")

gerarHmtl()