""" ENUNCIADO:
Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto.
Exiba o valor do desconto e o preço a pagar.
"""

sz_Title_Total = 40
txt_Title = "CALCULAR DESCONTO"
space_Title = (sz_Title_Total - len(txt_Title))//2 if sz_Title_Total - len(txt_Title) > 0 else 5
sz_Title_Side = "#" * space_Title

print(f"{sz_Title_Side} {txt_Title} {sz_Title_Side}\n")

desconto = float(input("Digite o percentual do desconto (%): "))
desconto /= 100.0
valor = float(input("Digite o valor do produto: "))

print(f"\n{'#' * ((len(sz_Title_Side) * 2) + len(txt_Title) + 2)}\n")

print(f"O desconto do produto foi de R$ {valor * (desconto):5.2f} e o valor final é de R$ {valor * (1 - desconto):5.2f}")