""" ENUNCIADO:
Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80km/h, exiba uma mensagem
dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5,00 por km a cima de 80km/h.
"""

sz_Title_Total = 50
txt_Title = "APLICAR MULTA"
space_Title = (sz_Title_Total - len(txt_Title))//2 if sz_Title_Total - len(txt_Title) > 0 else 5
sz_Title_Side = "#" * space_Title

print(f"{sz_Title_Side} {txt_Title} {sz_Title_Side}\n")

velocidadeMaxima = 80
velocidade = int(input("Digite a velocidade do carro em km/h: "))
valorMulta = 5.0

print(f"\n{'#' * ((len(sz_Title_Side) * 2) + len(txt_Title) + 2)}\n")

if velocidade > velocidadeMaxima:
    print(f"Você foi multado, o valor da multa é de R$ {float((velocidade - velocidadeMaxima) * valorMulta):.2f}!")