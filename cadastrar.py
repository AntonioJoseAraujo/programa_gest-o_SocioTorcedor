"""Módulo responsável pelo cadastro de sócios."""

import menu_inicial
import planos
import formas_pagamentos
import limpar_tela
from cores import BOLD, BRANCO, RESET, VERMELHO, VERDE, AMARELO
import pwinput
from datetime import date, timedelta

ARQUIVO = "socio_torcedor.txt"
SEPARADOR = " | "

# ------- Senhas -------


def obter_senha():
    """
    Solicita e confirma a senha do usuário durante o cadastro
    """
    while True:
        senha = input(BRANCO + BOLD + "Crie uma senha: " + RESET).strip()
        if len(senha) < 4:
            print(VERMELHO + BOLD + "Senha muito curta! Mínimo 4 caracteres." + RESET)
            print(VERMELHO + BOLD + "-" * 48 + RESET)
            continue
        confirma_senha = input(BRANCO + BOLD + "Confirme a senha: " + RESET).strip()
        if senha == confirma_senha:
            return senha
        print(VERMELHO + BOLD + "As senhas não são iguais! Tente novamente." + RESET)
        print(VERMELHO + BOLD + "-" * 48 + RESET)


# -------------- Confirmações de informações ----------------


def confirmar_informacoes(nome: str, sobrenome: str) -> bool:
    """
    Confirma nome e o sobrenome digitado
    """
    print(VERMELHO + BOLD + "---------- Confirmação de Informações ----------" + RESET)
    print(BRANCO + BOLD + "\nConfirme suas informações:" + RESET)
    print(BRANCO + BOLD + f"Nome: {nome} {sobrenome}" + RESET)
    print()

    while True:
        confirmacao = (
            input(BRANCO + BOLD + "As informações estão corretas? (S/N): " + RESET)
            .upper()
            .strip()
        )
        if confirmacao == "S":
            print()
            return True
        elif confirmacao == "N":
            print(BRANCO + BOLD + "Vamos corrigir as informações." + RESET)
            print()
            return False  # Quebra o fluxo
        else:
            print(
                BRANCO
                + BOLD
                + "Opção inválida! Digite 'S' para Sim ou 'N' para Não."
                + RESET
            )


def alterar_informacoes() -> str:
    """
    Permite o usuário digitar novamente o nome e sobrenome caso tenha digitado
    algo incorretamente
    """
    print(VERMELHO + BOLD + "-------------- Alterar informações -------------" + RESET)

    while True:
        nome = input(BRANCO + BOLD + "Digite o nome: " + RESET).capitalize().strip()
        sobrenome = (
            input(BRANCO + BOLD + "Digite o sobrenome: " + RESET).capitalize().strip()
        )

        if nome == "" or sobrenome == "":
            print(
                VERMELHO
                + BOLD
                + "O NOME e/ou SOBRENOME não podem estar em branco!"
                + RESET
            )
            print(VERMELHO + BOLD + "-" * 48 + RESET)
            continue

        elif not nome.isalpha() or not sobrenome.isalpha():
            print(
                VERMELHO
                + BOLD
                + "O NOME e/ou SOBRENOME não podem conter números!"
                + RESET
            )
            print(VERMELHO + BOLD + "-" * 48 + RESET)
            continue

        else:
            return nome, sobrenome


def escolher_continuar():
    """
    Dá a possibilidade ao usuário de voltar ao menu principal caso tenha apertado
    a tecla 2 por engano ou continuar o cadastro caso esse seja seu objetivo
    """
    while True:
        print(BRANCO + BOLD + "[1] - CONTINUAR" + RESET)
        print(BRANCO + BOLD + "[0] - MENU PRINCIPAL" + RESET)
        escolha = input(BRANCO + BOLD + "Opção: " + RESET).strip()

        if escolha != "1" and escolha != "0":
            print(VERMELHO + BOLD + "Opção inválida!" + RESET)
            print(VERMELHO + BOLD + "-" * 48 + RESET)
            continue

        elif escolha == "0":
            limpar_tela.limpar_tela()
            menu_inicial.main()

        else:
            break


