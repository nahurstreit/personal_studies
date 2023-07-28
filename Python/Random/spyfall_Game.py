import random
import os

MIN_PLAYERS = 4

players_roles = {}
choosed_roles = []
players = []
matches = {}
cenes = {"Base Militar": ["Atirador de Elite", "Cabo", "Sargento", "Desertor", "Enfermeiro", "Médico", "Intérprete", "Espião Infiltrado", "Engenheiro de Armas", "Comunicador", "Controlador de Radar", "Técnico de Comunicações", "Motorista de Veículo Blindado", "Soldado de Infantaria", "Cientista de Armas", "Analista de Inteligência", "Instrutor de Treinamento", "Quartel-Mestre", "Batedor", "Guarda de Segurança"],
         "Estação Espacial": ["Astronauta", "Comandante", "Engenheiro", "Explorador", "Biólogo Espacial", "Médico Espacial", "Piloto de Nave Espacial", "Oficial de Comunicações", "Cientista de Pesquisa", "Especialista em Gravidade Zero", "Operador de Robô", "Técnico de Reparos", "Guarda de Segurança Espacial", "Controlador de Navegação", "Meteorologista Espacial", "Técnico de Propulsão", "Operador de Laboratório", "Controlador de Energia", "Especialista em Experiências Científicas", "Tripulante Novato"],
         "Navio de Cruzeiro": ["Capitão", "Oficial de Navegação", "Médico", "Engenheiro de Máquinas", "Camareiro", "Garçom", "Animador de Eventos", "Cozinheiro Chefe", "Hóspede VIP", "Técnico de Entretenimento", "Barman", "Fotógrafo de Bord", "Instrutor de Dança", "Salva-Vidas", "Funcionário da Lavanderia", "Croupier do Cassino", "Funcionário de Recepção", "Guia Turístico", "Operador de Piscina", "Técnico de Som e Luz"],
         "Circo": ["Mestre de Cerimônias", "Equilibrista", "Palhaço", "Malabarista", "Trapezista", "Domador de Leões", "Engolidor de Espadas", "Acrobata", "Contorcionista", "Artista de Fogo", "Bailarina Aérea", "Ilusionista", "Cartomante", "Carpinteiro de Palco", "Costureiro de Fantasias", "Gerente de Bilheteria", "Maquiador", "Assistente de Palco", "Vendedor de Pipoca", "Responsável por Cuidar dos Animais"],
         "Estúdio de Cinema": ["Diretor", "Ator Principal", "Roteirista", "Câmera", "Produtor", "Figurinista", "Maquiador", "Assistente de Produção", "Técnico de Efeitos Especiais", "Dublê", "Assistente de Direção", "Coordenador de Ação", "Tratador de Animais", "Especialista de Som", "Operador de Claque", "Guarda de Segurança", "Estagiário", "Eletricista", "Responsável por Cenários", "Editor de Vídeo"],
         "Hospital": ["Médico", "Enfermeiro", "Cirurgião", "Anestesista", "Paciente", "Técnico de Laboratório", "Farmacêutico", "Recepcionista", "Terapeuta", "Assistente Social", "Bombeiro", "Ambulância", "Radiologista", "Técnico de Raio-X", "Responsável por Limpeza", "Voluntário", "Respiratório", "Enfermeiro de UTI", "Psiquiatra", "Fisioterapeuta"],
         "Escola de Magia": ["Mago", "Bruxo", "Feiticeiro", "Aluno de Primeiro Ano", "Professor de Poções", "Instrutor de Feitiços", "Guardião da Biblioteca", "Mestre das Criaturas Mágicas", "Espectador de Duelo", "Assistente de Professor", "Aluno de Último Ano", "Espectador do Jogo de Quadribol", "Guarda da Escola", "Enfermeira da Enfermaria", "Responsável pelos Corredores", "Zelador", "Professor de Transfiguração", "Professor de Defesa Contra as Artes das Trevas", "Professor de História da Magia", "Professor de Adivinhação"],
         "Banco": ["Gerente de Banco", "Caixa", "Consultor Financeiro", "Investidor", "Assaltante", "Segurança", "Gerente de Contas", "Atendente de Serviço ao Cliente", "Técnico de TI", "Analista de Risco", "Advogado Bancário", "Gerente de Empréstimos", "Tesoureiro", "Especialista em Fraude", "Coletor de Dívidas", "Revisor de Documentos", "Economista", "Estagiário de Banco", "Responsável por Depósitos", "Operador de Caixa Eletrônico"],
         "Zoológico": ["Zoólogo", "Veterinário", "Tratador de Animais", "Biologista", "Visitante", "Guia do Zoológico", "Cuidador de Répteis", "Cuidador de Aves", "Cuidador de Mamíferos", "Cuidador de Aquário", "Educador de Conservação", "Fotógrafo de Vida Selvagem", "Biólogo Marinho", "Cuidador de Primatas", "Pesquisador de Animais", "Técnico de Manutenção", "Responsável por Alimentação", "Voluntário do Zoológico", "Limpeza de Recintos", "Biólogo de Comportamento Animal"],
         "Mansão Assombrada": ["Fantasma", "Detetive Paranormal", "Caçador de Fantasmas", "Sensitivo", "Curador", "Exorcista", "Guardião da Mansão", "Convidado Inocente", "Responsável pela Limpeza", "Bibliotecário", "Zelador da Mansão", "Responsável por Cuidar do Jardim", "Médium", "Fotógrafo Paranormal", "Assistente de Detetive", "Jogador de Tabuleiro Assombrado", "Hóspede Curioso", "Vendedor de Bugigangas Esotéricas", "Pesquisador de História da Mansão", "Cético em Potencial"],
         "Estação de Trem": ["Maquinista", "Controlador de Bilhetes", "Passageiro Atrasado", "Responsável pelo Bagageiro", "Chefe de Estação", "Maquinista Novato", "Condutor", "Responsável pela Limpeza", "Inspetor de Segurança", "Companheiro de Viagem", "Responsável pelas Reservas", "Atendente do Café", "Fotógrafo de Viagem", "Responsável pelo Controle de Multidão", "Passageiro Turista", "Estagiário de Ferrovia", "Guarda de Segurança", "Responsável por Manutenção", "Mecânico de Trem", "Consultor de Viagens"],
         "Estúdio de TV": ["Apresentador de TV", "Câmera", "Produtor", "Diretor de Programa", "Estagiário de TV", "Técnico de Áudio", "Figurinista", "Técnico de Iluminação", "Operador de Switcher", "Maquiador", "Redator de Roteiro", "Engenheiro de Transmissão", "Assistente de Produção", "Responsável por Cenários", "Convidado Especial", "Teleprompter", "Entrevistador", "Público de Plateia", "Responsável por Efeitos Especiais", "Editor de Vídeo"],
         "Submarino": ["Capitão", "Navegador", "Engenheiro de Propulsão", "Oficial de Sonar", "Responsável por Mantimentos", "Mergulhador", "Técnico de Comunicações", "Responsável por Torpedos", "Oficial Médico", "Cozinheiro Submarino", "Guarda de Segurança Subaquático", "Especialista em Sistemas de Ar", "Responsável por Armas", "Mecânico de Submarino", "Responsável por Recursos Hídricos", "Técnico de Radar", "Batedor Submarino", "Operador de Compressor", "Especialista em Contramedidas", "Marinheiro Novato"],
         "Estádio de Esportes": ["Jogador de Futebol", "Treinador", "Árbitro", "Narrador Esportivo", "Fã Enlouquecido", "Responsável pelo Gramado", "Responsável por Vendas de Ingressos", "Cameraman Esportivo", "Médico Esportivo", "Torcedor Leal", "Comentarista", "Fotógrafo Esportivo", "Responsável por Segurança", "Técnico de Iluminação", "Jogador Reserva", "Fisioterapeuta", "Cheerleader", "Jornalista Esportivo", "Responsável pelo Controle de Multidão", "Estagiário de Esportes"],
         "Estação de Esqui": ["Instrutor de Esqui", "Monitor de Snowboard", "Responsável por Aluguel de Equipamentos", "Atendente de Teleférico", "Esquiador Profissional", "Responsável pela Patrulha de Pista", "Responsável pela Manutenção", "Operador de Teleférico", "Turista Empolgado", "Responsável pelo Controle de Multidão", "Fotógrafo de Esqui", "Vendedor de Lanches", "Responsável pela Loja de Souvenirs", "Responsável por Aulas de Iniciação", "Snowboarder Aventureiro", "Responsável pelo Resgate", "Responsável por Limpeza", "Estagiário de Estação de Esqui", "Médico de Montanha", "Responsável pela Segurança na Montanha"],
         "Carnaval": ["Mestre de Cerimônias", "Acrobata", "Palhaço", "Equilibrista", "Malabarista", "Dançarino de Samba", "Rainha do Carnaval", "Rei Momo", "Artista de Rua", "Folião Fantasiado", "Mestre-Sala", "Porta-Bandeira", "Responsável por Vendas de Ingressos", "Responsável por Efeitos Especiais", "Vendedor de Comida de Rua", "Maquiador de Carnaval", "Guarda de Segurança", "Responsável por Organização de Eventos", "Estagiário de Carnaval", "Sambista"],
         "Estúdio de Jogos de Vídeo": ["Desenvolvedor de Jogos", "Designer de Níveis", "Programador", "Artista Conceitual", "Tester de Jogos", "Responsável por Som", "Escritor de Histórias", "Animador", "Designer de Personagens", "Responsável por Efeitos Especiais", "Gerente de Projeto", "Responsável por Monetização", "Produtor de Jogos", "Designer de Interface", "Estagiário de Jogos", "Responsável por Marketing", "Community Manager", "Gerente de Comunidade", "Especialista em Jogabilidade", "Cinematic Designer"],
         "Praia": ["Salva-Vidas", "Instrutor de Surfe", "Barman da Barraca de Praia", "Vendedor de Sorvetes", "Turista com Câmera Fotográfica", "Guarda-Sol e Cadeira de Praia", "Responsável por Aluguel de Equipamentos Aquáticos", "Fotógrafo de Praia", "Vendedor de Frutas Tropicais", "Criança com Pipa", "Jogador de Frescobol", "Pescador", "Instrutor de Mergulho", "Atendente de Quiosque de Bebidas", "Responsável pela Limpeza da Praia", "Colecionador de Conchas", "Treinador de Beach Volley", "Artista de Escultura de Areia", "Estagiário de Praia", "Apanhador de Sol"],
         "Navio Pirata": ["Capitão Pirata", "Timoneiro", "Navegador", "Artilheiro de Canhão", "Saqueador de Tesouros", "Cozinheiro de Bordo", "Marujo", "Baleeiro", "Contramestre", "Especialista em Navegação Estelar", "Ferreiro Pirata", "Espião Disfarçado", "Boticário de Poções", "Mestre do Mapa do Tesouro", "Músico Pirata", "Médico de Bordo", "Responsável por Manutenção", "Escalador de Mastros", "Lutador de Espadas", "Estagiário Pirata"],
         "Escola": ["Diretor", "Professor de Matemática", "Professor de Língua Portuguesa", "Professor de Ciências", "Professor de História", "Professor de Geografia", "Professor de Inglês", "Professor de Educação Física", "Professor de Artes", "Professor de Música", "Professor de Informática", "Bibliotecário", "Enfermeira da Escola", "Responsável pela Secretaria", "Responsável pelo Pátio", "Responsável pela Cantina", "Responsável pela Limpeza", "Monitor de Recreação", "Aluno"],
}

