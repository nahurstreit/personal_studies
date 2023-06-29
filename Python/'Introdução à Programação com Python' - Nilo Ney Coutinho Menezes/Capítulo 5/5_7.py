""" ENUNCIADO:
Modifique o programa anterior (5_6.py) de forma que o usuário também digite o início e o fim da tabuada,
em vez de começar com 1 e 10.
"""

sz_Title_Total = 50
txt_Title = "TABUADA"
space_Title = (sz_Title_Total - len(txt_Title))//2 if sz_Title_Total - len(txt_Title) > 0 else 5
sz_Title_Side = "#" * space_Title

print(f"{sz_Title_Side} {txt_Title} {sz_Title_Side}\n")

num = int(input("Digite um número: "))
inicio = int(input("Digite o número para começar a tabuada: "))
fim = int(input("Digite o número para finalizar a tabuada: "))

print(f"\n{'#' * ((len(sz_Title_Side) * 2) + len(txt_Title) + 2)}\n")

i = inicio
while i <= fim:
    print(f"{num} x {i} = {num * i}")
    i += 1