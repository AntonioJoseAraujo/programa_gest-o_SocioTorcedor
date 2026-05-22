"""Módulo responsável por rodar o menu principal e a função main()"""

import limpar_tela
import controlar_cadastro
import cadastrar
import planos
from time import sleep
from cores import BOLD, BRANCO, RESET, VERMELHO


def cabecalho():
    """
    -> Função responsável por comportar o print do cabeçalho o qual é chamado
    em cada tela selecionada no menu principal
    """
    print(VERMELHO + BOLD + "_" * 48 + RESET)
    print(VERMELHO + BOLD + "PROGRAMA SÓCIO TORCEDOR".center(48) + RESET)
    print(VERMELHO + BOLD + "IBIS SPORT CLUB".center(48) + RESET)
    print(VERMELHO + BOLD + "_" * 48 + RESET)


def menu():
    """
    -> Função responsável por apresentar o menu principal
    """
    cabecalho()
    print(
        VERMELHO
        + BOLD
        + "[1]"
        + RESET
        + BRANCO
        + " - Mostrar planos disponíveis"
        + RESET
    )
    print(VERMELHO + BOLD + "[2]" + RESET + BRANCO + " - Novo cadastro" + RESET)
    print(VERMELHO + BOLD + "[3]" + RESET + BRANCO + " - Acessar seu cadastro" + RESET)
    print(VERMELHO + BOLD + "[4]" + RESET + BRANCO + " - Esqueci meu ID" + RESET)
    print(VERMELHO + BOLD + "[5]" + RESET + BRANCO + " - Esqueci a senha" + RESET)
    print(VERMELHO + BOLD + "[0]" + RESET + BRANCO + " - Sair" + RESET)


def main():
    """
    -> Função principal responsável por rodar as demais funções do código a
    partir do primeiro input recebido após a apresentação do menu principal.
    """

    while True:
        menu()
        opcao = input(BRANCO + "Opção: " + RESET)

        if opcao == "1":
            limpar_tela.limpar_tela()
            cabecalho()
            planos.mostrar_planos()
            limpar_tela.limpar_tela()

        elif opcao == "2":
            limpar_tela.limpar_tela()
            cabecalho()
            print(
                VERMELHO
                + BOLD
                + "---------------- Novo cadastro -----------------"
                + RESET
            )
            cadastrar.escolher_continuar()
            cadastrar.cadastrar()

        elif opcao == "3":
            limpar_tela.limpar_tela()
            cabecalho()
            print(
                VERMELHO
                + BOLD
                + "--------------- Acessar cadastro ---------------"
                + RESET
            )
            cadastrar.escolher_continuar()
            cadastrar.acessar_cadastro()

        elif opcao == "4":
            limpar_tela.limpar_tela()
            cabecalho()
            print(
                VERMELHO
                + BOLD
                + "----------------- Recuperar ID -----------------"
                + RESET
            )
            cadastrar.escolher_continuar()
            controlar_cadastro.recuperar_id()

        elif opcao == "5":
            limpar_tela.limpar_tela()
            cabecalho()
            print(
                VERMELHO
                + BOLD
                + "---------------- Recuperar senha ---------------"
                + RESET
            )
            cadastrar.escolher_continuar()
            controlar_cadastro.recuperar_senha()

        elif opcao == "0":
            print(BRANCO + BOLD + "Encerrando Sistema..." + RESET)
            sleep(3)
            break

        else:
            print(BRANCO + BOLD + "Opção incorreta!" + RESET)
            sleep(2)
            limpar_tela.limpar_tela()
            continue
