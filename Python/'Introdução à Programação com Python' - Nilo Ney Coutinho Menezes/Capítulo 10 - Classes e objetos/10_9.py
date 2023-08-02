""" ENUNCIADO:
Crie classes para representar estados e cidades. Cada estado tem um nome, sigla
e cidades. Cada cidade tem nome e população. Escreva um programa de testes que crie três estados
com algumas cidades em cada um. Exiba a população de cada estado como a soma da população de suas
cidades.
"""

import locale
locale.setlocale(locale.LC_ALL, "pt_BR.utf-8")

class Estado:
    def __init__(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla
        self.cidades = []
        self.populacao = 0

    def adicionarCidade(self, cidade):
        self.cidades.append(cidade)
        self.populacao += self.cidades[-1].populacao

    def exibirInfo(self):
        print(f"{self.nome} ({self.sigla}) - População Total: {self.populacao:n} de habitantes.")
        print("    Cidades:")
        for cidade in self.cidades:
            print(f"        {cidade.nome} - População: {cidade.populacao:n}")
        print()

class Cidade:
    def __init__(self, nome, populacao):
        self.nome = nome
        self.populacao = populacao

saoPaulo_estado = Estado("São Paulo", "SP")
saoPaulo_estado.adicionarCidade(Cidade("Indaiatuba", 256223))
saoPaulo_estado.adicionarCidade(Cidade("Campinas", 1138309))
saoPaulo_estado.adicionarCidade(Cidade("São Paulo", 12300000))

rioDeJaneiro_estado = Estado("Rio de Janeiro", "RJ")
rioDeJaneiro_estado.adicionarCidade(Cidade("Teresópolis", 184240))
rioDeJaneiro_estado.adicionarCidade(Cidade("Angra dos Reis", 207044))
rioDeJaneiro_estado.adicionarCidade(Cidade("Rio de Janeiro", 6748000))

saoPaulo_estado.exibirInfo()
rioDeJaneiro_estado.exibirInfo()