def clearScreen(text=''):
    if text != '':
        input(text)
    
    for i in range(10):
            print()
    os.system("cls")

def logoScreen():
    clearScreen()
    print("""
   _____ _______     ________      _      _      
  / ____|  __ \ \   / /  ____/\   | |    | |     
 | (___ | |__) \ \_/ /| |__ /  \  | |    | |     
  \___ \|  ___/ \   / |  __/ /\ \ | |    | |     
  ____) | |      | |  | | / ____ \| |____| |____ 
 |_____/|_|      |_|  |_|/_/    \_\______|______|              
                                                 
""")
    
def filterChoice(text, right_answer):
    print(text)
    if input("Escolha: ") != right_answer:
        return False
    return True

def howToPlay():
    logoScreen()
    print("""
O QUE É SPYFALL?
Spyfall é um jogo de festa social que foi criado por Alexandr Ushan em 2014. O jogo é baseado em dedução e blefe, e é uma atividade muito divertida para se jogar em encontros sociais e eventos com amigos.
A premissa do jogo é que todos os jogadores, exceto um, são agentes secretos em uma localização específica, como um cassino, submarino, parque temático ou qualquer outro lugar. Um dos jogadores é designado como "impostor" e não sabe onde eles estão. O objetivo dos agentes secretos é descobrir quem é o impostor sem revelar a localização para ele.
O jogo é jogado em rodadas, e em cada rodada, os jogadores fazem perguntas uns aos outros, tentando obter informações sobre a localização sem serem muito óbvios e dar pistas ao impostor. Por outro lado, o impostor tenta disfarçar sua falta de conhecimento sobre a localização e fazer perguntas que o ajudem a descobrir onde está.
O jogo termina quando os jogadores tentarem iniciar uma votação para acusar o impostor (podendo acertar ou não) ou quando o impostor for suficientemente capaz de deduzir em qual localidade eles estão.


          
COMO JOGAR:
1 - Preparação:
Primeiro deverão ser adicionados quantos jogadores participarão da partida, para isso inicie a partida e insira o nome de todos os jogadores. Caso dois ou mais jogadores compartilhem o mesmo nome, você terá a opção de adicionar um sobrenome.
Em seguida o programa perguntará quantos impostores os jogadores querem ter na partida, fazendo uma sugestão de 01 (um) impostor para cada 8 jogadores no total.
Depois de adicionar os jogadores e selecionar a quantidade de impostores o programa selecionará aleatoriamente um local e função para todos os jogadores.

2 - Início do jogo:
O programa exibirá uma lista enumerada com todos os jogadores.
Cada jogador, um por vez, digita o número correspondente ao seu nome para visualizar sua função e localização.
Após visualizar, o jogador pressiona qualquer tecla e passar a vez para o próximo jogador.
          
3 - Rodadas de perguntas e respostas:
A rodada começa com o primeiro jogador fazendo uma pergunta para outro jogador da lista (ex: "Jogador 1 pergunta para Jogador 3: O que você está bebendo?").
O jogador questionado responde de forma vaga, tentando não revelar sua localização, mas também com informações não muito genéricas.

4 - Acusação, votação e fim do jogo:
A qualquer momento durante a rodada, os jogadores podem acusar alguém de ser o impostor.
O jogo quando os jogadores decidirem iniciar uma votação para acusar o impostor ou quando o impostor deduzir o local em que todos estão.
""")

