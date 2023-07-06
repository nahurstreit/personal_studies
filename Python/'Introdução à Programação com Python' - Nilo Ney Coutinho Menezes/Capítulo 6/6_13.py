""" ENUNCIADO:
A lista de temperaturas de Mons, na Bélgica, foi armazenada na lista T = [-10, -8, 0, 1, 2, 5, -2, -4].
Faça um programa que imprima a menor e a maior temperatura, assim como a temperatura média.
"""

T = [-10, -8, 0, 1, 2, 5, -2, -4]

maior = T[0]
menor = T[0]
media = 0

for i in T:
    if i > maior:
        maior = i
    if i < menor:
        menor = i
    media += i

print(f"Menor Temperatura: {float(menor)}°C\nMaior Temperatura: {float(maior)}°C\nTemperatura Média: {float(media/len(T)):.2f}°C")