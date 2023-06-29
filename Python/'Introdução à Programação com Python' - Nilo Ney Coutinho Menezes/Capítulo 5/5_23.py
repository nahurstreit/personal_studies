""" ENUNCIADO:
Escreva um programa que leia um número e verifique se é ou não um número primo. Para fazer essa verificação,
calcule o resto da divisão do número por 2 e depois por todos os números ímpares até o número lido.
Se o resto de uma dessas divisões for igual a zero, o número não é primo. Observe que 0 e 1 não são números primos
e que 2 é o único número primo que é par.
"""

sz_Title_Total = 50
txt_Title = "VERIFICAR NÚMERO PRIMO"
space_Title = (sz_Title_Total - len(txt_Title))//2 if sz_Title_Total - len(txt_Title) > 0 else 5
sz_Title_Side = "#" * space_Title

print(f"{sz_Title_Side} {txt_Title} {sz_Title_Side}\n")

num = int(input("Digite um número: "))

if num < 0:
    print("Não existem números primos negativos.")
else:
    i = 2
    while i < num:
        if num % i == 0:
            break
        i += 1 if i == 2 else 2
    if i >= num and (num > 1):
        print(f"O número {num} é primo!")
    else:
        print(f"O número {num} não é primo.")

print(f"\n{'#' * ((len(sz_Title_Side) * 2) + len(txt_Title) + 2)}\n")