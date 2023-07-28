""" ENUNCIADO:
Altere o programa de forma a solicitar ao usuário o produto e a quantidade vendida. Verifique se o nome
do produto digitado existe no dicionário, e só então efetue a baixa em estoque.
    Programa:
        estoque = {"tomate": [1000, 2.30],
           "alface": [500, 0.45],
           "batata": [2001, 1.20],
           "feijão": [100, 1.50]}
        venda = [["tomate", 5], ["batata", 10], ["alface"], 5]
        total = 0
        print("Vendas:\n")
        for operacao in venda:
            produto, quantidade = operacao
            preco = estoque[produto][1]
            custo = preco * quantidade
            print(f"{produto:12s}: {quantidade:3d} x {preco:6.2f} = {custo:6.2f}")
            estoque[produto][0] -= quantidade
            total += custo
        print(f"Custo total: {total:21.2f}\n")
        print("Estoque:\n")
        for chave, dados in estoque.items():
            print("Descrição: ", chave)
            print("Quantidade: ", dados[0])
            print(f"Preço: {dados[1]:6.2f}\n")

"""
estoque = {"Tomate": [1000, 2.30],
           "Alface": [500, 0.45],
           "Batata": [2001, 1.20],
           "Feijão": [100, 1.50]}

print("Produtos disponíveis:\n")
for e in estoque.keys():
    print(e)

venda = []
erro_qtd = False
print("Venda:")
while True:
    item_atual = []
    if not erro_qtd:
        produto = input("Digite o nome do produto ou 'Fim' para terminar a venda: ")
    erro_qtd = False
    if produto == "Fim":
        break
    if produto in estoque: 
        item_atual.append(produto)
    else:
        print("Produto não encontrado! Tente novamente.\n")
        continue
    quantidade = int(input("Digite a quantidade comprada: "))
    if quantidade < 1:
        print("Quantidade inválida! Tente novamente.\n")
        erro_qtd = True
        continue
    elif quantidade > estoque[produto][0]:
        print("Quantidade digitada maior do que em estoque!")
        erro_qtd = True
        continue
    else:
        item_atual.append(quantidade)
        estoque[produto][0] -= quantidade
    venda.append(item_atual)

total = 0.0
for operacao in venda:
    produto, quantidade = operacao
    preco = estoque[produto][1]
    custo = preco * quantidade
    print(f"{produto:12s}: {quantidade:3d} x {preco:6.2f} = {custo:6.2f}")
    total += custo

print(f"Custo total: {total:21.2f}\n")
print("Estoque Final:")
for chave, dados in estoque.items():
    print("Descrição: ", chave)
    print("Quantidade: ", dados[0])
    print(f"Preço: {dados[1]:6.2f}\n")