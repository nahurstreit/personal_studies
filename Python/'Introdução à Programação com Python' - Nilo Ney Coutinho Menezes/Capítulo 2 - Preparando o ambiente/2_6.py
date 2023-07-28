""" ENUNCIADO: 
Modifique o programa, de forma que ele calcule um aumento de 15% para um salário de R$ 750.
    Programa:
        salario = 1500
        aumento = 5
        print(salario + (salario * aumento / 100))
"""

salario = 750

aumento = 15
aumento /= 100

print(salario * (1 + aumento))