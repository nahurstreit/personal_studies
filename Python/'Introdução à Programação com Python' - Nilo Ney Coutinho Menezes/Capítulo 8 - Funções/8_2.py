""" ENUNCIADO:
Escreva uma função que receba dois números e retorne True se o primeiro número for múltiplo do segundo.
Valores esperados:
multiplo(8,4) == True
multiplo(7,3) == False
multiplo(5,5) == True
"""

def multiplo(num1, num2):
    return num1 % num2 == 0

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

print(multiplo(num1, num2))