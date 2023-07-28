""" ENUNCIADO:
Escreva um programa para controlar uma pequena máquina registradora.
Você deve solicitar ao usuário que digite o código do produto e a quantidade comprada.
Utilize a tabela de códigos a seguir para obter o preço de cada produto.
    Tabela:
        Código 1 > R$ 0,50
        Código 2 > R$ 1,00
        Código 3 > R$ 4,00
        Código 5 > R$ 7,00
        Código 9 > R$ 8,00
Seu programa deve exibir o total das compras depois que o usuário digitar 0. 
Qualquer outro código deve gerar a mensagem de erro "Código Inválido".
"""

sz_Title_Total = 60
txt_Title = "MÁQUINA REGISTRADORA"
space_Title = (sz_Title_Total - len(txt_Title))//2 if sz_Title_Total - len(txt_Title) > 0 else 5
sz_Title_Side = "#" * space_Title

print(f"{sz_Title_Side} {txt_Title} {sz_Title_Side}\n")

print("Digite o código do produto e em seguida a quantidade comprada.")
print("Ou então, digite [0] para finalizar a compra.")

valor_total = 0.0
while True:
    cod = int(input("\nDigite o código do produto: "))
    if cod == 1:
        preco = 0.5
    elif cod == 2:
        preco = 1.0
    elif cod == 3:
        preco = 4.0
    elif cod == 5:
        preco = 7.0
    elif cod == 9:
        preco = 8.0
    elif cod == 0:
        break
    else:
        print("Código inválido, digite novamente!\n")
        continue

    qtd = int(input("Digite a quantidade comprada desse produto: "))
    valor_total += (qtd * preco)

print(f"\n{'#' * ((len(sz_Title_Side) * 2) + len(txt_Title) + 2)}\n")

print(f"Valor total: R$ {float(valor_total):.2f}")