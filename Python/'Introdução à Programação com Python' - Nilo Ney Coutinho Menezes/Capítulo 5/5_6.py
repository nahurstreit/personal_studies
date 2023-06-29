""" ENUNCIADO:
Altere o programa para exibir os resultados no mesmo formato de uma tabuada: 2x1 = 2, 2x2 = 4,...
    Programa:
        n = int(input("Tabuada de soma: "))
        x = 1
        while x <= 10:
            print(n + x)
            x = x + 1
"""

sz_Title_Total = 50
txt_Title = "TABUADA"
space_Title = (sz_Title_Total - len(txt_Title))//2 if sz_Title_Total - len(txt_Title) > 0 else 5
sz_Title_Side = "#" * space_Title

print(f"{sz_Title_Side} {txt_Title} {sz_Title_Side}\n")

num = int(input("Digite um número: "))

print(f"\n{'#' * ((len(sz_Title_Side) * 2) + len(txt_Title) + 2)}\n")

i = 1
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1