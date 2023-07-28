""" ENUNCIADO:
Escreva uma função para validar uma variável string. Essa função recebe como parâmetro a string,
o número mínimo e o número máximo de caracteres. Retorne verdadeiro se o tamanho da string estiver
entre os valores de máximo e mínimo, e falso, caso contrário.

"""
def validarTamanho(string, min, max):
    if len(string) >= min and len(string) <= max: return True
    return False

string = input("Digite uma string: ")
print(validarTamanho(string, 5, 10))