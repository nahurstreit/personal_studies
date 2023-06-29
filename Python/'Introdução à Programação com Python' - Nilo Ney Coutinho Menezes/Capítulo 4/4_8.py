""" ENUNCIADO:
Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar.
Você deve poder calcular soma (+), subtração (-), multiplicação (*) e divisão (/).
Exiba o resultado da operação solicitada.
"""

sz_Title_Total = 50
txt_Title = "CALCULADORA"
space_Title = (sz_Title_Total - len(txt_Title))//2 if sz_Title_Total - len(txt_Title) > 0 else 5
sz_Title_Side = "#" * space_Title

print(f"{sz_Title_Side} {txt_Title} {sz_Title_Side}\n")

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

print(f"\n{'#' * ((len(sz_Title_Side) * 2) + len(txt_Title) + 2)}\n")

print("Operações disponíveis:\n")
print("[+] Soma\n[-] Subtração\n[*] Multiplicação\n[/] Divisão\n")

opr = input("Digite a operação desejada: ")

print(f"\n{'#' * ((len(sz_Title_Side) * 2) + len(txt_Title) + 2)}\n")

if opr == "+":
    print(f"{num1} + {num2} = {num1 + num2}\n")
elif opr == "-":
    print(f"{num1} - {num2} = {num1 - num2}\n")
elif opr == "*":
    print(f"{num1} * {num2} = {num1 * num2}\n")
elif opr == "/":
    print(f"{num1} / {num2} = {float(num1 / num2)}\n")
else:
    print("Operação inválida, execute o programa novamente!\n")