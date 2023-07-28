""" ENUNCIADO:
Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros
fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro
e calcule quantos dias de vida um fumante perderá. Exiba o total em dias.
"""

sz_Title_Total = 60
txt_Title = "CALCULAR REDUÇÃO DE VIDA POR TABAGISMO"
space_Title = (sz_Title_Total - len(txt_Title))//2 if sz_Title_Total - len(txt_Title) > 0 else 5
sz_Title_Side = "#" * space_Title

print(f"{sz_Title_Side} {txt_Title} {sz_Title_Side}\n")

qntDia = int(input("Quantos cigarros você fuma por dia? "))
qntAnos = int(input("Há quantos anos você fuma? "))

qntAnos *= 365 * (qntDia * 10 * 60)

tempoPerdidoMeses, tempoPerdidoDias = divmod(qntAnos, (30 * 24 * 60 * 60))
tempoPerdidoDias, tempoPerdidoHoras = divmod(tempoPerdidoDias, (24 * 60 * 60))
tempoPerdidoHoras, tempoPerdidoMinutos = divmod(tempoPerdidoHoras, (60 * 60))
tempoPerdidoMinutos, tempoPerdidoSegundos = divmod(tempoPerdidoMinutos, 60)

print(f"\n{'#' * ((len(sz_Title_Side) * 2) + len(txt_Title) + 2)}\n")

print(f"Por dia você perde {qntDia * 10} minutos de vida.")
print(f"E por fumar há todos esses anos, você já perdeu um total de:\n")
print(f"{tempoPerdidoMeses} meses,\n{tempoPerdidoDias} dias,\n{tempoPerdidoHoras} horas,\n{tempoPerdidoMinutos} minutos e\n{tempoPerdidoSegundos} segundos")