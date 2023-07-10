""" ENUNCIADO:
Escreva uma função que receba a base e a altura de um triângulo e retorne sua área (A = (base x altura)/2)
Valores esperados:
area_triangulo(6,9) == 27
area_triangulo(5,8) == 20
"""

def area_triangulo(base, alt):
    return (base * alt) / 2

base = float(input("Digite o tamanho da base do triângulo: "))
alt = float(input("Digite o tamanho da altura do triângulo: "))

print(f"A área desse triângulo é: {area_triangulo(base, alt):.2f}")