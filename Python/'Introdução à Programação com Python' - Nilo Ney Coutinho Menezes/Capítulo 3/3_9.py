""" ENUNCIADO:
Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.
"""

sz_Title_Total = 40
txt_Title = "CALCULANDO SEGUNDOS"
space_Title = (sz_Title_Total - len(txt_Title))//2 if sz_Title_Total - len(txt_Title) > 0 else 5
sz_Title_Side = "#" * space_Title

print(f"{sz_Title_Side} {txt_Title} {sz_Title_Side}\n")

dias = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantidade de segundos: "))

dias *= 24 * 60 * 60
horas *= 60 * 60
minutos *= 60

totalSegundos = dias + horas + minutos + segundos


print(f"\n{'#' * ((len(sz_Title_Side) * 2) + len(txt_Title) + 2)}\n") #Somando 2 por causa dos dois espaços entre o texto e os #

print(f"Total em segundos {totalSegundos} segundos")