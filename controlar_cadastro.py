"""Módulo responsável por controlar o cadastro do usuário"""

import cadastrar
import limpar_tela

def recuperar_id():
    """
    Caso o usuário esqueça o seu id de cadastro. 
    Ele pode consultar pressionando a tecla 4 no menu principal a qual vai 
    executar a função em questão permitindo a recumento através do nome e sobrenome
    """
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

def recuperar_senha():
    """
    Recupera a senha usando ID + Nome + Sobrenome.
    """
    print("---------- Recuperar Senha ----------")
    id_ = input("Digite seu ID de sócio: ").strip()
    nome = input("Digite seu nome: ").capitalize().strip()
    sobrenome = input("Digite seu sobrenome: ").capitalize().strip()

    clientes = cadastrar.carregar_clientes()

    if id_ not in clientes:
        print("ID não encontrado!")
        return

    cliente = clientes[id_]
    if cliente["nome"] == nome and cliente["sobrenome"] == sobrenome:
        print(f"\nSua senha é: {cliente['senha']}")
    else:
        print("Dados incorretos! Não foi possível recuperar a senha.")

    input("\nPressione ENTER para continuar...")
    limpar_tela.limpar_tela()
