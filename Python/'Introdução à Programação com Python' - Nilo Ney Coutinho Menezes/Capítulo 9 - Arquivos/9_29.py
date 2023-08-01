""" ENUNCIADO:
Modifique o programa para utilizar o elemento p em vez de h2 nos filmes.
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
            pagina.write(f"<p>{e}</p>")
    pagina.write("""
    </body>
</html>""")