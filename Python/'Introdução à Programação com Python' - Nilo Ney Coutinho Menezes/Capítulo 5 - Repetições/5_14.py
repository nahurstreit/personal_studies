""" ENUNCIADO:
Escreva um programa que leia números inteiros do teclado. O programa deve ler os números até que
o usuário digite 0 (zero). No final da execução, exiba a quantidade de números digitados, assim
como a soma e a média aritmética.
"""

sz_Title_Total = 50
txt_Title = "SOMAR ATÉ DIGITAR ZERO"
space_Title = (sz_Title_Total - len(txt_Title))//2 if sz_Title_Total - len(txt_Title) > 0 else 5
sz_Title_Side = "#" * space_Title

print(f"{sz_Title_Side} {txt_Title} {sz_Title_Side}\n")

total_sum = 0
count_sum = 0
print("Digite números aleatórios. O programa encerrará quando você digitar 0")
while True:
    num = int(input(""))
    if num == 0:
        break
    total_sum += num
    count_sum += 1

print(f"\n{'#' * ((len(sz_Title_Side) * 2) + len(txt_Title) + 2)}\n")

print(f"Números digitados: {count_sum}")
print(f"Soma total: {total_sum}")
print(f"Média Aritmética: {float(total_sum /count_sum):.2f}")