"""
Para a resolução dos exercícios (10_4) e (10_5), use:
    Classe:
        class Televisao:
        def __init__(self, min, max):
            self.ligada = False
            self.canal = 2
            self.cmin = min
            self.cmax = max
        def muda_canal_para_baixo(self):
            if self.canal - 1 >= self.cmin:
                self.canal -= 1
        def muda_canal_para_cima(self):
            if self.canal + 1 <= self.cmax:
                self.canal += 1

ENUNCIADO 10_4: Utilizando o que aprendemos com funções, modifique o construtor da classe Televisao de forma
que 'min' e 'max' sejam parâmetros opicionais, em que 'min' vale 2 e 'max' vale 14, caso outro valor não seja
passado.

ENUNCIADO 10_5: Utilizando a classe Televisao modificada no exercício anterior, crie duas instâncias (objetos),
especificando o valor de 'min e 'max' por nome.
"""
class Televisao:
    def __init__(self, min=2, max=14):
        self.ligada = False
        self.canal = 2
        self.cmin = min
        self.cmax = max
    def muda_canal_para_baixo(self):
        if self.canal - 1 >= self.cmin:
            self.canal -= 1
    def muda_canal_para_cima(self):
        if self.canal + 1 <= self.cmax:
            self.canal += 1

tv_sala = Televisao(max=10)
tv_quarto = Televisao(min=0)

for i in range(10):
    tv_sala.muda_canal_para_cima()
    tv_quarto.muda_canal_para_baixo()

print(f"TV sala: {tv_sala.canal}")
print(f"TV quarto: {tv_quarto.canal}")