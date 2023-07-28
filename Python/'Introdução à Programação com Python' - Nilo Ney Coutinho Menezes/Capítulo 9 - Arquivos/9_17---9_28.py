""" Os exercícios de 9_17 até 9_28 são apenas modificações do mesmo (programa9_6.py), sempre incrementando
o funcionamento do mesmo, portanto, para não tornar a pasta do capítulo 9 redundante, farei os exercícios
de 9_17 até 9_28 em um mesmo arquivo.
ENUNCIADO 9_17: Altere o (programa9_6.py) para exibir o tamanho da agenda no menu principal.

ENUNCIADO 9_19: Altere a função lista para que exiba também a posição de cada elemento.

ENUNCIADO 9_20: Adicione a opção de ordenar a lista por nome no menu principal.

ENUNCIADO 9_21: Nas funções de 'altera' e 'apaga', peça que o usuário confirme a alteração e exclusão
do nome antes de realizar a operação em si.

ENUNCIADO 9_22: Ao ler ou gravar uma nova lista, verifique se a agenda atual já foi gravada. Você pode usar uma
variável para controlar quando a lista foi alterada (novo, altera, apaga) e reinicializar esse valor quando ela
for lida ou gravada.

ENUNCIADO 9_23: Altere o programa para ler a última agenda lida ou gravada ao inicializar.
Dica: utilize outro arquivo para armazenar o nome.

ENUNCIADO 9_25: Altere as funções pede_nome e pede_telefone de forma a receberem um parâmetro opcional.
Caso esse parâmetro seja passado, utilize-o como retorno caso a entrada de dados seja vazia.

ENUNCIADO 9_26: Altere o programa de forma a verificar a repetição de nomes. Gere uma mensagem
de erro caso duas entradas na agenda tenham o mesmo nome.

ENUNCIADO 9_27: Modifique o programa para também controlar a data de aniversário e o e-mail de cada pessoa.

ENUNCIADO 9_28: Modifique o programa de forma a poder registrar vários telefones para a mesma pessoa.
Permita também cadastrar o tipo de telefone: celular, fixo, residencial ou trabalho.
"""
import os

agenda = []
alfabetica = False
jaExiste = False

nome_arquivo_ler = None
lido = False
salvo = True

AGENDA_HISTORICO = "agenda_historico.txt"

def limparTela():
    os.system("cls")

def pede_nome(vazio="Desconhecido"):
    while True:
        nome = input("Nome: ").replace("#", "")
        jaExiste = False
        for contato in agenda:
            if contato[0] == nome:
                jaExiste = True
                break
        if jaExiste:
            print(f"ERRO: Já existe uma pessoa com o nome '{nome}'!\nAdicione um sobrenome ou coloque outro nome.")
            continue
        break
    return nome if len(nome) > 0 else vazio

def pede_telefone(vazio="(Sem nenhum telefone)"):
    telefones = {}
    categorias = ["Celular", "Fixo", "Residencial", "Trabalho"]
    texto_input = "Digite o número de telefone ou Enter para pular: "
    while True:
        telefone = input(texto_input).replace("#", "")
        if len(telefone) > 0:
            while True:
                try:
                    print("Esse telefone é... \n[1] Celular\n[2] Fixo\n[3] Residencial\n[4] Trabalho")
                    categoria = int(input("Categoria: "))
                    if 1 <= categoria <= 4:
                        if categorias[categoria - 1] not in telefones:
                            telefones[categorias[categoria - 1]] = []
                        telefones[categorias[categoria - 1]].append(telefone)
                        break
                    else:
                        print("Categoria inválida! Digite novamente.")
                except ValueError:
                    print("Digite apenas números!")
                    continue
            texto_input = "Digite o próximo número de telefone ou Enter para pular: "
        else:
            break
    return telefones if len(telefones) > 0 else vazio

def pede_data(vazio="00/00/0000"):
    mesesComTrintaEUm = [1, 3, 5, 7, 8, 10, 12]
    while True:
        data_nascimento = input("Digite a data de nascimento: ")
        data_nascimento = data_nascimento.replace("/", "")
        if len(data_nascimento) > 5:
            diasMes = 31 if int(data_nascimento[2:4]) not in mesesComTrintaEUm else 32
            if int(data_nascimento[2:4]) == 2:
                diasMes = 29
            if int(data_nascimento[:2]) in range(1, diasMes):
                return f"{data_nascimento[:2]}/{data_nascimento[2:4]}/{data_nascimento[4:]}"
        print("Data inválida! Tentar novamente ou deixar em vazio?")
        if input("[1] Digitar novamente\t\t[2] Deixar vazio\nEscolha: ") != '1':
            return vazio
        continue    

def pede_email(vazio="(Sem e-mail)"):
    email = input("Digite o e-mail da pessoa: ")
    return email if len(email) > 0 else vazio

def mostra_dados(pessoa, ordem=None):
    print(f"{f'#{ordem} ' if ordem is not None else ''}Nome: {pessoa[0]}\tTelefone: {pessoa[1]}\tData Nasc.: {pessoa[2]}\tE-mail: {pessoa[3]}")

def pedir_nome_arquivo():
    return input("Nome do arquivo: ")

def pesquisa(nome):
    mnome = nome.lower()
    for p, e in enumerate(agenda):
        if e[0].lower() == mnome:
            return p
    return None

def novo():
    global agenda, salvo
    agenda.append([pede_nome(), pede_telefone(), pede_data(), pede_email()])
    salvo = False
    limparTela()
    print("Novo contato:")
    mostra_dados(agenda[-1])

