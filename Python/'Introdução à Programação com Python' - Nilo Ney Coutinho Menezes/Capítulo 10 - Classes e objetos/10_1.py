""" ENUNCIADO:
Usando a classe a seguir, adicione os atributos 'tamanho' e 'marca' à classe Televisão. Crie dois
objetos Televisão e atribua tamanhos e marcas diferentes. Depois, imprima o valor desses atributos 
de forma a confirmar a independência dos valores de cada instância(objeto).
    Classe:
        class Televisão:
        def __init__(self):
            self.ligada = False
            sel.canal = 2
"""

class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2
        self.marca = "Nenhuma"
        self.tamanho = 32

tv_quarto = Televisao()
tv_quarto.ligada = True
tv_quarto.marca = "Samsung"
tv_quarto.tamanho = 50

tv_sala = Televisao()
tv_sala.canal = 10
tv_sala.marca = "LG"
tv_sala.tamanho = 75

def exibirTelevisão(obj):
    print(f"""Ligada = {obj.ligada}
Canal ativo = {obj.canal}
Marca = {obj.marca}
Tamanho = {obj.tamanho}"
""")

exibirTelevisão(tv_quarto)
exibirTelevisão(tv_sala)