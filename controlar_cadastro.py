"""Módulo responsável por controlar o cadastro do usuário"""

import cadastrar
import limpar_tela
from cores import BOLD, BRANCO, RESET, VERMELHO


def recuperar_id():
    """
    Caso o usuário esqueça o seu id de cadastro.
    Ele pode consultar pressionando a tecla 4 no menu principal a qual vai
    executar a função em questão permitindo a recumento através do nome e sobrenome
    """
    clientes = cadastrar.carregar_clientes()
    print()
    print(VERMELHO + BOLD + "------------- Recuperar ID de sócio ------------" + RESET)
    buscar_nome = (
        input(BRANCO + BOLD + "Digite seu nome: " + RESET).strip().capitalize()
    )
    buscar_sobrenome = (
        input(BRANCO + BOLD + "Digite seu sobrenome: " + RESET).strip().capitalize()
    )
    print()

    for cliente in clientes.values():
        if cliente["nome"] == buscar_nome and cliente["sobrenome"] == buscar_sobrenome:
            cliente_encontrado = cliente
            print(
                BRANCO
                + BOLD
                + f"Seu ID de sócio é: #{cliente_encontrado['id']}"
                + RESET
            )
            input("Pressione ENTER para continuar...")
            limpar_tela.limpar_tela()
            break
    else:
        print(VERMELHO + BOLD + "Cadastro não encontrado!" + RESET)
        input("Pressione ENTER para continuar...")
        limpar_tela.limpar_tela()


def recuperar_senha():
    """
    Recupera a senha usando ID + Nome + Sobrenome.
    """
    print(VERMELHO + BOLD + "------------------------------------------------" + RESET)
    id_ = input(BRANCO + BOLD + "Digite seu ID de sócio: " + RESET).strip()
    nome = input(BRANCO + BOLD + "Digite seu nome: " + RESET).capitalize().strip()
    sobrenome = (
        input(BRANCO + BOLD + "Digite seu sobrenome: " + RESET).capitalize().strip()
    )

    clientes = cadastrar.carregar_clientes()

    if id_ not in clientes:
        print(VERMELHO + BOLD + "ID não encontrado!" + RESET)
        input("Pressione ENTER para continuar...")
        limpar_tela.limpar_tela()
        return

    cliente = clientes[id_]
    if cliente["nome"] == nome and cliente["sobrenome"] == sobrenome:
        print(BRANCO + BOLD + f"\nSua senha é: {cliente['senha']}" + RESET)
    else:
        print(
            VERMELHO
            + BOLD
            + "Dados incorretos! Não foi possível recuperar a senha."
            + RESET
        )

    input("\nPressione ENTER para continuar...")
    limpar_tela.limpar_tela()
