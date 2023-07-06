""" ENUNCIADO:
Altere o (programa6_7.py) de forma a poder trabalhar com vários comandos digitados de uma só vez.
Atualmente, apenas um comando pode ser inserido por vez. Altere-o de forma a considerar operação como uma string.

Exemplo: FFFAAAS significaria três chegadas de novos clientes, três atendimentos e, finalmente, a saída do programa.
"""

ultimo = 10
fila = list(range(1, ultimo + 1))
sair = False
while True:
    print(f"\nExistem {len(fila)} clientes na fila")
    print(f"Fila atual: {fila}")
    print("Digite F para adicionar um cliente ao fim da fila,")
    print("ou A para realizar o atendimento. S para sair.")
    operacao = input("Digite a string de operação: ")

    print("\nOperações realizadas: ")
    i = 0
    while i < len(operacao):
        opr = operacao[i]
        if opr == "A" or opr == "a":
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f"Cliente {atendido} atendido!")
            else:
                print(f"Fila vazia! Ninguém para atender.")
        elif opr == "F" or opr == "f":
            ultimo += 1
            fila.append(ultimo)
            print(f"Cliente {ultimo} adicionado a fila.")
        elif opr == "S" or opr == "s":
            sair = True
            break
        else:
            print(f"O comando inválido '{opr}' será ignorado e as outras operações serão realizadas.")
        i += 1
    if sair:
        break

print("Programa encerrado com sucesso!")