# --------- Realizar cadastro -----------
def cadastrar():
    """
    Função encarregada de realizar o cadastro dos usuários recebendo nome, sobrenome
    idade, escolha do plano e forma de pagamento do mesmo.
    """
    while True:
        nome = input(BRANCO + BOLD + "Nome: " + RESET).title().strip()
        sobrenome = input(BRANCO + BOLD + "Sobrenome: " + RESET).title().strip()

        if nome == "" or sobrenome == "":
            print(
                VERMELHO
                + BOLD
                + "O NOME e/ou SOBRENOME não podem estar em branco!"
                + RESET
            )
            print(VERMELHO + BOLD + "-" * 48 + RESET)
            continue
        if (
            not nome.replace(" ", "").isalpha()
            or not sobrenome.replace(" ", "").isalpha()
        ):
            print(
                VERMELHO
                + BOLD
                + "O NOME e/ou SOBRENOME não podem conter números!"
                + RESET
            )
            print(VERMELHO + BOLD + "-" * 48 + RESET)
            continue

        else:
            while not confirmar_informacoes(nome, sobrenome):
                nome, sobrenome = alterar_informacoes()
            break

    idade = obter_idade()
    if idade < 18 or idade > 120:
        print(VERMELHO + BOLD + "Assinaturas indisponiveis para sua idade!" + RESET)
        input("Pressione ENTER para continuar...")
        limpar_tela.limpar_tela()
        return

    senha = obter_senha()

    planos.mostrar_planos()
    print(VERMELHO + BOLD + "-" * 48 + RESET)
    plano_opcao = (
        input(BRANCO + BOLD + "Escolha o nº do plano: " + RESET).upper().strip()
    )

    while plano_opcao not in "12345" or plano_opcao == "":
        print(VERMELHO + BOLD + "Escolha incorreta" + RESET)
        print(VERMELHO + BOLD + "-" * 48 + RESET)
        plano_opcao = (
            input(BRANCO + BOLD + "Escolha o nº do plano: " + RESET).upper().strip()
        )

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
            "data_pagamento": str(date.today()),
        }
        salvar_clientes(clientes)

        print(
            BRANCO
            + BOLD
            + f"Parabéns {nome} {sobrenome} por adquirir o plano {plano}!!!"
            + RESET
        )
        print(
            VERMELHO
            + BOLD
            + "=====> "
            + RESET
            + BRANCO
            + BOLD
            + f"Seu ID de sócio é : {novo_id}"
            + RESET
            + VERMELHO
            + BOLD
            + " <====="
            + RESET
        )
        input(BRANCO + "\nPressione ENTER para continuar..." + RESET)
        limpar_tela.limpar_tela()


# --------- Funções auxiliares ----------


def obter_idade():
    """
    -> Função responsável por receber a idade como uma str, transforma-la em int
    e retorna-lá para que possa ser usada em novo_cadastro()
    """
    while True:
        idade = input(BRANCO + BOLD + "Idade: " + RESET).strip()

        if not idade.isdigit():
            print(VERMELHO + BOLD + "Digite um número válido para idade!" + RESET)
            print(VERMELHO + BOLD + "-" * 48 + RESET)
            continue

        return int(idade)


def obter_id():
    """
    Obtem e retorna o ID do usuário para que possa ser usada na função
    novo_cadastro()
    """
    while True:
        id_ = input(BRANCO + BOLD + "Digite seu ID de sócio: " + RESET).strip()
        if id_:
            return id_
        print(VERMELHO + BOLD + "ID inválido! Por favor, digite o ID correto." + RESET)


def obter_plano() -> str:
    """
    Usuario escolha o plano atráves da variavel plano
    E a opção é retornada em formato de string
    """
    opc = {"1": "Bronze", "2": "Prata", "3": "Ouro", "4": "Diamante", "5": "Social"}
    while True:
        print(VERMELHO + BOLD + "-" * 48 + RESET)
        plano = input(BRANCO + BOLD + "Escolha o nº do plano (1-5): " + RESET).strip()
        if plano in opc:
            return opc[plano]

        print(BRANCO + BOLD + "-" * 40 + RESET)
        print(VERMELHO + BOLD + "Opção inválida!" + RESET)
        print(
            BRANCO
            + BOLD
            + "Escolha entre:\n[1] - BRONZE\n[2] - PRATA\n[3] - OURO\n[4] - DIAMANTE\n[5] - SOCIAL"
            + RESET
        )


def proximo_id(clientes):
    """
    Retorna o próximo ID disponível para um novo cliente.
    """
    if not clientes:
        return "1"
    return str(max(int(c["id"]) for c in clientes.values()) + 1)


# ------- Verificação de pagamento -------


