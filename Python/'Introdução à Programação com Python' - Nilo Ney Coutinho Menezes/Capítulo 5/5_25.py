""" ENUNCIADO:
Escreva um programa que calcule a raiz quadrada de um número. 
Utilize o método de Newton para obter um resultado aproximado. Sendo n o número a obter a raiz quadrada,
considere a base b = 2. Calcule p usando a fórmula p = (b + (n/b))/2. Agora calcule o quadrado de p.
A cada passo, faça b = p e recalcule p usando a fórmula apresentada. Pare quando a diferença absoluta
entre n e o quadrado de p for menor que 0,0001.

"""

sz_Title_Total = 50
txt_Title = "RAIZ QUADRADA APROXIMADA"
space_Title = (sz_Title_Total - len(txt_Title))//2 if sz_Title_Total - len(txt_Title) > 0 else 5
sz_Title_Side = "#" * space_Title

print(f"{sz_Title_Side} {txt_Title} {sz_Title_Side}\n")

n = int(input("Digite um número: "))

b = 2
while True:
    p = (b + (n/b)) / 2
    x = p ** 2
    if x - n < 0.0001:
        break
    b = p

print(f"\n{'#' * ((len(sz_Title_Side) * 2) + len(txt_Title) + 2)}\n")

print(f"A raiz quadrada de {n} = {float(b):.3f}")