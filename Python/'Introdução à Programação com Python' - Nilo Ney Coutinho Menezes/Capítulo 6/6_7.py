""" ENUNCIADO:
Faça um programa que leia uma expressão com parênteses. Usando pilhas, verifique se os parênteses foram abertos
e fechados na ordem correta.
    Exemplo:
        (())         OK
        ()()(()())   OK
        ())          Erro
Você pode adicionar elementos à pilha sempre que encontrar abre parênteses e desempilhá-la a cada fecha parênteses.
Ao desempilhar, verifique se o topo da pilha é um abre parênteses. 
Se a expressão estiver correta, sua pilha estará vazia no final
"""

pilha = []
string = input("Digite a expressão com parênteses: ")

i = 0
while i < len(string):
    st = string[i]
    if st == "(":
        pilha.append(st)
    elif st == ")":
        if len(pilha) > 0 and pilha[-1] == "(":
            pilha.pop(-1)
        else:
            pilha.append(st)
    i += 1

if len(pilha) > 0: print("Erro!")
else: print("Ok!")