""" ENUNCIADO:
Escreva um generator capaz de gerar a sequência de Fibonacci.
"""

def fibonacci():
    old, new = 0, 1
    while True:
        yield old
        old, new = new, new + old

numFibonacci = fibonacci()
while True:
    try:
        qtd = int(input("Digite a quantidade de números da sequência de fibonacci: "))
        for i in range(qtd):
            print(f"{next(numFibonacci)} ", end="")
            print()
        break
    except ValueError:
        print("\nDigite apenas números.")
    except Exception as erro:
        print(f"\nHouve um erro: {erro}")