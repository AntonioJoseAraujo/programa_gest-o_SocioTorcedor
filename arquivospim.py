import random
import string
import os
from time import sleep

# 

ARQUIVO = "socio_torcedor.txt"
SEPARADOR = " | "

# --- Main() -----------------------------------------------------

def main():
    """
    -> Função principal responsavel por rodar as demais funções do código a
    partir do primeiro input recebido após a apresentação do menu principal.
    Variavel opcao: recebe o primeiro input do programa o qual deve ser um número

    if opcao == "1": caso o valor do input seja "1" os planos são apresentados na
    tela do usuario a partir da função mostrar_planos()

    elif opcao == "2": caso o valor do input seja "2" uma tela de cadastro é 
    apresentada. Esta tela pede o nome a partir de um input direto na função
    e a idade a partir da função obter_idade definida na váriavel idade
        Dentro desta estrutura condicional temos: 
        if idade <18: ela impossibilita o cadastro do futuro sócio torcedor caso
        o mesmo tenha menos de 18 anos 
    """

    while True:
        menu()
        opcao = input("Opção: ")

        if opcao == "1":
            mostrar_planos()
        
        elif opcao == "2":
            print()
            print('---------- Novo Cadastro ----------')
            nome = input("Nome: ").capitalize().strip()
            sobrenome = input("Sobrenome: ").capitalize().strip()
            idade = obter_idade()
            if idade < 18:
                print("Assinaturas indisponiveis para sua idade!")
                sleep(3)
                main()

            plano_opção = input("Escolha o nº do plano: ").upper().strip()

            planos = {"1": "Bronze", "2": "Prata", "3": "Ouro", "4": "Diamante"}

            if plano_opção in planos:
                plano = planos[plano_opção]
                pagamentos()
                clientes = carregar_clientes()
                novo_id = proximo_id(clientes)
                clientes[novo_id] = {
                    "id":    novo_id,
                    "nome":  nome,
                    "sobrenome" : sobrenome,
                    "idade": str(idade),
                    "plano": plano,
                }
                salvar_clientes(clientes)
                
                print(f"Parabéns {nome} {sobrenome} por adquirir o plano {plano}!!!")
                print(f"Seu ID de sócio é : {novo_id} ")
                sleep(7)
                limpar_tela()
            else:
                print("Escolha incorreta!")

        elif opcao == "3":
            acessar_cadastro()

        elif opcao == "4":
            recuperar_id()
            
        elif opcao == "0":
            print('Encerrando Sistema...')
            sleep(3)
            break
        elif opcao != "0" and opcao != "1" and opcao != "2" and opcao != "3" and opcao!= "4":
            print("Opção incorreta!")
            sleep(2)
            limpar_tela()
            continue
            
# --- Banco de dados ---------------------------------------------

def novo_cadastro():
    """
    => Função responsável por realizar o cadastro de novos sócios
    1 - Ela inicia com a declação da função carregar_clientes() a qual é encarregada 
    de gerar/carregar o arquivo txt e seu conteúdo.
    2 - Variavel nome: é um input direto do nome da pessoa o qual já é tratado para
    que as primeiras letras fiquem maiúsculas e espaços vazios sejam eliminados
    3 - Variável idade: ela recebe a idade através da declação da função obter_idade.
    4 - if < 18: verifica o retorno da variável idade, caso a pessoa tenha menos 
    que 18 anos de idade a possibilidade de cadastro é bloqueada
    5 - if id_ in clientes
    """
    clientes = carregar_clientes()

    print()
    nome  = input("Digite o nome: ").capitalize().strip()
    sobrenome = input("Digite o sobrenome: ").capitalize().strip()
    idade = obter_idade()

    if idade < 18:
        print("Assinaturas indisponíveis para menores de idade!")
        return

    id_ = obter_id()

    if id_ in clientes:
        print(f"\nID já cadastrado! Bem-vindo de volta, {clientes[id_]['nome']}.")
        print(f"Seu plano atual é: {clientes[id_]['plano']}")
        return

    mostrar_planos()
    plano = obter_plano()

    novo = {
        "id":    id_,
        "nome":  nome,
        "sobrenome" : sobrenome,
        "idade": str(idade),
        "plano": plano,
    }
    clientes[id_] = novo
    salvar_clientes(clientes)

    print(f"\nParabéns, {nome} {sobrenome}! Cadastro no plano {plano} realizado com sucesso!")
    print(f"Seu número de sócio é: {novo['id']}")


def obter_id():
    while True:
        id_ = input("Digite seu ID de sócio: ").strip()
        if id_:
            return id_
        print("ID inválido! Por favor, digite o ID correto.")

def obter_plano():
    opc = {"1": "Bronze", "2": "Prata", "3": "Ouro", "4": "Diamante"}
    while True:
        plano = input("Escolha o nº do plano (1-4): ").strip()
        if plano in opc:
            return opc[plano]
        print("Opção inválida! Escolha entre 1(Bronze), 2(Prata), 3(Ouro) ou 4(Diamante).")

