""" ENUNCIADO:
Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento.
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
Para inferiores ou iguais, de 15%.
"""

sz_Title_Total = 50
txt_Title = "CALCULAR AUMENTO DE SALÁRIO"
space_Title = (sz_Title_Total - len(txt_Title))//2 if sz_Title_Total - len(txt_Title) > 0 else 5
sz_Title_Side = "#" * space_Title

print(f"{sz_Title_Side} {txt_Title} {sz_Title_Side}\n")

salario = float(input("Digite o salário a aumentar: R$ "))
limiteSalario = 1250.0
aumento_BaixoLimite = 15
aumento_MaiorLimite = 10

print(f"\n{'#' * ((len(sz_Title_Side) * 2) + len(txt_Title) + 2)}\n")

aumento = aumento_BaixoLimite

if salario > limiteSalario:
    aumento = aumento_MaiorLimite

aumento /= 100

print(f"O salário aumentou R$ {salario * aumento:.2f}")
print(f"e agora o novo salário é de R$ {salario * (1 + aumento)}!\n")