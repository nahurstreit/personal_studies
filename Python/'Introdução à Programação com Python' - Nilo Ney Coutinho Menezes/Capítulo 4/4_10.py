""" ENUNCIADO:
Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica.
Pergunte a quantidade de kWh consumida e o tipo de instalação:
    [R] para residências, [I] para indústricas e [C] para comércios.

Calcule o preço a pagar de acordo com a tabela a seguir:
    Tabela:
        > Residencial: Até 500kWh = 0,40. Acima de 500kWh = 0,65.
        > Comercial: Até 1000kWh = 0,55. Acima de 1000kWh = 0,60.
        > Industrial: Até 5000kWh = 0,55. Acima de 5000kWh = 0,60.
"""

sz_Title_Total = 50
txt_Title = "VALOR ENERGIA"
space_Title = (sz_Title_Total - len(txt_Title))//2 if sz_Title_Total - len(txt_Title) > 0 else 5
sz_Title_Side = "#" * space_Title

print(f"{sz_Title_Side} {txt_Title} {sz_Title_Side}\n")

consumo_kwh = float(input("Digite o valor consumido de kWh: "))

print(f"\n{'#' * ((len(sz_Title_Side) * 2) + len(txt_Title) + 2)}\n")

print("Tipos de instalação disponíveis")
print("[R] Residencial\n[C] Comercial\n[I] Industrial\n")
instalacao = input("Digite o tipo de instalação consultada: ")

print(f"\n{'#' * ((len(sz_Title_Side) * 2) + len(txt_Title) + 2)}\n")

if instalacao == "R":
    if consumo_kwh <= 500:
        preco_final = consumo_kwh * 0.4
    else:
        preco_final = consumo_kwh * 0.65
    print(f"Preço final: {preco_final}")
elif instalacao == "C":
    if consumo_kwh <= 1000:
        preco_final = consumo_kwh * 0.55
    else:
        preco_final = consumo_kwh * 0.6
    print(f"Preço final: {preco_final}")
elif instalacao == "I":
    if consumo_kwh <= 5000:
        preco_final = consumo_kwh * 0.55
    else:
        preco_final = consumo_kwh * 0.6
    print(f"Preço final: {preco_final}")
else:
    print("Tipo de instalação inválida! Execute o programa novamente.\n")