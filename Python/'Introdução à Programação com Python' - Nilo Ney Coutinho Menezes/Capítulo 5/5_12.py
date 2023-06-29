""" ENUNCIADO:
Altere o programa anterior (5_11.py) de forma a perguntar também o valor depositado mensalmente.
Esse valor será depositado no início de cada mês, e você deve considerá-lo para o cálculo de juros do
mês seguinte.
"""

sz_Title_Total = 50
txt_Title = "CALCULO DE JUROS COM APORTE MENSAL"
space_Title = (sz_Title_Total - len(txt_Title))//2 if sz_Title_Total - len(txt_Title) > 0 else 5
sz_Title_Side = "#" * space_Title

print(f"{sz_Title_Side} {txt_Title} {sz_Title_Side}\n")

deposito = float(input("Digite o valor do depósito inicial: R$ "))
aporte = float(input("Digite o valor do aporte mensal: R$ "))
taxa_juros = float(input("Digite o valor da taxa de juros mensal (%): "))
taxa_juros /= 100

print(f"\n{'#' * ((len(sz_Title_Side) * 2) + len(txt_Title) + 2)}\n")

mes = 1
montante = deposito
while mes <= 24:
    montante *= (1 + taxa_juros)
    print(f"Mês {mes}: R$ {montante:.2f}")
    montante += aporte
    mes += 1

juros = montante - deposito - (aporte * 24)

print(f"\nValor final: R$ {montante:.2f}")
print(f"Ganho com juros no período: R$ {juros:.2f}")
print(f"Total aplicado: R$ {montante - juros:.2f}\n")