def acessar_cadastro():
    clientes = carregar_clientes()

    print()
    buscar_id = input('Digite o ID do sócio: ').strip()

    if buscar_id not in clientes:
        print("Nenhum cadastro encontrado com esse ID.")
        return

    consulta = clientes[buscar_id]
    print("_" * 40)
    print("DADOS DO SÓCIO".center(40))
    print("_" * 40)
    print(f"Nº de sócio : {consulta['id']}")
    print(f"Nome        : {consulta['nome']}")
    print(f"Sobrenome   : {consulta['sobrenome']}")
    print(f"Idade       : {consulta['idade']} anos")
    print(f"Plano       : {consulta['plano']}")
    print("_" * 40)

    print("[1] - Alterar plano")
    print("[2] - Cancelar cadastro")
    print("[3] - Simular venda")
    print("[0] - Voltar")
    acao = input("Opção: ").strip()

    if acao == "1":
        mostrar_planos()
        novo_plano = obter_plano()
        clientes[buscar_id]["plano"] = novo_plano
        salvar_clientes(clientes)
        print(f"\nPlano alterado para {novo_plano} com sucesso!")

    elif acao == "2":
        confirma = input(f"Tem certeza que deseja cancelar o cadastro de {consulta['nome']}? (s/n): ").strip().lower()
        if confirma == "s":
            del clientes[buscar_id]
            salvar_clientes(clientes)
            print("\nCadastro cancelado com sucesso.")

    elif acao == "3":
        mostrar_ingressos()
        escolha = definir_ingresso() #pode ser None caso o usuário escolha voltar para o menu principal
        print()

        if escolha is not None and escolha > 0:
            valor = calcular_valor_final(escolha=escolha)
            if clientes[buscar_id]["plano"] == "Bronze":
                print("Seu plano não oferece % de desconto")
            
            elif clientes[buscar_id]["plano"] == "Prata":
                print(f"Valor à ser pago: R${valor - (valor - valor * 20/100):.2f}")

            elif clientes[buscar_id]["plano"] == "Ouro":
                print(f"Valor à ser pago: R${valor - (valor - valor * 30/100):.2f}")

            elif clientes[buscar_id]["plano"] == "Diamante":
                print(f"Valor à ser pago: R${valor - (valor - valor * 50/100):.2f}")
        
       

def salvar_clientes(clientes):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        for c in clientes.values():
            linha = SEPARADOR.join([c["id"], c["nome"], c["sobrenome"], c["idade"], c["plano"]])
            f.write(linha + "\n")

def proximo_id(clientes):
    if not clientes:
        return "1"
    return str(max(int(c["id"]) for c in clientes.values()) + 1)

def carregar_clientes():
    clientes = {}
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                if linha:
                    id_,nome,sobrenome,idade,plano = linha.split(SEPARADOR)
                    clientes[id_] = {
                        "id":    id_,
                        "nome":  nome,
                        "sobrenome" : sobrenome,
                        "idade": idade,
                        "plano": plano,
                    }
    except FileNotFoundError:
        pass
    return clientes

# --- Menu Principal ----------------------------------------------

def menu():
    """
    -> Função responsável por apresentar o menu principal
    """
    print("_" * 40)
    print("PROGRAMA SÓCIO TORCEDOR".center(40))
    print("IBIS SPORT CLUB".center(40))
    print("_" * 40)
    print("[1] - Mostrar planos disponiveis")
    print("[2] - Novo cadastro")
    print("[3] - Acessar seu cadastro")
    print("[4] - Esqueci meu ID")
    print("[0] - Sair")

def mostrar_planos():
    """
    -> Função responsável por mostrar planos e seus benificios ao usuário
    """
    print("_" * 40)
    print("PLANOS DISPONÍVEIS".center(40))
    print("_" * 40)

    print("[1] - Bronze")
    print("Valor: R$9,90")
    print("Pré-venda nos ingressos")
    print()
    sleep(2)

    print("[2] - Prata")
    print("Valor: R$19,90")
    print("Desconto em ingresso: 20%")
    print("Pré-venda nos ingressos")
    print()
    sleep(2)

    print("[3] - Ouro")
    print("Valor: R$79,90")
    print("Desconto em ingresso: 30%")
    print("Pré-venda nos ingressos")
    print("Descontos em itens oficiais: 20%")
    print()
    sleep(2)

    print("[4] - Diamante")
    print("Valor: R$99,90")
    print("Desconto em ingresso: 50%")
    print("Pré-venda nos ingressos")
    print("Descontos em itens oficiais: 40%")
    print("Participação em sorteios do clube")
    print()
    sleep(2)

