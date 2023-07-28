""" nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")
idade = int(input("Digite sua idade: "))
dinheiro = float(input("Digite seu saldo: "))

print(f"Seu nome é {nome}, você tem {idade} anos e possuí R${dinheiro:5.2f} no banco!") """


 ## Soma - Exercíco 3.7 - página 72
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
soma = num1 + num2

print(f"A soma dos dois números é {num1 + num2}")


""" ## Conversão para milimetros - Exercício 3.8 - página 72
numMetro = float(input("Digite o número em metros: "))
conversãoMilimetro = numMetro * 1000
print(f"O número {numMetro}m em milímetros é {conversãoMilimetro}mm") """


""" ## Conversor de tempo em segundos
dias = int(input("Digite a quantidade de dias: "))
diasSegundos = dias * 86400

horas = int(input("Digite a quantiade de horas: "))
horasSegundos = horas * 3600

minutos = int(input("Digite a quantidade de minutos: "))
minutosSegundos = minutos * 60

segundos = int(input("Digite a quantidade de segundos: "))

somaSegundos = diasSegundos + horasSegundos + minutosSegundos + segundos

print(f"Você digitou: {dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos.")
print(f"A conversão dessas medidas para segundos é: {somaSegundos} segundos") """



""" ## Aumento de salário - Exercício 3.10 - Página 72
salário = float(input("Digite o valor do salário: R$"))
percentualAumento = int(input("Digite o percentual de aumento do salário: "))

totalAumento = salário * percentualAumento / 100
salárioNovo = salário + totalAumento

print(f"O valor do aumento é de: R${totalAumento:.2f}")
print(f"O novo salário é de: R${salárioNovo:.2f}") """


""" ## Desconto em mercadoria - Exercício 3.11 - Página 72
preçoMercadoria = float(input("Digite o valor da mercadoria: R$"))
percentualDesconto = float(input("Digite o percentual de desconto: "))

valorDesconto = preçoMercadoria * percentualDesconto / 100
valorTotalComDesconto = preçoMercadoria - valorDesconto

print(f"O valor do desconto é de R${valorDesconto:.2f}")
print(f"O valor a se pagar é de R${valorTotalComDesconto:.2f}") """


""" ## Tempo viagem de carro - Exercício 3.12 - Página 72
distanciaViagem = float(input("Digite a distância total da viagem em km: "))
velocidadeMediaViagem = float(input("Digite a velocidade média do carro em km/h: "))

tempoViagem = (distanciaViagem * 1000) / (velocidadeMediaViagem / 3.6)

segundosDias = 3600 * 24
segundosHoras = 3600
segundosMinutos = 60

tempoViagemDias = tempoViagem // segundosDias
tempoViagemHoras = tempoViagem % segundosDias // segundosHoras
tempoViagemMinutos = tempoViagem % segundosDias % segundosHoras // segundosMinutos
tempoViagemSegundos = tempoViagem % segundosDias % segundosHoras % segundosMinutos

print(f"Tempo total de viagem: {tempoViagemDias} dias, {tempoViagemHoras} horas, {tempoViagemMinutos} minutos e {tempoViagemSegundos} segundos. ")
 """

""" ## Conversão de temperaturas - Exercício 3.13
temperaturaCelsius = float(input("Digite a temperatura em ºC: "))

temperaturaFahrenheit = (temperaturaCelsius * 9 / 5) + 32

print(f"A temperatura {temperaturaCelsius}ºC em Fahrenheit é {temperaturaFahrenheit}ºF") """


""" ## Aluguel de um carro - Exercício 3.14
diasAlugados = int(input("Digite a quantidade de dias que o carro foi alugado: "))
kmPercorridos = float(input("Digite a quantidade de kms rodados do carro alugado: "))

valorTotalAluguel = (diasAlugados * 60) + (kmPercorridos * 0.15)

print(f"Você alugou o carro por {diasAlugados} e percorreu {kmPercorridos:.2f} km")
print(f"O total a pagar pelo aluguel é de: R${valorTotalAluguel:.2f}")
 """


""" ## Cálculo de redução de vida de um fumante - Exercício 3.15
anosFumando = int(input("Há quantos anos você fuma? "))
cigarrosPorDia = int(input("Aproximadamente quantos cigarros você fuma por dia? "))

cigarrosTotalAnos = anosFumando * 365 * cigarrosPorDia
# Conversão de tempo em Segundos
totalPerdidoEmSegundos = (cigarrosTotalAnos * 10 * 60)

# Métricas de conversão para segundos
# Quantos segundos tem em: 
segundosDia = 86400
segundosHora = 3600
segundosMinuto = 60

# Primeiro é feito o agrupamento dos dias. Quantos dias exatos existem na quantidade total de segundos. Para fazer isso é dividido o número total de segundos sem que haja resto.
# Depois, com o resto da divisão de dias por segundo, é feito o agrupamento novamente, agora com horas, dividindo sem resto, o resto da divisão de dias, pela quantidade de segundos em uma hora.
# Assim por diante é feito o agrupamento do fator temporal, em cima do RESTO do agrupamento anterior.

diasPerdidos = totalPerdidoEmSegundos // segundosDia
horasPerdidas = totalPerdidoEmSegundos % segundosDia // segundosHora
minutosPerdidos = totalPerdidoEmSegundos % segundosDia % segundosHora // segundosMinuto
segundosPerdidos = totalPerdidoEmSegundos % segundosDia % segundosHora % segundosMinuto

print(f"Você perdeu {diasPerdidos:.0f} dias, {horasPerdidas:.0f} horas, {minutosPerdidos:.0f} minutos e {segundosPerdidos:.0f} segundos de vida fumando.") """