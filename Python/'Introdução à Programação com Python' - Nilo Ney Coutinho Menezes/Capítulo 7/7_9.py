""" ENUNCIADO: 
Modifique o (programa7_2.py) para utilizar listas de strings para desenhar o boneco da forca.
Você pode utilizar uma lista para cada linha_forca e organizá-las em uma lista de listas.
Em vez de controlar quando imprimir cada parte, desenhe nessas listas, substituindo o elemento a desenhar.
    Exemplo colocando comandos no IDLE de Python:
        >>> linha_forca = list("X------")
        >>> linha_forca
        ['X', '-', '-', '-', '-', '-', '-', '-']
        >>> linha_forca[6] = "|"
        >>> linha_forca
        ['X', '-', '-', '-', '-', '-', '-', '|']
        >>> "".join(linha_forca)
        'X-----|'
"""

palavra = input("Digite a palavra secreta: ").lower().strip()
for x in range(100):
    print()
digitadas = []
acertos = []
erros = 0
forca = ["X==:==",
         "X  : ",
         "X  ",
         "X ",
         "X ",
         "X\n==========="]
boneco = ["O ", "\\", "|", "/", "/ ", "\\"]
linha_forca = 2
while True:
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else "."
    print(senha)
    if senha == palavra:
        print("Você acertou!")
        break
    tentativa = input("\nDigite uma letra: ").lower().strip()
    if tentativa in digitadas:
        print("Você já tentou esta letra!")
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            forca[linha_forca] += boneco[erros - 1]
            if len(forca[linha_forca]) >= 5: linha_forca += 1
            for e in forca:
                print(e)
            print("Você errou!")
        if erros == 6:
            print("Enforcado!")
            print(f"A palavra secreta era: {palavra}")
            break