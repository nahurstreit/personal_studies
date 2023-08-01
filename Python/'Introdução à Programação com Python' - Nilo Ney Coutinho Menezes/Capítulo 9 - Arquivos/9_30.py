""" ENUNCIADO:
Modifique o (programa9_8.py) para gerar uma lista html, usando os elementos ul e li.
Todos os elementos da lista devem estar dentro do elemento ul, e cada item dentro de um elemento li.
    Exemplo:
        <ul><li>Item1</li><li>Item2</li><li>Item3</li></ul>
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
        pagina.write(f"<h1>{c}</h1>\n<ul>\n")
        for e in v:
            pagina.write(f"<li>{e}</li>\n")
        pagina.write("</ul>\n")
    pagina.write("""
    </body>
</html>""")