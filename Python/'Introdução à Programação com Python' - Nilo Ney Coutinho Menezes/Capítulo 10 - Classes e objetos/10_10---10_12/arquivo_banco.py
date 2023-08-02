from clientes import Cliente
from conta import Conta, ContaEspecial

joao = Cliente("João da Silva", "19 9 9123-4567")
jose = Cliente("Jose Aparecido", "21 3812-3456")

conta_joao = Conta(joao, 123, 500)
conta_jose = ContaEspecial(jose, 456, 500, 1000)

conta_joao.saque(100, 1000)
conta_joao.resumo()
conta_joao.extrato()
print()
conta_jose.saque(1450)
conta_jose.resumo()
conta_jose.extrato()