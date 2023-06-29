""" ENUNCIADO:
Escreva um programa que calcule o resto da divisão inteira entre dois números. Utilize apenas as operações 
de soma e subtração para calcular o resultado.
"""

sz_Title_Total = 50
txt_Title = "CALCULAR O RESTO EXTENSIVO"
space_Title = (sz_Title_Total - len(txt_Title))//2 if sz_Title_Total - len(txt_Title) > 0 else 5
sz_Title_Side = "#" * space_Title

print(f"{sz_Title_Side} {txt_Title} {sz_Title_Side}\n")

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

copyNum1 = num1
while num2 <= copyNum1:
    copyNum1 -= num2

print(f"\n{'#' * ((len(sz_Title_Side) * 2) + len(txt_Title) + 2)}\n")

print(f"O resto da divisão entre o número {num1} pelo número {num2} é igual à {copyNum1}.")