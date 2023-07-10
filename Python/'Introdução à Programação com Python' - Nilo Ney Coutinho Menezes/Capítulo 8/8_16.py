""" ENUNCIADO:
Escreva um generator capaz de gerar a sequência dos números primos
"""

def gerarPrimos():
    num = 2
    while True:
        i = 2
        while i < num:
            if num % i == 0: break
            i += 1
        if i >= num:
            yield num
            
        num += 1 if num <= 2 else 2

primo = gerarPrimos()
while True:
    qtd = '0'
    try:
        qtd = int(input(f"Digite a quantidade de primos: "))
        for num in range(qtd):
            print(f"{next(primo)} ", end="")
            print()
        break
    except ValueError:
        print("\nDigite apenas números.")
    except Exception as erro:
        print(f"Houve um erro: {erro}")