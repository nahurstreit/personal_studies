"""
Modificação do arquivo (conta.py) da página 230 e 231 - Capítulo 10, para resolução dos exercícios (10_06),
(10_07) e (10_08).
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
    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(["SAQUE", valor])
        else:
            print(f"Saldo insuficiente! Saldo atual: R$ {self.saldo:.2f}")
    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(["DEPÓSITO", valor])
    def extrato(self):
        print(f"Extrato CC Nº {self.numero}\n")
        for o in self.operacoes:
            print(f"    {o[0]:10s} R$ {o[1]:10.2f}")
        print(f"Saldo: R$ {self.saldo:10.2f}\n")