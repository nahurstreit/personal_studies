"""
Para a resolução dos exercícios (10_2) e (10_3), use:
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
ENUNCIADO 10_2: Atualmente, a classe Televisão inicializa o canal com 2. Modifique a classe Televisão de
forma a receber o canal inicial em seu construtor.

ENUNCIADO 10_3: Modifique a classe Televisão de forma que, se pedirmos para mudar o canal para baixo, além do 
mínimo, ela vá para o canal máximo. Se mudarmos para cima, além do máximo, que volte ao canal mínimo.
"""

class Televisao:
    def __init__(self, canal_inicio, min, max):
        self.ligada = False
        self.canal = canal_inicio
        self.cmin = min
        self.cmax = max
    def muda_canal_para_baixo(self):
        if self.canal - 1 >= self.cmin:
            self.canal -= 1
        else:
            self.canal = self.cmax
    def muda_canal_para_cima(self):
        if self.canal + 1 <= self.cmax:
            self.canal += 1
        else:
            self.canal = self.cmin

tv = Televisao(5, 1, 10)
for i in range(6):
    tv.muda_canal_para_cima()
    print(tv.canal)