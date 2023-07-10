""" ENUNCIADO:
Escreva uma função que receba uma string e uma lista. A função deve comparar a string passada com os 
elementos da lista, também passada como parâmetro. Retorne verdadeiro se a string for encontrada 
dentro da lista, e falso, caso contrário.
"""

def findLista(string, lista):
    if string in lista:
        return True
    return False

lista = ["banana", "café", "refrigerante", "cebola", "arroz"]
string = input("Digite uma palavra para pesquisar na lista de compras: ")

print(findLista(string, lista))