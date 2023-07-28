""" ENUNCIADO:
Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário,
assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, 
sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.
"""

sz_Title_Total = 60
txt_Title = "CALCULAR PREÇO ALUGUEL DE CARRO"
space_Title = (sz_Title_Total - len(txt_Title))//2 if sz_Title_Total - len(txt_Title) > 0 else 5
sz_Title_Side = "#" * space_Title

print(f"{sz_Title_Side} {txt_Title} {sz_Title_Side}\n")

dias = int(input("Digite a quantidade de dias de uso do veículo: "))
kmsRodados = float(input("Digite a quantidade de km rodados: "))

print(f"\n{'#' * ((len(sz_Title_Side) * 2) + len(txt_Title) + 2)}\n")

print(f"O valor total a se pagar por esse aluguel é de R$ {(dias * 60) + (kmsRodados * 0.15):.2f}")