def registerPlayers():
    global cene, roles, players, players_roles, choosed_roles, MIN_PLAYERS

    add_new = True
    logoScreen()
    if len(players) != 0:
        if filterChoice("Continuar partida com os mesmos jogadores?\n[1] Sim\t\t[2] Não","2"):
            players = []
        else:
            add_new = filterChoice("Adicionar mais jogadores?\n[1] Sim\t\t[2] Não", "1")
        
    while True and add_new:
        try:
            player_name = input(f"Digite o nome do {len(players) + 1}º jogador: ")
            if player_name in players:
                while True:
                    player_name = f"{player_name} {input(f'Você já registrou uma pessoa chamada {player_name}, digite um sobrenome: ')}"
                    if player_name not in players:
                        break
            players.append(player_name)
            if len(players) < MIN_PLAYERS:
                continue
            else:
                if filterChoice("Digitar mais um jogador?\n[1] Sim\t\t[2] Não", "1"):
                    continue
            break
        except Exception as erro:
            print(erro)
    while True:
        try:
            num_imp = int(input(f"Digite a quantidade de Impostores (Recomendado = {(len(players) // 8) + 1}): "))
            if num_imp == len(players):
                print("Quantidade inválida!")
                continue
            if num_imp >= len(players) / 2:
                if filterChoice("Quantidade de impostores desbalanceada, tem certeza que quer continuar?\n[1] Sim\t\t[2] Não","1"):
                    break
                else:
                    continue
            break
        except ValueError:
            print("Digite apenas números!")
            continue

    for player in players:
        try:
            while True:
                if len(choosed_roles) == len(roles):
                    choosed_roles.pop(random.choice(range(len(choosed_roles) - 1)))
                current_role = random.choice(roles)
                if current_role not in choosed_roles:
                    choosed_roles.append(current_role)
                    players_roles[player] = current_role
                    break
        except Exception as erro:
            print(erro)

    for i in range(num_imp):
        while True:
            select = random.choice(list(players))
            if players_roles[select] != "Impostor":
                players_roles[select] = "Impostor"
                break

