""" ENUNCIADO:
Faça um programa que peça dois números inteiros. Improma a soma desses dois números na tela.
"""

sz_Title_Total = 50
txt_Title = "SOMA DE DOIS NÚMEROS"
space_Title = (sz_Title_Total - len(txt_Title))//2 if sz_Title_Total - len(txt_Title) > 0 else 5
sz_Title_Side = "#" * space_Title

print(f"{sz_Title_Side} {txt_Title} {sz_Title_Side}\n")

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

print(f"\n{'#' * ((len(sz_Title_Side) * 2) + len(txt_Title) + 2)}\n") #Somando 2 por causa dos dois espaços entre o texto e os #

print(f"{num1} + {num2} = {num1 + num2}")