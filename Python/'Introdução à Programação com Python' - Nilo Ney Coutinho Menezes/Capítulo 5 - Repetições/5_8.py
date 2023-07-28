""" ENUNCIADO:
Escreva um programa que leida dois números. Imprima o resultado da multiplicação do primeiro pelo segundo.
Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos entender
a multplicação de dois números como somas sucessivas de um deles. 
Assim, 4 x 5 = (5 + 5 + 5 + 5) = (4 + 4 + 4 + 4 + 4) = 20.
"""

sz_Title_Total = 50
txt_Title = "MULTIPLICAÇÃO EXTENSIVA"
space_Title = (sz_Title_Total - len(txt_Title))//2 if sz_Title_Total - len(txt_Title) > 0 else 5
sz_Title_Side = "#" * space_Title

print(f"{sz_Title_Side} {txt_Title} {sz_Title_Side}\n")

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

print(f"\n{'#' * ((len(sz_Title_Side) * 2) + len(txt_Title) + 2)}\n")

i = 0
somaNum1 = 0
while i < num2:
    somaNum1 += num1
    i = i + 1

print(f"{f'{num1} + ' * (num2 - 1)}{num1} = {f'{num2} + ' * (num1 -1)}{num2} = {somaNum1}\n")