""" ENUNCIADO:
Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar.
O valor da prestação mensal não pode ser superior a 30% do salário.
Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.
"""

sz_Title_Total = 50
txt_Title = "EMPRÉSTIMO BANCÁRIO"
space_Title = (sz_Title_Total - len(txt_Title))//2 if sz_Title_Total - len(txt_Title) > 0 else 5
sz_Title_Side = "#" * space_Title

print(f"{sz_Title_Side} {txt_Title} {sz_Title_Side}\n")

valor_casa = float(input("Digite o valor da casa: R$ "))
salario = float(input("Digite o valor do salário: R$ "))
qtdAnos = int(input("Digite de anos a pagar: "))

valor_prestacao = float(valor_casa/(qtdAnos * 12))

print(f"\n{'#' * ((len(sz_Title_Side) * 2) + len(txt_Title) + 2)}\n")

if (salario * 0.3) < valor_prestacao:
    print("O empréstimo não pode ser feito!\n")
else:
    print(f"O empréstimo pode ser feito e o valor das prestações é de R$ {valor_prestacao:.2f}\n")