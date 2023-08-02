from clientes import Cliente
from conta import Conta

joao = Cliente("João da Silva", "19 9 9123-4567")
jose = Cliente("Jose Aparecido", "21 3812-3456")

conta_joao = Conta(joao, 123, 500)
conta_jose = Conta(jose, 345, 500)

conta_joao.resumo()
conta_joao.extrato()
conta_jose.resumo()
conta_jose.extrato()