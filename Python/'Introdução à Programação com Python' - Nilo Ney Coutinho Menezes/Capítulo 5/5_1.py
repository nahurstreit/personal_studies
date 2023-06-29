""" ENUNCIADO:
Modifique o programa para exibir os números de 1 a 100
    Programa:
        x = 1
        while x <= 3:
            print(x)
            x = x + 1
"""

sz_Title_Total = 50
txt_Title = "REPETIR NÚMEROS"
space_Title = (sz_Title_Total - len(txt_Title))//2 if sz_Title_Total - len(txt_Title) > 0 else 5
sz_Title_Side = "#" * space_Title

print(f"{sz_Title_Side} {txt_Title} {sz_Title_Side}\n")

x = 1
while x <= 100:
    print(x)
    x += 1
else: 
    print("Acabou o While!")

print(f"\n{'#' * ((len(sz_Title_Side) * 2) + len(txt_Title) + 2)}\n")