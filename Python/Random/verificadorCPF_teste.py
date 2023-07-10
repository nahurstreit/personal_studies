def checkDigit(cpf, maxRange):
    digit = 0
    for i, j in zip(range(maxRange), range(maxRange, 1, -1)):
        digit += int(cpf[i]) * j
    digit = 11 - (digit % 11)
    return digit if digit < 10 else 0

while True:
    while True:
        cpf = input("Digite o seu CPF: ").translate(str.maketrans("", "", ".,- "))
        if cpf.isnumeric():
            if len(cpf) == 11:
                break
            print("\nQuantidade de números inválida. Um CPF tem obrigatoriamente 11 números.")
            continue
        print("\nNão digite letras!")

    if int(cpf[-2]) != checkDigit(cpf, 10) or int(cpf[-1]) != checkDigit(cpf, 11):
        print("CPF inválido! Tente novamente.")
        continue

    break

print("O CPF {}.{}.{}-{} é válido!".format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:]))