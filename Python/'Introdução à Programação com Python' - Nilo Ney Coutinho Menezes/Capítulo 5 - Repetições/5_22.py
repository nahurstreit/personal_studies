""" ENUNCIADO:
Escreva um programa que exiba uma lista de opções (menu): adição, subtração, divisão, multiplicação e sair.
Imprima a tabuada da operação escolhida. Repita até que a opção saída seja escolhida.
"""

sz_Title_Total = 50
txt_Title = "MENU TABUADA"
space_Title = (sz_Title_Total - len(txt_Title))//2 if sz_Title_Total - len(txt_Title) > 0 else 5
sz_Title_Side = "#" * space_Title

while True:
    print(f"{sz_Title_Side} {txt_Title} {sz_Title_Side}\n")
    print("[1] Adição\n[2] Subtração\n[3] Multiplicação\n[4] Divisão\n[5] Sair\n")
    opr = int(input("Digite uma opção: "))

    if opr == 5:
        break
    elif opr > 5 or opr < 1:
        print("Opção inválida! Digite novamente.\n")
        continue
    else:
        i = 1
        num = int(input("Digite um número: "))
        if opr == 1:
            print(f"Tabuada de Somatória do número {num}:")
            while i <= 10:
                print(f"{num} + {i} = {num + i}")
                i += 1
        elif opr == 2:
            print(f"Tabuada de Subtração do número {num}:")
            while i <= 10:
                print(f"{num} - {i} = {num - i}")
                i += 1
        elif opr == 3:
            print(f"Tabuada de Multiplicação do número {num}:")
            while i <= 10:
                print(f"{num} * {i} = {num * i}")
                i += 1
        elif opr == 4:
            print(f"Tabuada de Divisão do número {num}:")
            while i <= 10:
                print(f"{num} / {i} = {float(num / i):5.4f}")
                i += 1
        print("\n")

print(f"\n{'#' * ((len(sz_Title_Side) * 2) + len(txt_Title) + 2)}\n")
print("Programa encerrado com sucesso!\n")