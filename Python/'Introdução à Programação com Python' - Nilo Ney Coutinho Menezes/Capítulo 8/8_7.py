""" ENUNCIADO:
Defina uma função recursiva que calcule o maior divisor comum (M.D.C.) entre dois números a e b, em que a > b.
    
    A definição de M.D.C. segue o seguinte:
        mdc(a, b) = a, se b = 0
        ou mdc(a, b) = mdc(b, [(a-b) ^ (a/b)]), se a > b

    Em que [(a - b) ^ (a/b)] pode ser escrito em Python como a % b.
"""

def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, (a % b))

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

print(f"O M.D.C. entre {a} e {b} = {mdc(a,b)}")