def verificar_pagamento(cliente: dict, clientes: dict) -> bool:
    """
    Verifica se a mensalidade do sócio está em dia.
    - Retorna True se o acesso pode continuar.
    - Retorna False se o sócio optou por não renovar.
    A mensalidade vence 30 dias após a data do último pagamento.
    """
    data_pagamento = date.fromisoformat(cliente["data_pagamento"])
    data_vencimento = data_pagamento + timedelta(days=30)
    hoje = date.today()
    dias_em_atraso = (hoje - data_vencimento).days

    if hoje <= data_vencimento:
        dias_restantes = (data_vencimento - hoje).days
        vencimento_fmt = data_vencimento.strftime("%d/%m/%Y")
        print(VERDE + BOLD + f"Mensalidade em dia! Vence em {dias_restantes} dia(s) ({vencimento_fmt})." + RESET)
        return True

    # Mensalidade vencida
    vencimento_fmt = data_vencimento.strftime("%d/%m/%Y")
    hoje_fmt = hoje.strftime("%d/%m/%Y")
    print(VERMELHO + BOLD + "================================================" + RESET)
    print(VERMELHO + BOLD + "       ⚠  MENSALIDADE VENCIDA  ⚠              " + RESET)
    print(VERMELHO + BOLD + "================================================" + RESET)
    print(BRANCO + BOLD + f"Vencimento : {vencimento_fmt}" + RESET)
    print(BRANCO + BOLD + f"Hoje       : {hoje_fmt}" + RESET)
    print(AMARELO + BOLD + f"Em atraso  : {dias_em_atraso} dia(s)" + RESET)
    print(VERMELHO + BOLD + "------------------------------------------------" + RESET)

    while True:
        renovar = (
            input(BRANCO + BOLD + "Deseja renovar sua mensalidade agora? (S/N): " + RESET)
            .strip()
            .upper()
        )
        if renovar == "S":
            formas_pagamentos.pagamentos()
            cliente["data_pagamento"] = str(date.today())
            clientes[cliente["id"]] = cliente
            salvar_clientes(clientes)
            print(VERDE + BOLD + "\nMensalidade renovada com sucesso!" + RESET)
            input("Pressione ENTER para continuar...")
            limpar_tela.limpar_tela()
            return True
        elif renovar == "N":
            print(BRANCO + BOLD + "\nAcesso negado. Renove sua mensalidade para continuar." + RESET)
            input("Pressione ENTER para continuar...")
            limpar_tela.limpar_tela()
            return False
        else:
            print(VERMELHO + BOLD + "Opção inválida! Digite 'S' para Sim ou 'N' para Não." + RESET)


