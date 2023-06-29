""" ENUNCIADO:
Faça um programa para escrever a contagem regressiva do lançamento de um foguete.
O programa deve imprimir 10,9,8,...,1,0 e Fogo! na tela.
"""

sz_Title_Total = 50
txt_Title = "CONTAGEM REGRESSIVA!"
space_Title = (sz_Title_Total - len(txt_Title))//2 if sz_Title_Total - len(txt_Title) > 0 else 5
sz_Title_Side = "#" * space_Title

print(f"{sz_Title_Side} {txt_Title} {sz_Title_Side}\n")

x = 10
while x >= 0:
    print(x)
    x -= 1
else: 
    print("Fogo!")

print(f"\n{'#' * ((len(sz_Title_Side) * 2) + len(txt_Title) + 2)}\n")