def seePlayers():
    player_seen = []
    seen = False
    global players, role, cene

    while len(player_seen) < len(players):
        try:
            logoScreen()
            if seen:
                print(f"O Jogador '{current_player}' já foi visualizado. Tente novamente.\n")
                seen = False
            i = 1
            for player in players:
                print(f"[{i}] {player}{' - Visto' if player in player_seen else ''}")
                i += 1
            
            num_choice = int(input("Digite o número do jogador para visualizar a função: "))

            current_player = players[num_choice - 1]
            if current_player in player_seen:
                seen = True
                continue
            else:
                player_seen.append(current_player)

            clearScreen()
            role = players_roles[players[num_choice - 1]]
            print(f"JOGADOR {current_player.upper()}")
            print(f"Local: {cene if role != 'Impostor' else '???'}, Função: {role}")
            
            clearScreen("Pressione qualquer tecla e passe para o próximo jogador.")

        except ValueError:
            input("\nDigite apenas números!")
            continue
    logoScreen()
    input("Boa partida!\n")

def doRegisterMatch():
    num_match = 1
    while True:
        matches[f"Partida {num_match} ({cene})"] = players_roles.copy()
        num_match += 1
        yield num_match

register_match = doRegisterMatch()
while True:
    try:
        logoScreen()
        opt = int(input(("""[1] Como jogar\n[2] Iniciar Partida\n[3] Sair\n\nEscolha: """)))
        match opt:
            case 1:
                howToPlay()
                input("\nPressione qualquer tecla para voltar ao menu inicial.")
            case 2:
                cene, roles = random.choice(list(cenes.items()))
                registerPlayers()
                seePlayers()
                next(register_match)
            case 3:
                break
            case _:
                input("Opção inválida. Pressione qualquer tecla para tentar novamente.")
                continue
    except ValueError:
        input("Digite apenas números. Pressione qualquer tecla para tentar novamente.")

print(matches)