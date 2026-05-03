"""Módulo responsável pelo cadastro de sócios."""

import menu_inicial
import arquivospim
import planos
import formas_pagamentos
from time import sleep
import pwinput

ARQUIVO = "socio_torcedor.txt"
SEPARADOR = " | "

# ------- Senhas -------


def obter_senha():
    """
    Solicita e confirma a senha do usuário durante o cadastro
    """
    while True:
        senha = input("Crie uma senha: ").strip()
        if len(senha) < 4:
            print("Senha muito curta! Mínimo 4 caracteres.")
            continue
        confirma_senha = input("Confirme a senha: ").strip()
        if senha == confirma_senha:
            return senha
        print("As senhas não são iguais! Tente novamente.")


def recuperar_senha():
    """
    Recupera a senha usando ID + Nome + Sobrenome.
    """
    print("---------- Recuperar Senha ----------")
    id_ = input("Digite seu ID de sócio: ").strip()
    nome = input("Digite seu nome: ").capitalize().strip()
    sobrenome = input("Digite seu sobrenome: ").capitalize().strip()

    clientes = carregar_clientes()

    if id_ not in clientes:
        print("ID não encontrado!")
        return

    cliente = clientes[id_]
    if cliente["nome"] == nome and cliente["sobrenome"] == sobrenome:
        print(f"\nSua senha é: {cliente['senha']}")
    else:
        print("Dados incorretos! Não foi possível recuperar a senha.")

    input("\nPressione ENTER para continuar...")
    arquivospim.limpar_tela()


# --- Confirmações de informações


def confirmar_informacoes(nome: str, sobrenome: str) -> bool:
    """
    Confirma nome e o sobrenome digitado
    """
    print("---------- Confirmação de Informações ----------")
    print("\nConfirme suas informações:")
    print(f"Nome: {nome} {sobrenome}")
    print()

    while True:
        confirmacao = input("As informações estão corretas? (S/N): ").upper().strip()
        if confirmacao == "S":
            return True
        elif confirmacao == "N":
            print("Vamos corrigir as informações.")
            return False  # Quebra o fluxo
        else:
            print("Opção inválida! Digite 'S' para Sim ou 'N' para Não.")


def alterar_informacoes() -> str:
    """
    Permite o usuário digitar novamente o nome e sobrenome caso tenha digitado
    algo incorretamente
    """
    print("---------- Alterar Informações ----------")
    nome = input("Digite o nome: ").capitalize().strip()
    sobrenome = input("Digite o sobrenome: ").capitalize().strip()
    return nome, sobrenome


def escolher_continuar():
    """
    Dá a possbilidade ao usuário de voltar ao menu principal caso tenha apertado
    a tecla 2 por engano ou continuar o cadastro caso esse seja seu objetivo
    """
    while True:
        print("---------- Novo Cadastro ----------")
        print("[1] - CONTINUAR")
        print("[0] - MENU PRINCIPAL")
        escolha = input("Opcão: ")

        if escolha != "1" and escolha != "0":
            print("Opção inválida!")
            continue

        elif escolha == "0":
            arquivospim.limpar_tela()
            menu_inicial.main()

        else:
            break


# --------- Realizar cadastro -----------
def cadastrar():
    """
    105 se nao for vazio inicia outro loop
    confirmar informacoes retorna true ou false
    while not confirmar_informacoes: se for false ele entra no loop e chama a função alterar_informacoes para corrigir os dados,
    caso seja true ele quebra o loop e segue o fluxo normal do cadastro
    é um WHILE TRUE invertido
    """
    while True:
        escolher_continuar()
        nome = input("Nome: ").title().strip()
        sobrenome = input("Sobrenome: ").title().strip()

        if nome == "" or sobrenome == "":
            print("O NOME e/ou SOBRENOME não podem estar em branco!")
            continue
        if (
            not nome.replace(" ", "").isalpha()
            or not sobrenome.replace(" ", "").isalpha()
        ):
            print("Nome e sobrenome não podem conter números!")
            continue

        else:
            while not confirmar_informacoes(nome, sobrenome):
                nome, sobrenome = alterar_informacoes()
            break

    idade = arquivospim.obter_idade()
    if idade < 18 or idade > 120:
        print("Assinaturas indisponiveis para sua idade!")
        sleep(3)
        menu_inicial.main()
        return

    senha = obter_senha()

    planos.mostrar_planos()
    plano_opcao = input("Escolha o nº do plano: ").upper().strip()

    planos_disponiveis = {
        "1": "Bronze",
        "2": "Prata",
        "3": "Ouro",
        "4": "Diamante",
        "5": "Social",
    }

    if plano_opcao in planos_disponiveis:
        plano = planos_disponiveis[plano_opcao]
        formas_pagamentos.pagamentos()
        clientes = carregar_clientes()
        novo_id = proximo_id(clientes)
        clientes[novo_id] = {
            "id": novo_id,
            "nome": nome,
            "sobrenome": sobrenome,
            "idade": str(idade),
            "senha": senha,
            "plano": plano,
        }
        salvar_clientes(clientes)

        print(f"Parabéns {nome} {sobrenome} por adquirir o plano {plano}!!!")
        print(f"=====> Seu ID de sócio é : {novo_id} <=====")
        input("\nPressione ENTER para continuar...")
        arquivospim.limpar_tela()
    else:
        print("Escolha incorreta!")


