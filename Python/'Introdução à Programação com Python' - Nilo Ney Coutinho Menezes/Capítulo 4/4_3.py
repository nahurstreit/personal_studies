""" ENUNCIADO:
Escreva um programa que leia três números e que imprima o maior e o menor.
"""

sz_Title_Total = 50
txt_Title = "IDENTIFICAR MAIOR E MENOR"
space_Title = (sz_Title_Total - len(txt_Title))//2 if sz_Title_Total - len(txt_Title) > 0 else 5
sz_Title_Side = "#" * space_Title

print(f"{sz_Title_Side} {txt_Title} {sz_Title_Side}\n")

num1 = int(input("Digite o primeiro número: "))
maior = num1
menor = num1

num2 = int(input("Digte o segundo número: "))
if num2 > maior:
    maior = num2
if num2 < menor:
    menor = num2

num3 = int(input("Digite o terceiro número: "))
if num3 > maior:
    maior = num3
if num3 < menor:
    menor = num3

print(f"\n{'#' * ((len(sz_Title_Side) * 2) + len(txt_Title) + 2)}\n")

print(f"O maior número que você digitou foi o número: {maior}")
print(f"e o menor número que você digitou foi o número: {menor}.\n")
