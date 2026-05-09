"""Módulo responsável por rodar o menu principal e a função main()"""

import limpar_tela
import controlar_cadastro
import cadastrar
import planos
from time import sleep


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
    print("[5] - Esqueci a senha")
    print("[0] - Sair")


def main():
    """
    -> Função principal responsavel por rodar as demais funções do código a
    partir do primeiro input recebido após a apresentação do menu principal.
    """

    while True:
        limpar_tela.limpar_tela()
        menu()
        opcao = input("Opção: ")

        if opcao == "1":
            limpar_tela.limpar_tela()
            planos.mostrar_planos()
            limpar_tela.limpar_tela()

        elif opcao == "2":
            limpar_tela.limpar_tela()
            cadastrar.cadastrar()

        elif opcao == "3":
            limpar_tela.limpar_tela()
            cadastrar.acessar_cadastro()

        elif opcao == "4":
            limpar_tela.limpar_tela()
            controlar_cadastro.recuperar_id()

        elif opcao == "5":
            limpar_tela.limpar_tela()
            controlar_cadastro.recuperar_senha()

        elif opcao == "0":
            print("Encerrando Sistema...")
            sleep(3)
            break
        elif (
            opcao != "0"
            and opcao != "1"
            and opcao != "2"
            and opcao != "3"
            and opcao != "4"
        ):
            print("Opção incorreta!")
            sleep(2)
            limpar_tela.limpar_tela()
            continue
