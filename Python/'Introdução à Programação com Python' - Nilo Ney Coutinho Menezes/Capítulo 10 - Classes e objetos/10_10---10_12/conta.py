"""
Modificação do arquivo (conta.py) da página 230 e 231 - Capítulo 10, para resolução dos exercícios (10_10),
(10_11) e (10_12).
"""

class Conta:
    def __init__(self, _cliente, numero, saldo_init=0):
        self.saldo = 0
        self.cliente = _cliente
        self.numero = numero
        self.operacoes = []
        self.deposito(saldo_init)
    
    def resumo(self):
        print(f"Cliente: {self.cliente.nome}\tTelefone: {self.cliente.telefone}")
        print(f"CC Nº{self.numero}\tSaldo: R$ {self.saldo:10.2f}")

    def saque(self, valor, *args):
        if len(args) > 0 and isinstance(self, ContaEspecial): limite = args[0]
        else: limite = 0

        if self.verificarSaque((self.saldo + limite), valor):
            self.saldo -= valor
            self.operacoes.append(["SAQUE", valor])
            return True

        print(f"Saldo insuficiente! Saldo atual: R$ {self.saldo:.2f}")
        return False
    
    @staticmethod
    def verificarSaque(disponivel, valor):
        if disponivel >= valor:
            return True
        return False

    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(["DEPÓSITO", valor])

    def extrato(self):
        print(f"\nExtrato CC Nº {self.numero}\n")
        if len(self.operacoes) > 0:
            for operacao in self.operacoes:
                print(f"    {operacao[0]:10s} R$ {operacao[1]:10.2f}")
        else:
            print(f"    Nenhuma movimentação recente.")
        print(f"\nSaldo: R$ {self.saldo:10.2f}")


class ContaEspecial(Conta):
    def __init__(self, cliente, numero, saldo=0, limiteConta=0):
        self.limiteConta = limiteConta
        self.limiteAtual = limiteConta
        Conta.__init__(self, cliente, numero, saldo)

    def saque(self, valor):
        super().saque(valor, self.limiteAtual)
        if self.saldo < 0:
            self.limiteAtual += self.saldo
    
    def deposito(self, valor):
        super().deposito(valor)
        if self.saldo >= 0:
            self.limiteAtual = self.limiteConta
        else:
            self.limiteAtual += valor

    def aumentarLimiteConta(self, valor):
        self.limiteConta += valor
        self.limiteAtual += valor

    def extrato(self):
        super().extrato()
        print(f"Limite Atual: R$ {self.limiteAtual:10.2f}")