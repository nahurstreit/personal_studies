""" ENUNCIADO:
Escreva um programa que pergunte o valor inicial de uma dívida e o juro mensal.
Pergunte também o valor mensal que será pago. Imprima o número de meses para que a dívida seja paga,
o total pago e o total de juros pago.
"""

sz_Title_Total = 50
txt_Title = "CALCULO DE MESES PARA QUITAR DÍVIDA"
space_Title = (sz_Title_Total - len(txt_Title))//2 if sz_Title_Total - len(txt_Title) > 0 else 5
sz_Title_Side = "#" * space_Title

print(f"{sz_Title_Side} {txt_Title} {sz_Title_Side}\n")

divida = float(input("Digite o valor da dívida: R$ "))
pagamento = float(input("Digite o valor pago mensalmente: R$ "))
taxa_juros = float(input("Digite o valor da taxa de juros mensal (%): "))
taxa_juros /= 100

print(f"\n{'#' * ((len(sz_Title_Side) * 2) + len(txt_Title) + 2)}\n")

divida_inicial = divida
meses = 0
juros_total = 0
total_pago = 0

while divida >= pagamento:
    juros_mes = divida * taxa_juros
    juros_total += juros_mes
    divida += juros_mes
    print(f"Mês {meses + 1}: R$ {divida:.2f}")
    divida -= pagamento
    meses += 1
    total_pago += pagamento

if divida > 0:
    juros_mes = divida * taxa_juros
    juros_total += juros_mes
    divida += juros_mes
    total_pago += divida

print(f"Você levará {meses} meses para pagar essa dívida")
print(f"e pagará ao final R$ {total_pago:.2f} dos quais R$ {juros_total:.2f} serão juros.\n")