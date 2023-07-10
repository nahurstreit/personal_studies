""" ENUNCIADO:
Reescreva a função para cálculo da sequência de Fibonacci, sem utilizar recursão.
    Função recursiva de Fibonacci:
        def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    
    Exemplo da sequência de fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21...
"""

def fibonacci(n):
    res_old, res_new = 0, 1
    for i in range(1, n):
        res_old, res_new = res_new, (res_new + res_old)
    return res_old

n = int(input("Digite o enésimo número da sequência de fibonacci que você deseja saber: "))
print(f"O {n}º número da sequência de fibonacci é {fibonacci(n)}.")