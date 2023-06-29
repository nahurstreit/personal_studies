""" ENUNCIADO:
Escreva um programa que converta uma temperatura digitada em °C para °F.
A Fórmula para essa conversão é: F = (9 * C / 5) + 32.
"""

sz_Title_Total = 40
txt_Title = "CONVERTER CELSIUS PARA FAHRENHEIT"
space_Title = (sz_Title_Total - len(txt_Title))//2 if sz_Title_Total - len(txt_Title) > 0 else 5
sz_Title_Side = "#" * space_Title

print(f"{sz_Title_Side} {txt_Title} {sz_Title_Side}\n")

celsius = float(input("Digite a temperatura em °C: "))
fahrenheit = (9 * celsius / 5) + 32 

print(f"\n{'#' * ((len(sz_Title_Side) * 2) + len(txt_Title) + 2)}\n")

print(f"{celsius:.2f}°C = {fahrenheit:.2f}°F")