def listar():
    ordem_agenda = agenda.copy()
    ordem_agenda.sort()
    print("\nAgenda\n\n------")
    for i, contato in enumerate(agenda if not alfabetica else ordem_agenda):
        mostra_dados(contato, i + 1)
    print("------\n")

def confirmarMod(texto):
    print(f"Você tem certeza que deseja {texto} esse contato? Essa ação é irreversível.")
    if input("[1] Sim, tenho certeza!\t\t[2] Não, deixe-me pensar...\nEscolha: ") != '1':
        return False
    return True

def apagar():
    global agenda, salvo
    p = pesquisa(input("Digite o nome da pessoa a apagar: "))
    if p is not None:
        if confirmarMod("apagar"):
            del agenda[p]
            salvo = False
        else:
            limparTela()
            print("Operação cancelada.")
    else:
        limparTela()
        print("Nome não encontrado.")

def alterar():
    global salvo
    p = pesquisa(input("Digite o nome: "))
    if p is not None:
        print("Encontrado: ")
        mostra_dados(agenda[p])
        if confirmarMod("alterar"):
            agenda[p] = [pede_nome(), pede_telefone(), pede_data(), pede_email()]
            print("Dados alterados: ", end='')
            mostra_dados(agenda[p])
            salvo = False
        else:
            limparTela()
            print("Operação cancelada.")
    else:
        limparTela()
        print("Nome não encontrado.")

def ler(nome_arquivo=None):
    global agenda, salvo, nome_arquivo_ler
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            agenda = []
            for l in arquivo.readlines():
                nome, telefone, data_nascimento, email = l.strip().split("#")
                agenda.append([nome, telefone, data_nascimento, email])
            salvo = True
        return 0
    
    except FileNotFoundError:
        return -1
    except Exception as erro:
        return -2

def gravar(nome_arquivo=None):
    global salvo, nome_arquivo_ler
    try:
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            for e in agenda:
                arquivo.write(f"{e[0]}#{e[1]}#{e[2]}#{e[3]}\n")
            salvo = True
        return 0
    except Exception as erro:
        raise erro

def handle_Arquivo(tipo):
    global nome_arquivo_ler, salvo
    match tipo:
        case "gravar":
            if nome_arquivo_ler is None:
                print("Digite o nome do arquivo para gravar: ")
                nome_arquivo_ler = pedir_nome_arquivo()
                nome_escolha = nome_arquivo_ler
            else:
                print("Digite o nome do novo arquivo de salvamento,")
                nome_escolha = input(f"ou então pressione ENTER para salvar no arquivo atual: {nome_arquivo_ler}.\n..: ")
                if len(nome_escolha) <= 0:
                    nome_escolha = nome_arquivo_ler
            gravar(nome_escolha)
            print("Arquivo gravado!")
        case "ler":
            if not salvo:
                print(f"Você ainda tem alterações não salvas na agenda atual ({nome_arquivo_ler if nome_arquivo_ler is not None else 'Não definida'}).")
                print("Deseja salvar as alterações antes de abrir outro arquivo?")
                if int(input("[1] Sim, desejo salvar\t\t[2] Não, desejo sair sem salvar\nEscolha: ")) == 1:
                    handle_Arquivo("gravar")
            while True:
                print("Agora digite o nome do arquivo que você quer ler.")
                nome_arquivo_ler = pedir_nome_arquivo()
                limparTela()
                match ler(nome_arquivo_ler):
                    case -1:
                        print(f"O arquivo {nome_arquivo_ler} não foi encontrado. Digite novamente!")
                    case -2:
                        print(f"Formato inválido para o arquivo: '{nome_arquivo_ler}'. Digite um arquivo de agenda!")
                        nome_arquivo_ler = None
                    case 0:
                        break
                continue
            atualizarHistorico()

def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return valor
        except ValueError:
            print(f"Valor inválido, favor digitar entre {inicio} e {fim}.")

def carregarHistorico():
    global nome_arquivo_ler
    try:
        with open(AGENDA_HISTORICO, "r", encoding="utf-8") as agenda_hist:
            print("Deseja inicializar com a última agenda salva/lida?")
            if input("[1] Sim\t\t[2] Não\nEscolha: ") == '1':
                nome_arquivo_ler = agenda_hist.readline()
                ler(nome_arquivo_ler)
                limparTela()
                print("Última agenda recuperada com sucesso!")
            else: 
                limparTela()
    except Exception as erro:
        print('')

def atualizarHistorico():
    try:
        with open(AGENDA_HISTORICO, "w", encoding="utf-8") as agenda_hist:
            agenda_hist.write(nome_arquivo_ler)
    except Exception as erro:
        print(erro)

def statusAgenda():
    print(f"Agenda atual: {nome_arquivo_ler if nome_arquivo_ler is not None else 'Nenhuma'}")
    print(f"Número de contatos: {len(agenda)}")
    print(f"{'Alterações nessa agenda ainda não foram salvas!' if not salvo else ''}")

def menu():
    statusAgenda()
    print(f"""
1 - Novo
2 - Alterar
3 - Apagar
4 - Listar
5 - Gravar
6 - Lêr
7 - Alternar listagem para: {'Ordem Alfabética' if not alfabetica else 'Ordem Salva'}

0 - Sair
""")
    return valida_faixa_inteiro("Escolha uma opção: ", 0, 7)

limparTela()
carregarHistorico()
while True:
    opcao = menu()
    limparTela()
    if opcao == 0:
        break
    elif opcao == 1:
        novo()
    elif opcao == 2:
        alterar()
    elif opcao == 3:
        apagar()
    elif opcao == 4:
        listar()
    elif opcao == 5:
        handle_Arquivo("gravar")
    elif opcao == 6:
        handle_Arquivo("ler")
    elif opcao == 7:
        alfabetica = not alfabetica