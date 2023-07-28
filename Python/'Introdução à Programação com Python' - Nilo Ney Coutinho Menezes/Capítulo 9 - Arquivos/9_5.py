""" ENUNCIADO:
Crie um programa que inverta a ordem das linhas do arquivo pares.txt. A primeira linha deve conter
o maior número e a última, o menor.
"""

par_inverse = []

try:
    with open("pares.txt", "r") as par:
        for linha in par.readlines():
            par_inverse.append(linha)
    
    with open("pares.txt", "w") as par:
        for i in range(len(par_inverse) - 1, -1, -1):
            par.write(f"{par_inverse[i]}")

except Exception as erro:
    print(erro)