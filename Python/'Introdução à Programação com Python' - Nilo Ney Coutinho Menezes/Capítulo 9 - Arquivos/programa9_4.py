"""
Cópia do Programa 9.3 do livro (página 199 - Capítulo 9) - Gravação de números pares e ímpares em 
arquivos diferentes usando with em uma só linha.
Programa necessário para gerar os arquivos de texto "impares.txt" e "pares.txt" para a resolução
dos exercícios (9_3.py) e (9_5.py) e também para servir de exemplo no exercício (9_4.py).
"""

with open("impares.txt", "w") as impares, open("pares.txt", "w") as pares:
    for n in range(0, 1000):
        if n % 2 == 0:
            pares.write(f"{n}\n")
        else:
            impares.write(f"{n}\n")