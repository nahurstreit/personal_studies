""" ENUNCIADO:
Crie um arquivo que receba uma lista de nomes de arquivo e que gere apenas um grande arquivo de saída.
"""

lidos = 0

nome_final = input("Digite o nome do arquivo de saída: ")
nome_final += ".txt"

print("""Digite o nome dos arquivos que você quer juntar.
Digite individualmente ou uma lista separada por vírgulas.
Todos sem extensão e não são permitidos arquivos com espaços.
      
Ou então digite Enter para encerrar o programa.""")

lidos = 0
while True:
    if lidos > 0:
        print("Digite o nome do(s) próximo(s) arquivo(s): ")
    nome_arquivo = input("\nNome: ")
    if len(nome_arquivo) == 0:
        break
    
    arquivos = nome_arquivo.split().split(",")

    for arquivo in arquivos:
        arquivo += ".txt"
        try:
            with open(arquivo, "r") as original:
                with open(nome_final, "a") as final:
                    final.write(f"Arquivo {arquivo}: \n")
                    for linha in original.readlines():
                        final.write(f"{linha}\n")
                    lidos += 1
        
        except FileNotFoundError:
            print(f"O arquivo '{arquivo}' não foi encontrado{' e será ignorado.' if len(arquivos) > 1 else '. Digite novamente.'}")
            continue

print(f"Programa encerrado com sucesso após juntar {lidos} arquivos.")