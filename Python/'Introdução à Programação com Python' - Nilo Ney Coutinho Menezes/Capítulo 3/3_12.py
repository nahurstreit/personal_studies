""" ENUNCIADO:
Escreva um programa que calcule o tempo de uma viagem de carro.
Pergunte a distância a percorrer e a velocidade média esperada para a viagem.
"""

sz_Title_Total = 40
txt_Title = "CALCULAR TEMPO DE VIAGEM"
space_Title = (sz_Title_Total - len(txt_Title))//2 if sz_Title_Total - len(txt_Title) > 0 else 5
sz_Title_Side = "#" * space_Title

print(f"{sz_Title_Side} {txt_Title} {sz_Title_Side}\n")

distancia = float(input("Digite a distância total da viagem em km: "))
distancia *= 1000
velocidade_media = int(input("Digite a velocidade média do veículo em km/h: "))
velocidade_media /= 3.6

tempo_Total = distancia / velocidade_media

tempoDias, tempoHoras = divmod(tempo_Total, (24 * 60 * 60))
tempoHoras, tempoMinutos = divmod(tempoHoras, (60 * 60))
tempoMinutos, tempoSegundos = divmod(tempoMinutos, 60)

#tempoDias = tempo_Total // (24 * 60 * 60)
#tempoHoras = (tempo_Total % (24 * 60 * 60)) // (60 * 60) 
#tempoMinutos = ((tempo_Total % (24 * 60 * 60)) % (60 * 60)) // 60
#tempoSegundos = ((tempo_Total % (24 * 60 * 60)) % (60 * 60)) % 60

print(f"\n{'#' * ((len(sz_Title_Side) * 2) + len(txt_Title) + 2)}\n")

print("Com as informações passadas a viagem demorará:\n")
print(f"{tempoDias} dias,\n{tempoHoras} horas,\n{tempoMinutos} minutos e\n{tempoSegundos} segundos.")