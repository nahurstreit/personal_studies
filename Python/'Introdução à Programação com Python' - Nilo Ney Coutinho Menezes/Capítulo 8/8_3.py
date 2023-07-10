""" ENUNCIADO:
Escreva uma função que receba o lado de um quadrado e retorne sua área (A = lado²).
Valores esperados:
area_quadrado(4) == 16
area_quadrado(9) == 81
"""

def area_quadrado(lado):
    return lado ** 2

lado = float(input("Digite o valor do lado do quadrado: "))

print(f"Área do quadrado: {area_quadrado(lado):.2f}")