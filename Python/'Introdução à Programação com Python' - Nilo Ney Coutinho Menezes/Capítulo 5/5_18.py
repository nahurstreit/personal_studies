""" ENUNCIADO:
Modifique o Programa 5_1 para também trabalhar com notas de R$ 100,00.
"""

sz_Title_Total = 50
txt_Title = "SUGESTÃO DE CÉDULAS PARA PAGAMENTO - Parte 2"
space_Title = (sz_Title_Total - len(txt_Title))//2 if sz_Title_Total - len(txt_Title) > 0 else 5
sz_Title_Side = "#" * space_Title

print(f"{sz_Title_Side} {txt_Title} {sz_Title_Side}\n")

valor = int(input("Digite o valor a pagar: R$ "))

print(f"\n{'#' * ((len(sz_Title_Side) * 2) + len(txt_Title) + 2)}\n")

cedulas = 0
atual = 100
apagar = valor
while True:
    if atual <= apagar:
        apagar -= atual
        cedulas += 1
    else:
        if cedulas != 0:
            print(f"{cedulas} cédula(s) de R${float(atual):.2f}")
        if apagar == 0:
            break
        if atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        cedulas = 0
print("\n")