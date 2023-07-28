""" ENUNCIADO:
Modifique o programa do exercício (9_11.py) para também registrar a linha e a coluna de cada ocorrência da palavra
no arquivo. Para isso, utilize listas nos valores de cada palavra, guardando a linha e a coluna de cada ocorrência.
"""

dicionario = {}

def atualizarOcorrencia(palavra, num_ocorrencias, posicoes):
    global dicionario
    dicionario[palavra] = (num_ocorrencias, posicoes) #Substitui o valor atual do dicionário pelas novas informações

while True:
    nome_arquivo = input("Digite o nome do arquivo: ") + ".txt"
    try:
        with open(nome_arquivo) as arquivo:
            qtd_linha = 1
            for linha in arquivo.readlines():
                linha = linha.lower()
                conteudoLinha = linha.replace(",", "").split(" ") #faz o tratamento tirando ',' e separando cada palavra por espaço
                for palavra in conteudoLinha:
                    if palavra not in list(dicionario.keys()): #Se a palavra não estiver no dicionário ainda
                        atualizarOcorrencia(palavra, 1, [(linha.find(palavra), qtd_linha)]) #Cria a chave do dicionário com o valor de uma tupla sendo: o primeiro valor da tupla é a quantidade total de ocorrências, o segundo valor da tupla é uma lista de tuplas, da qual cada item da lista é uma tupla de posições (coluna, linha).
                    else:
                        ocorrencias, posicoes = dicionario[palavra] #Em um segundo resultado daquela mesma palavra, a tupla daquela chave é dividida em ocorrências e posições. A ocorrência é acrescida de uma unidade e as posições, que é uma lista de tupla, recebe um append para a nova posição.
                        ocorrencias += 1
                        posicoes.append((linha.find(palavra, posicoes[-1][0] + 1), qtd_linha)) #O append da lista é feito com uma tupla contendo (coluna, linha), onde a coluna deve ser igual ao próximo resultado da palavra na linha, onde o valor de início da procura deve ser o último valor armazenado na lista daquela chave.
                        atualizarOcorrencia(palavra, ocorrencias, posicoes)
                qtd_linha += 1
        break

    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado. Digite novamente.")
        continue

print(dicionario)