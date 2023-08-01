"""
Cópia do Programa 9.8 do livro (página 210 - Capítulo 9) - Geração de uma página web a partir de um dicionário
Programa necessário a resolução dos exercícios (9_29.py) e (9_30.py).
"""

filmes = {
    "drama": ["Cidadão Kane", "O Poderoso Chefão"],
    "comédia": ["Tempos Modernos", "American Pie", "Dr. Dolittle"],
    "policial": ["Chuva Negra", "Desejo de Matar", "Difícil de Matar"],
    "guerra": ["Rambo", "Platoon", "Tora!Tora!Tora!"]
}
with open("filmes.html", "w", encoding="utf-8") as pagina:
    pagina.write("""
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8" />
        <title>title</title>
    </head>
    <body>
""")
    for c, v in filmes.items():
        pagina.write(f"<h1>{c}</h1>\n")
        for e in v:
            pagina.write(f"<h2>{e}</h2>\n")
    pagina.write("""
    </body>
</html>""")