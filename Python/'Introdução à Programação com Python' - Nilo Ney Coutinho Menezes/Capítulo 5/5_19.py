""" ENUNCIADO:
Modifique o (programa5_1.py) para aceitar valores decimais, ou seja, também contar moedas de 0,5, 0,25, 0,10, 0,05 e 0,01.
Esse exercício também compreende o exercício proposto em 5_20: 
    'O que acontece se digitarmos 0,001 no programa? Caso não funcione, altere-o de forma a corrigir o problema.' 
"""

sz_Title_Total = 50
txt_Title = "SUGESTÃO DE CÉDULAS PARA PAGAMENTO - Parte 3"
space_Title = (sz_Title_Total - len(txt_Title))//2 if sz_Title_Total - len(txt_Title) > 0 else 5
sz_Title_Side = "#" * space_Title

print(f"{sz_Title_Side} {txt_Title} {sz_Title_Side}\n")

valor = float(input("Digite o valor a pagar: R$ "))

print(f"\n{'#' * ((len(sz_Title_Side) * 2) + len(txt_Title) + 2)}\n")

cedulas = 0
atual = 100.0
apagar = valor
while True:
    if atual <= apagar:
        apagar -= atual
        cedulas += 1
    else:
        if cedulas != 0:
            if atual >= 1:
                print(f"{cedulas} cédula(s) de R${float(atual):.2f}")
            else:
                if atual == 0.01:
                    cedulas += 1
                print(f"{cedulas} moeda(s) de R${float(atual):.2f}")

        if apagar <= 0.01:
            break
        if atual == 100.0:
            atual = 50.0
        elif atual == 50.0:
            atual = 20.0
        elif atual == 20.0:
            atual = 10.0
        elif atual == 10.0:
            atual = 5.0
        elif atual == 5.0:
            atual = 1.0
        elif atual == 1.0:
            atual = 0.5
        elif atual == 0.5:
            atual = 0.25
        elif atual == 0.25:
            atual = 0.1
        elif atual == 0.1:
            atual = 0.05
        elif atual == 0.05:
            atual = 0.01
        cedulas = 0