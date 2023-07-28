""" ENUNCIADO:
Modifique o programa para que aceite respostas com letras maiúsculas e minúsculas em todas as questões.
    Programa:
        pontos = 0
        questao = 1
        while questao <= 3:
            resposta = input(f"Resposta da questão {questao}: ")
            if questao == 1 and resposta == "b":
                pontos = pontos + 1
            if questao == 2 and resposta == "a":
                pontos = pontos + 1
            if questao == 3 and resposta == "d":
                pontos = pontos + 1
            questao = questao + 1
            print(f"O aluno fez {pontos} ponto(s).")     
"""

sz_Title_Total = 50
txt_Title = "CORREÇÃO DA PROVA"
space_Title = (sz_Title_Total - len(txt_Title))//2 if sz_Title_Total - len(txt_Title) > 0 else 5
sz_Title_Side = "#" * space_Title

print(f"{sz_Title_Side} {txt_Title} {sz_Title_Side}\n")

pontos = 0
questao = 1

while questao <= 3:
    resposta = input(f"Digite a resposta para a questão {questao}: ")
    if questao == 1 and (resposta == 'b' or resposta == 'B'):
        pontos += 1
    elif questao == 2 and (resposta == "a" or resposta == "A"):
        pontos += 1
    elif questao == 3 and (resposta == "d" or resposta == "D"):
        pontos += 1
    questao += 1

print(f"\n{'#' * ((len(sz_Title_Side) * 2) + len(txt_Title) + 2)}\n")

print(f"O aluno fez {pontos} ponto(s)")