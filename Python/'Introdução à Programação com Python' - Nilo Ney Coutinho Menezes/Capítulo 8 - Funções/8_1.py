""" ENUNCIADO:
Escreva uma função que retorne o maior de dois números.
Valores esperados:
maximo(5,6) == 6
maximo(2,1) == 2
maximo(7,7) == 7
"""

def maximo(num1, num2):
    if num1 > num2:
        return num1
    return num2

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

print(f"O maior número é o {maximo(num1, num2)}.")