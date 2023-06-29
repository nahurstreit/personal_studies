""" ENUNCIADO:
Reescreva o programa anterior (5_4.py) para escrever os 10 primeiros múltiplos de 3.
"""

sz_Title_Total = 50
txt_Title = "MÚLTIPLOS DE 3"
space_Title = (sz_Title_Total - len(txt_Title))//2 if sz_Title_Total - len(txt_Title) > 0 else 5
sz_Title_Side = "#" * space_Title

print(f"{sz_Title_Side} {txt_Title} {sz_Title_Side}\n")

i = 1
while i <= 10:
    print(i * 3)
    i += 1

print(f"\n{'#' * ((len(sz_Title_Side) * 2) + len(txt_Title) + 2)}\n")