# --------- Funções auxiliares ----------
def obter_id():
    """
    Obtem e retorna o ID do usuário para que possa ser usada na função
    novo_cadastro()
    """
    while True:
        id_ = input("Digite seu ID de sócio: ").strip()
        if id_:
            return id_
        print("ID inválido! Por favor, digite o ID correto.")


def obter_plano() -> str:
    """
    Usuario escolha o plano atráves da variavel plano
    E a opção é retornada em formato de string
    """
    opc = {"1": "Bronze", "2": "Prata", "3": "Ouro", "4": "Diamante", "5": "Social"}
    while True:
        plano = input("Escolha o nº do plano (1-5): ").strip()
        if plano in opc:
            return opc[plano]
        print(
            "Opção inválida! Escolha entre 1(Bronze), 2(Prata), 3(Ouro), 4(Diamante) ou 5(Social)."
        )


# ------- Funções de cadastro ----------
def acessar_cadastro():
    """
    Permite que o usuario acesse o cadastro para que possa acessar algumas opções
    como simular uma venda, alterar o plano atual, realizar cancelamente e afins
    """
    clientes = carregar_clientes()

    print()
    buscar_id = input("Digite o ID do sócio: ").strip()

    if buscar_id not in clientes:
        print("Nenhum cadastro encontrado com esse ID.")
        return

    senha_digitada = pwinput.pwinput("Digite sua senha: ").strip()
    if senha_digitada != clientes[buscar_id]["senha"]:
        print("Senha incorreta!")
        input("\nEsqueceu sua senha? Use a opção 'Recuperar Senha' no menu.")
        return

    consulta = clientes[buscar_id]
    print("_" * 40)
    print("DADOS DO SÓCIO".center(40))
    print("_" * 40)
    print(f"Nº de sócio : {consulta['id']}")
    print(f"Nome        : {consulta['nome']}")
    print(f"Sobrenome   : {consulta['sobrenome']}")
    print(f"Idade       : {consulta['idade']} anos")
    print(f"Senha       : {consulta['senha']}")
    print(f"Plano       : {consulta['plano']}")
    print("_" * 40)

    print("[1] - Alterar plano")
    print("[2] - Cancelar cadastro")
    print("[3] - Simular venda")
    print("[0] - Voltar")
    acao = input("Opção: ").strip()

    if acao == "1":
        planos.mostrar_planos()
        novo_plano = obter_plano()
        clientes[buscar_id]["plano"] = novo_plano
        salvar_clientes(clientes)
        print(f"\nPlano alterado para {novo_plano} com sucesso!")

    elif acao == "2":
        confirma = (
            input(
                f"Tem certeza que deseja cancelar o cadastro de {consulta['nome']}? (s/n): "
            )
            .strip()
            .lower()
        )
        if confirma == "s":
            del clientes[buscar_id]
            salvar_clientes(clientes)
            print("\nCadastro cancelado com sucesso.")

    elif acao == "3":
        planos.mostrar_ingressos()
        escolha = (
            planos.definir_ingresso()
        )  # pode ser None caso o usuário escolha voltar para o menu principal
        print()

        if escolha is not None and escolha > 0:
            valor = planos.calcular_valor_final(escolha=escolha)
            if clientes[buscar_id]["plano"] == "Bronze":
                print("Seu plano não oferece % de desconto")

            elif clientes[buscar_id]["plano"] == "Prata":
                print(f"Valor à ser pago: R${valor - (valor - valor * 20/100):.2f}")

            elif clientes[buscar_id]["plano"] == "Ouro":
                print(f"Valor à ser pago: R${valor - (valor - valor * 30/100):.2f}")

            elif clientes[buscar_id]["plano"] == "Diamante":
                print(f"Valor à ser pago: R${valor - (valor - valor * 50/100):.2f}")

            elif clientes[buscar_id]["plano"] == "Social":
                print(f"Valor à ser pago: R${valor - (valor - valor * 50/100):.2f}")


def salvar_clientes(clientes):
    """
    Salva os clientes em um arquivo .txt
    """
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        for c in clientes.values():
            linha = SEPARADOR.join(
                [c["id"], c["nome"], c["sobrenome"], c["idade"], c["senha"], c["plano"]]
            )
            f.write(linha + "\n")


def proximo_id(clientes):
    """
    .
    """
    if not clientes:
        return "1"
    return str(max(int(c["id"]) for c in clientes.values()) + 1)


def carregar_clientes():
    """
    Carrega os clientes salvos no arquivo .txt
    """
    clientes = {}
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                if linha:
                    id_, nome, sobrenome, idade, senha, plano = linha.split(SEPARADOR)
                    clientes[id_] = {
                        "id": id_,
                        "nome": nome,
                        "sobrenome": sobrenome,
                        "idade": idade,
                        "senha": senha,
                        "plano": plano,
                    }
    except FileNotFoundError:
        pass
    return clientes
