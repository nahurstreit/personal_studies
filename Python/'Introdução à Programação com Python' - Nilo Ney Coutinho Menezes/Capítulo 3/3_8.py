""" ENUNCIADO:
Escreva um programa que leia um valor em metros e o exiba convertido em milimetros.
"""

sz_Title_Total = 40
txt_Title = "CONVERSOR MILÍMETROS"
space_Title = (sz_Title_Total - len(txt_Title))//2 if sz_Title_Total - len(txt_Title) > 0 else 5
sz_Title_Side = "#" * space_Title

print(f"{sz_Title_Side} {txt_Title} {sz_Title_Side}\n")

metros = float(input("Digite o valor em metros (m): "))


print(f"\n{'#' * ((len(sz_Title_Side) * 2) + len(txt_Title) + 2)}\n") #Somando 2 por causa dos dois espaços entre o texto e os #

print(f"{metros}m em milímetros = {metros * 1000:.0f}mm")