""" ENUNCIADO:
Modifique o programa anterior (5_23.py) de forma a ler um número n. Imprima os n primeiros números primos.
"""

sz_Title_Total = 50
txt_Title = "MOSTRAR N NÚMEROS PRIMOS"
space_Title = (sz_Title_Total - len(txt_Title))//2 if sz_Title_Total - len(txt_Title) > 0 else 5
sz_Title_Side = "#" * space_Title

print(f"{sz_Title_Side} {txt_Title} {sz_Title_Side}\n")

n = int(input("Digite uma quantidade de números primos: "))

print(f"Estes são os {n} primeiros números primos:\n")
i = 0 # Controle de Loop do n
j = 2 # Controle de primos
while i < n:
    k = 2 # Controle de Loop dos primos
    while k < j:
        if j % k == 0:
            break
        k += 1 if k == 2 else 2
    if k >= j:
        print(f"{j} ")
        i += 1
    j += 1 if j == 2 else 2

print(f"\n{'#' * ((len(sz_Title_Side) * 2) + len(txt_Title) + 2)}\n")