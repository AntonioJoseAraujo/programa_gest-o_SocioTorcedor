import arquivospim
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
            planos.mostrar_planos()

        elif opcao == "2":
            cadastrar.cadastrar()

        elif opcao == "3":
            cadastrar.acessar_cadastro()

        elif opcao == "4":
            arquivospim.recuperar_id()

        elif opcao == "5":
            cadastrar.recuperar_senha()

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
            arquivospim.limpar_tela()
            continue
