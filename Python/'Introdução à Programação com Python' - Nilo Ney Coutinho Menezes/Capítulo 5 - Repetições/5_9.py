""" ENUNCIADO:
Escreva um programa que leia dois números. Imprima a divisão inteira do primeiro pelo segundo, assim como
o resto da divisão. Utilize apenas os operadores de soma e subtração para calcular o resulatado.
Lembre-se de que podemos entender o quociente da divisão de dois números como a quantidade de vezes que podemos
retirar o divisor do dividendo. Logo, 20 / 4 = 5, uma vez que podemos subtratir 4 cinco vezes de 20.
"""

sz_Title_Total = 50
txt_Title = "DIVISÃO EXTENSIVA"
space_Title = (sz_Title_Total - len(txt_Title))//2 if sz_Title_Total - len(txt_Title) > 0 else 5
sz_Title_Side = "#" * space_Title

print(f"{sz_Title_Side} {txt_Title} {sz_Title_Side}\n")

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

print(f"\n{'#' * ((len(sz_Title_Side) * 2) + len(txt_Title) + 2)}\n")

copiaNum1 = num1

contadorDiv = 0
while True:
    if copiaNum1 >= num2:
        copiaNum1 -= num2
        contadorDiv += 1
    else: break

print(f"Resultado da divisão inteira: {contadorDiv}\nResto da divisão: {copiaNum1}\n")