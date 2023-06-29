""" ENUNCIADO:
Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200km, e R$ 0,45 para viagens mais longas.
"""

sz_Title_Total = 50
txt_Title = "CALCULAR PREÇO DA PASSAGEM"
space_Title = (sz_Title_Total - len(txt_Title))//2 if sz_Title_Total - len(txt_Title) > 0 else 5
sz_Title_Side = "#" * space_Title

print(f"{sz_Title_Side} {txt_Title} {sz_Title_Side}\n")

distancia = float(input("Digite a distância que você deseja percorrer em km: "))
preco_viagemCurta = 0.5
preco_viagemLonga = 0.45

print(f"\n{'#' * ((len(sz_Title_Side) * 2) + len(txt_Title) + 2)}\n")

if distancia > 200:
    print(f"O valor da passagem é de R$ {distancia * preco_viagemLonga:.2f}")
else:
    print(f"O valor da passagem é de R$ {distancia * preco_viagemCurta:.2f}")