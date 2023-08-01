""" ENUNCIADO:
Modifique o programa de forma a verificar se z existe e é um diretório.
    Programa - Verificação se um diretório ou arquivo já existe
        import os.path
        if os.path.exists("z"):
            print("O diretório z existe.")
        else:
            print("O diretório z não existe.")
"""

import os.path

nome = "z"

if os.path.exists(nome):
    if os.path.isdir(nome):
        print(f"'{nome}' existe e é um diretório!")
    else:
        print(f"'{nome}' existe mas é um arquivo!")
else:
    print(f"O diretório '{nome}' não existe.")