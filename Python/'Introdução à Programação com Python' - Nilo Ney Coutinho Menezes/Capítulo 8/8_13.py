""" ENUNCIADO:
Escreva uma função que receba uma string com as opções válidas a aceitar (cada opção é uma letra).
Converta as opções válidas para letras minúsculas. Utilize input para ler uma opção, converter o valor
para letras minúsculas e verificar se a opção é válida. Em caso de opção inválida, a função deve pedir
ao usuário que digite novamente outra opção.
"""

G_VALIDAS = []

def criarValidas(string):
    global G_VALIDAS
    for letra in string.lower().replace(" ", ""):
        if letra not in G_VALIDAS:
            G_VALIDAS.append(letra)

def validarOpcao(char):
    if char in G_VALIDAS: return True
    return False

criarValidas(input("Digite uma string para criar as opções válidas: "))

print()
valido = False
while not valido:
    for element in G_VALIDAS:
        print(f"Opção [{element}]")
    escolha = input("Opção escolhida: ").lower()
    valido = validarOpcao(escolha[0])
    if not valido:
        print("\nOpção incorreta! Digite novamente.")

print("Opção correta!! Programa encerrado.")