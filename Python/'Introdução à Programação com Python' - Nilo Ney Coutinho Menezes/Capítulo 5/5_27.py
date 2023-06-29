""" ENUNCIADO:
Escreva um programa que verifique se um número é palíndromo.
Um número é palíndromo se continua o mesmo caso seus dígitos sejam invertidos.
Exemplos: 454, 10501.
"""

sz_Title_Total = 50
txt_Title = "VERIFICAR NÚMERO PALÍNDROMO"
space_Title = (sz_Title_Total - len(txt_Title))//2 if sz_Title_Total - len(txt_Title) > 0 else 5
sz_Title_Side = "#" * space_Title

print(f"{sz_Title_Side} {txt_Title} {sz_Title_Side}\n")

num = int(input("Digite um número: "))

i = 1
while (10 ** i) < num:
    i += 1

j = 0
reverse_num = 0
while i > 0:
    digit = (((num % (10 ** i)) - (num % (10 ** (i - 1)))) // 10 ** (i - 1)) * (10 ** j)
    """ digit = pega o número mais a esquerda e multiplica por uma potência de 10
                seguindo pelos demais números"""
    reverse_num += digit
    i -= 1
    j += 1

print(f"\n{'#' * ((len(sz_Title_Side) * 2) + len(txt_Title) + 2)}\n")

if num == reverse_num:
    print(f"O número {num} é palíndromo!")
else:
    print(f"O número {num} não é palíndromo.")