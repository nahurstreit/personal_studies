""" ENUNCIADO:
Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança.
Exiba os valores mês a mês para os 24 primeiros meses. Escreva o total ganho com juros no período.
"""

sz_Title_Total = 50
txt_Title = "CALCULO DE JUROS"
space_Title = (sz_Title_Total - len(txt_Title))//2 if sz_Title_Total - len(txt_Title) > 0 else 5
sz_Title_Side = "#" * space_Title

print(f"{sz_Title_Side} {txt_Title} {sz_Title_Side}\n")

deposito = float(input("Digite o valor do depósito inicial: R$ "))
taxa_juros = float(input("Digite o valor da taxa de juros mensal (%): "))
taxa_juros /= 100

print(f"\n{'#' * ((len(sz_Title_Side) * 2) + len(txt_Title) + 2)}\n")

mes = 1
montante = deposito
while mes <= 24:
    montante *= (1 + taxa_juros)
    print(f"Mês {mes}: R$ {montante:.2f}")
    mes += 1

juros = montante - deposito

print(f"Ganho com juros no período: R$ {juros:.2f}")