""" ENUNCIADO:
Faça um programa que calcule o aumento de um salário. 
Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.
"""

sz_Title_Total = 40
txt_Title = "CALCULAR AUMENTO DE SALÁRIO"
space_Title = (sz_Title_Total - len(txt_Title))//2 if sz_Title_Total - len(txt_Title) > 0 else 5
sz_Title_Side = "#" * space_Title

print(f"{sz_Title_Side} {txt_Title} {sz_Title_Side}\n")

aumento = float(input("Digite o percentual do aumento (%): "))
aumento /= 100.0
salario = float(input("Digite o valor do salário: "))

print(f"\n{'#' * ((len(sz_Title_Side) * 2) + len(txt_Title) + 2)}\n") #Somando 2 por causa dos dois espaços entre o texto e os #

print(f"O novo salário teve um aumento de R$ {salario * (aumento):5.2f} e agora o valor total é de R$ {salario * (1 + aumento):5.2f}")