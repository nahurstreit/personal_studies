""" ENUNCIADO:
Modifique o programa (9_1.py) para que receba mais dois parâmetros:
a linha de início e a de fim para impressão. O programa deve imprimir apenas as linhas entre
esses dois valores (incluindo as linhas de início e fim).
"""

while True:
    arq = input("Digite o nome do arquivo de texto (sem digitar a extensão '.txt'): ")
    arq += ".txt"
    try: #Tentando abrir o arquivo
        with open (arq, "r") as arquivo:
            #Recebendo quantidade de linha válida do arquivo:
            inicio, fim = None, None
            while inicio is None or fim is None:
                try:
                    if inicio is None:
                        inicio = int(input("Digite a linha em que quer começar: "))
                        if inicio <= 0:
                            inicio = None
                            raise ValueError()
                    if fim is None:
                        fim = int(input("Digite a linha em que quer terminar: "))
                        if fim <= 0:
                            fim = None
                            raise ValueError()
                except ValueError:
                    print("Digite apenas NÚMEROS maiores do que zero.")

            print(f"\nImprimindo o conteúdo do arquivo encontrado entre as linhas {inicio} e {fim}:")
            for i, linha in enumerate(arquivo.readlines()):
                if inicio - 1 <= i <= fim - 1:
                    print(linha, end="")
        
        break #Break do while principal

    except Exception: #Except caso o arquivo não possa ser aberto
        print("Não foi possível abrir o arquivo. Tente novamente.\n")