import menu_inicial
import arquivospim
import planos
import formas_pagamentos
from time import sleep

ARQUIVO = "socio_torcedor.txt"
SEPARADOR = " | "


def obter_senha():
    """Solicita e confirma a senha do usuário durante o cadastro"""
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
    """Recupera a senha usando ID + Nome + Sobrenome."""
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

    input("\nPressione Enter para continuar...")
    arquivospim.limpar_tela()


def cadastrar():
    print("---------- Novo Cadastro ----------")
    nome = input("Nome: ").capitalize().strip()
    sobrenome = input("Sobrenome: ").capitalize().strip()
    idade = arquivospim.obter_idade()
    if idade < 18:
        print("Assinaturas indisponiveis para sua idade!")
        sleep(3)
        menu_inicial.main()
        return
    elif idade > 120:
        op_idd = (
            input(f"Tem certezar que você possui essa idade? > {idade} anos < (S/N): ")
            .upper()
            .strip()
        )
        if op_idd == "N":
            menu_inicial.main()
            return
        elif op_idd == "S":
            pass
        else:
            print("Opção inválida! Voltando ao menu...")
            sleep(2)
            menu_inicial.main()
            return

    senha = obter_senha()

    plano_opção = input("Escolha o nº do plano: ").upper().strip()

    planos = {"1": "Bronze", "2": "Prata", "3": "Ouro", "4": "Diamante"}

    if plano_opção in planos:
        plano = planos[plano_opção]
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
        print(f"Seu ID de sócio é : {novo_id} ")
        input("\nDigite enter para continuar...")
        arquivospim.limpar_tela()
    else:
        print("Escolha incorreta!")


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
    nome = input("Digite o nome: ").capitalize().strip()
    sobrenome = input("Digite o sobrenome: ").capitalize().strip()
    idade = arquivospim.obter_idade()

    if idade < 18:
        print("Assinaturas indisponíveis para menores de idade!")
        return

    id_ = obter_id()

    if id_ in clientes:
        print(f"\nID já cadastrado! Bem-vindo de volta, {clientes[id_]['nome']}.")
        print(f"Seu plano atual é: {clientes[id_]['plano']}")
        return

    senha = obter_senha()
    planos.mostrar_planos()
    plano = obter_plano()

    novo = {
        "id": id_,
        "nome": nome,
        "sobrenome": sobrenome,
        "idade": str(idade),
        "senha": senha,
        "plano": plano,
    }
    clientes[id_] = novo
    salvar_clientes(clientes)

    print(
        f"\nParabéns, {nome} {sobrenome}! Cadastro no plano {plano} realizado com sucesso!"
    )
    print(f"===> Seu número de sócio é: {novo['id']} <===")


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
        print(
            "Opção inválida! Escolha entre 1(Bronze), 2(Prata), 3(Ouro) ou 4(Diamante)."
        )


def acessar_cadastro():
    clientes = carregar_clientes()

    print()
    buscar_id = input("Digite o ID do sócio: ").strip()

    if buscar_id not in clientes:
        print("Nenhum cadastro encontrado com esse ID.")
        return

    senha_digitada = input("Digite sua senha: ").strip()
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


def salvar_clientes(clientes):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        for c in clientes.values():
            linha = SEPARADOR.join(
                [c["id"], c["nome"], c["sobrenome"], c["idade"], c["senha"], c["plano"]]
            )
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
