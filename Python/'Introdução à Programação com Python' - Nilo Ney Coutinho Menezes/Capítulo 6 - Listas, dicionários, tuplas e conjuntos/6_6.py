""" ENUNCIADO:
Modifique o (programa6_7.py) para trabalhar com duas filas. 
Para facilitar seu trabalho, considere o comando A para o atendimento da fila 1; e B, para o atendimento da fila 2.
O mesmo para a chegada de clientes: F para a fila 1; e G, para a fila 2.
"""

ultimo1 = 10
fila1 = list(range(1, ultimo1 + 1))
ultimo2 = 7
fila2 = list(range(1, ultimo2 + 1))
sair = False
while True:
    print(f"\nExistem {len(fila1)} clientes na Fila 1: {fila1}")
    print(f"Existem {len(fila2)} clientes na Fila 2: {fila2}")

    if sair:
        break

    print(f"\n{'#'* 5} Operações disponíveis {'#'* 5} ")
    print("ADICIONAR um cliente:")
    print("Fila 1: Digite 'F'\tFila 2: Digite 'G'\n")
    print("ATENDER o próximo cliente:")
    print("Fila 1: Digite 'A'\tFila 2: Digite 'B'\n")
    print("Digite as letras das operações que você deseja realizar.\nOu então, digite 'S' para sair.")
    operacao = input("Digite a string de operação: ")

    print("\nOperações realizadas: ")
    i = 0
    while i < len(operacao):
        opr = operacao[i]
        if opr == "A" or opr == "a":
            if len(fila1) > 0:
                atendido = fila1.pop(0)
                print(f"Cliente {atendido} da Fila 1 foi atendido!")
            else:
                print(f"Fila 1 vazia! Ninguém para atender.")
        elif opr == "B" or opr == "b":
            if len(fila2) > 0:
                atendido = fila2.pop(0)
                print(f"Cliente {atendido} da Fila 2 foi atendido!")
            else:
                print(f"Fila 2 vazia! Ninguém para atender.")
        elif opr == "F" or opr == "f":
            ultimo1 += 1
            fila1.append(ultimo1)
            print(f"Cliente {ultimo1} adicionado à Fila 1.")
        elif opr == "G" or opr == "g":
            ultimo2 += 1
            fila2.append(ultimo2)
            print(f"Cliente {ultimo2} adicionado à Fila 2.")
        elif opr == "S" or opr == "s":
            sair = True
            break
        else:
            print(f"O comando inválido '{opr}' será ignorado e as outras operações serão realizadas.")
        i += 1

print("Programa encerrado com sucesso!")