def mostrar_ingressos():
    """
    => Função responsável para mostrar as opções de ingressos que podem ser
    adiquiros pelo torcedor.
    Não retorna nada, apenas apresenta as informações na tela
    """
    ingressos = [("[1] - NORTE", 80.00),
             ("[2] - SUL", 130.00),
             ("[3] - LESTE SUPERIOR CORNER",115.00),
             ("[4] - LESTE SUPERIOR LATERAL", 125.00),
             ("[5] - LESTE SUPERIOR CENTRAL", 140.00),
             ("[6] - LESTE INFERIOR CORNER", 140.00),
             ("[7] - LESTE INFERIOR CENTRAL", 190.00),
             ("[8] - LESTE INFERIOR CENTRAL", 190.00),
             ("[9] - OESTE INFERIOR", 200.00),
             ("[10] - OESTE INFERIOR CENTRAL", 250.00),
             ("[11] - OESTE INFERIOR LATERAL", 290.00),]

    print("_" * 40)
    print("INGRESSOS DISPONIVEIS".center(40))
    print("_" * 40)

    for ingresso, valor in ingressos:
        valor = f"{valor:.2f}"
        print(f"{ingresso:.<32}R${valor:>0}")
    print("[0] - MENU PRINCIPAL")


def obter_idade():
    """
    -> Função responsável por receber a idade como uma str, transforma-la em int
    e retorna-lá para que possa ser usada em novo_cadastro()
    """
    while True:
        idade = input("Idade: ")

        try: 
            idade = int(idade)
            return idade
        except ValueError:
            print("Digite um número válido para idade!")

def definir_ingresso():
    while True:
        try:
            op_ingresso = int(input("Opção: "))

            if op_ingresso < 0 or op_ingresso > 11:
                print("Escolha uma opção válida!")
                continue

            elif op_ingresso == 0:
                limpar_tela()
                return
                
            return op_ingresso

        except ValueError:
            print("Digite o número correspondente ao ingresso!")

def calcular_valor_final(escolha):
    ingressos = [("[1] - NORTE", 80.00),
             ("[2] - SUL", 130.00),
             ("[3] - LESTE SUPERIOR CORNER",115.00),
             ("[4] - LESTE SUPERIOR LATERAL", 125.00),
             ("[5] - LESTE SUPERIOR CENTRAL", 140.00),
             ("[6] - LESTE INFERIOR CORNER", 140.00),
             ("[7] - LESTE INFERIOR CENTRAL", 190.00),
             ("[8] - LESTE INFERIOR CENTRAL", 190.00),
             ("[9] - OESTE INFERIOR", 200.00),
             ("[10] - OESTE INFERIOR CENTRAL", 250.00),
             ("[11] - OESTE INFERIOR LATERAL", 290.00),]
    
    if escolha == 0:
        return
    else:
        ingresso = ingressos[escolha - 1][1]
        print(f"Valor total do ingresso R${ingresso:.2f}")
        return ingresso

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def recuperar_id():
    clientes = carregar_clientes()
    print()
    print("---------- Recuperar ID de sócio ----------")
    buscar_nome = input("Digite seu nome: ").strip().capitalize()
    buscar_sobrenome = input("Digite seu sobrenome: ").strip().capitalize()
    print()
    
    for cliente in clientes.values():
        if cliente['nome'] == buscar_nome and cliente['sobrenome'] == buscar_sobrenome:
            cliente_encontrado = cliente
            print(f'Seu ID de sócio é: #{cliente_encontrado['id']}')
            break
    else:       
        print("Cadastro não encontrado!")


# --- Formas de pagamento -----------------------------------------

def pagamentos():    
    print('')
    pagamento = input('''Qual método de pagamento?
    1 - PIX
    2 - Cartão
    3 - Boleto
    Selecione uma das opções: ''')
    sleep(1)
    if pagamento == '1':
        print('Copie o código e cole no banco de sua escolha.')
        print('')
        chave_pix()
    elif pagamento == '2':
        pag_cartao()
        print('\nPagamento concluido com Sucesso !')
    elif pagamento == '3':
        print('Estamos gerando seu Boleto...')
        print()
        sleep(3)
        gera_boleto()
        print()

def pag_cartao():
    while True:
        num_cartao =input('Digite os dados do seu cartão: ').strip()
        if len(num_cartao) == 16 and num_cartao.isdigit():
            break
        print("\nNúmero do cartão inválido! Digite corretamente os números.")

    while True:
        cv = input('Cód. Segurança: ').strip()
        if len(cv) == 3 and cv.isdigit():
            break
        print("\nCódigo de Segurança inválido! Digite novamente.")

    print('Processando o pagamento!')
    for i in range(1,10):
        sleep(1)
        print(i)

def chave_pix():
    caracteres = string.ascii_letters + string.digits
    tamanho = 30
    pix = ''.join(random.choices(caracteres, k=tamanho))
    print(pix)
    print('')

def gera_boleto():
    for _ in range (30): #_ usado no lugar de i para indicar que a variável não será utilizada
        print(random.randint(1,99), end='')
    print('')
    sleep(5)