# ------- Funções de cadastro ----------
def acessar_cadastro():
    """
    Permite que o usuario acesse o cadastro para que possa acessar algumas opções
    como simular uma venda, alterar o plano atual, realizar cancelamente e afins
    """
    clientes = carregar_clientes()

    print()
    buscar_id = input(BRANCO + BOLD + "Digite o ID do sócio: " + RESET).strip()

    if buscar_id not in clientes:
        print(BRANCO + BOLD + "Nenhum cadastro encontrado com esse ID." + RESET)
        input("Pressione ENTER para continuar...")
        limpar_tela.limpar_tela()
        return

    senha_digitada = pwinput.pwinput(
        BRANCO + BOLD + "Digite sua senha: " + RESET
    ).strip()
    if senha_digitada != clientes[buscar_id]["senha"]:
        print(BRANCO + BOLD + "Senha incorreta!" + RESET)
        input(
            BRANCO
            + BOLD
            + "\nEsqueceu sua senha? Use a opção 'Recuperar Senha' no menu."
            + RESET
        )
        return

    consulta = clientes[buscar_id]

    # Verificar se a mensalidade está em dia antes de liberar o acesso
    print(VERMELHO + BOLD + "_" * 48 + RESET)
    print(VERMELHO + BOLD + "SITUAÇÃO DA MENSALIDADE".center(48) + RESET)
    print(VERMELHO + BOLD + "_" * 48 + RESET)
    if not verificar_pagamento(consulta, clientes):
        return

    print(VERMELHO + BOLD + "_" * 48 + RESET)
    print(VERMELHO + BOLD + "DADOS DO SÓCIO".center(48) + RESET)
    print(VERMELHO + BOLD + "_" * 48 + RESET)
    print(BRANCO + BOLD + f"Nº de sócio : {consulta['id']}" + RESET)
    print(BRANCO + BOLD + f"Nome        : {consulta['nome']}" + RESET)
    print(BRANCO + BOLD + f"Sobrenome   : {consulta['sobrenome']}" + RESET)
    print(BRANCO + BOLD + f"Idade       : {consulta['idade']} anos" + RESET)
    print(BRANCO + BOLD + f"Senha       : {consulta['senha']}" + RESET)
    print(BRANCO + BOLD + f"Plano       : {consulta['plano']}" + RESET)
    print(VERMELHO + BOLD + "_" * 48 + RESET)

    print(BRANCO + BOLD + "[1] - Alterar plano" + RESET)
    print(BRANCO + BOLD + "[2] - Cancelar cadastro" + RESET)
    print(BRANCO + BOLD + "[3] - Simular venda" + RESET)
    print(BRANCO + BOLD + "[0] - Voltar" + RESET)
    acao = input(BRANCO + BOLD + "Opção: " + RESET).strip()

    if acao == "1":
        planos.mostrar_planos()
        novo_plano = obter_plano()

        if clientes[buscar_id]["plano"] == novo_plano:
            print(VERMELHO + BOLD + "-" * 40 + RESET)
            print(BRANCO + BOLD + "O plano selecionado é o mesmo do seu atual!" + RESET)
            print(VERMELHO + BOLD + "<Impossivel alterar>" + RESET)
            input("Pressione ENTER para continuar...")
            limpar_tela.limpar_tela()

        else:
            clientes[buscar_id]["plano"] = novo_plano
            salvar_clientes(clientes)
            print(
                BRANCO
                + BOLD
                + f"\nPlano alterado para {novo_plano} com sucesso!"
                + RESET
            )
            input("Pressione ENTER para continuar...")
            limpar_tela.limpar_tela()

    elif acao == "2":
        confirma = (
            input(
                BRANCO
                + BOLD
                + f"Tem certeza que deseja cancelar o cadastro de {consulta['nome']}? (s/n): "
                + RESET
            )
            .strip()
            .lower()
        )
        if confirma == "s":
            del clientes[buscar_id]
            salvar_clientes(clientes)
            print(BRANCO + BOLD + "\nCadastro cancelado com sucesso." + RESET)
            input("Pressione ENTER para continuar...")
            limpar_tela.limpar_tela()

    elif acao == "3":
        planos.mostrar_ingressos()
        escolha = (
            planos.definir_ingresso()
        )  # pode ser None caso o usuário escolha voltar para o menu principal
        print()

        if escolha is not None and escolha > 0:
            valor = planos.calcular_valor_final(escolha=escolha)
            if clientes[buscar_id]["plano"] == "Bronze":
                print(BRANCO + BOLD + "Seu plano não oferece % de desconto" + RESET)

            elif clientes[buscar_id]["plano"] == "Prata":
                print(
                    BRANCO
                    + BOLD
                    + f"Valor à ser pago: R${valor - (valor - valor * 20/100):.2f}"
                    + RESET
                )

            elif clientes[buscar_id]["plano"] == "Ouro":
                print(
                    BRANCO
                    + BOLD
                    + f"Valor à ser pago: R${valor - (valor - valor * 30/100):.2f}"
                    + RESET
                )

            elif clientes[buscar_id]["plano"] == "Diamante":
                print(
                    BRANCO
                    + BOLD
                    + f"Valor à ser pago: R${valor - (valor - valor * 50/100):.2f}"
                    + RESET
                )

            elif clientes[buscar_id]["plano"] == "Social":
                print(
                    BRANCO
                    + BOLD
                    + f"Valor à ser pago: R${valor - (valor - valor * 50/100):.2f}"
                    + RESET
                )
    elif acao == "0":
        input("\nPressione ENTER para continuar")
        limpar_tela.limpar_tela()
        return


# ------------- Manipulação de txt ---------------


def salvar_clientes(clientes):
    """
    Salva os clientes em um arquivo .txt
    """
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        for c in clientes.values():
            data_pagamento = c.get("data_pagamento", str(date.today()))
            linha = SEPARADOR.join(
                [c["id"], c["nome"], c["sobrenome"], c["idade"], c["senha"], c["plano"], data_pagamento]
            )
            f.write(linha + "\n")


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
                    partes = linha.split(SEPARADOR)
                    # Retrocompatibilidade: registros antigos sem data_pagamento
                    if len(partes) == 6:
                        id_, nome, sobrenome, idade, senha, plano = partes
                        data_pagamento = str(date.today())
                    else:
                        id_, nome, sobrenome, idade, senha, plano, data_pagamento = partes
                    clientes[id_] = {
                        "id": id_,
                        "nome": nome,
                        "sobrenome": sobrenome,
                        "idade": idade,
                        "senha": senha,
                        "plano": plano,
                        "data_pagamento": data_pagamento,
                    }
    except FileNotFoundError:
        pass
    return clientes
