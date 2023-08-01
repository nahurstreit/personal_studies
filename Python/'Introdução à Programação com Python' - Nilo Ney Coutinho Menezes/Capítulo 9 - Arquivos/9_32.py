""" ENUNCIADO:
Modifique o programa do exercício (9_31.py) de forma a receber o nome do arquivo ou diretório a verificar pela
linha de comando. Imprima se existir e se for um arquivo ou diretório.
"""

import os.path
import sys

params = list(sys.argv)
if len(params) > 1:
    nome = params[1]
else:
    nome = input("Digite o nome do arquivo/diretório: ")

if os.path.exists(nome):
    if os.path.isdir(nome):
        print(f"'{nome}' existe e é um DIRETÓRIO!")
    else:
        print(f"'{nome}' existe e é um ARQUIVO!")
else:
    print(f"O diretório '{nome}' não existe.")