""" ENUNCIADO:
Modifique o programa para imprimir de 1 até o número digitado pelo usuário, mas dessa vez apenas os
números ímpares.
    Programa:
        # Imprimir números pares até...
        fim = int(input("Digite o último número a imprimir:"))
        x = 0
        while x <= fim
            print(x)
            x = x + 2
"""

sz_Title_Total = 50
txt_Title = "ÍMPARES ATÉ..."
space_Title = (sz_Title_Total - len(txt_Title))//2 if sz_Title_Total - len(txt_Title) > 0 else 5
sz_Title_Side = "#" * space_Title

print(f"{sz_Title_Side} {txt_Title} {sz_Title_Side}\n")

fim = int(input("Digite o último número a imprimir: "))

print(f"\n{'#' * ((len(sz_Title_Side) * 2) + len(txt_Title) + 2)}\n")

i = 1
while i <= fim:
    print(i)
    i += 2