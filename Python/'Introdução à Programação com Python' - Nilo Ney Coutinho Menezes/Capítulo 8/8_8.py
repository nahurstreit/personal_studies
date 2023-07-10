""" ENUNCIADO:
Usando a função mdc definida no exercício anterior (8_7.py), defina uma função para calcular o 
menor múltiplo comum (M.M.C.) entre dois números.

    A definição de M.M.C. segue o seguinte:
        mmc(a, b) = (|a x b|)/[mdc(a, b)]

    Em que |a x b| pode ser escrito em Python como: abs(a * b)
"""

def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, (a % b))

def mmc(a, b):
    return abs(a * b) / mdc(a, b)

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

print(f"O M.M.C. entre {a} e {b} = {mmc(a,b):.0f}")