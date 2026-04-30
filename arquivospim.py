import os
import cadastrar


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


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def recuperar_id():
    clientes = cadastrar.carregar_clientes()
    print()
    print("---------- Recuperar ID de sócio ----------")
    buscar_nome = input("Digite seu nome: ").strip().capitalize()
    buscar_sobrenome = input("Digite seu sobrenome: ").strip().capitalize()
    print()

    for cliente in clientes.values():
        if cliente["nome"] == buscar_nome and cliente["sobrenome"] == buscar_sobrenome:
            cliente_encontrado = cliente
            print(f"Seu ID de sócio é: #{cliente_encontrado['id']}")
            break
    else:
        print("Cadastro não encontrado!")
