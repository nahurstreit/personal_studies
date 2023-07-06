""" ENUNCIADO:
Modifique o seguinte programa para ler 7 notas em vez de 5.
    Programa:
        notas = [0, 0, 0, 0, 0]
        soma = 0
        x = 0
        while x < 5:
            notas[x] = float(input(f"Nota {x}: "))
            soma += notas[x]
            x += 1
        x = 0
        while x < 5:
            print(f"Nota {x}: {notas[x]:6.2f}")
            x += 1
        print(f"Média: {soma / x:5.2f}")
"""

notas = [0, 0, 0, 0, 0, 0, 0]
soma = 0
x = 0
while x < len(notas):
    notas[x] = float(input(f"Nota {x + 1}: "))
    soma += notas[x]
    x += 1

x = 0
while x < len(notas):
    print(f"Nota {x}: {notas[x]:6.2f}")
    x += 1
    
print(f"Média: {soma / len(notas):5.2f}")