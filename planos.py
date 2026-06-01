"""Módulo responsável por apresentar planos e ingressos"""

import limpar_tela
from cores import BOLD, BRANCO, RESET, VERMELHO

def mostrar_planos():
    """
    -> Função responsável por mostrar planos e seus benificios ao usuário
    """

    print(VERMELHO + BOLD + '-------------- Planos disponiveis --------------'+ RESET)

    print(VERMELHO + BOLD + "[1] - Bronze" + RESET)
    print(BRANCO + BOLD + "Valor: R$9,90" + RESET)
    print(BRANCO + BOLD + "Pré-venda nos ingressos" + RESET)
    input("Pressione ENTER para continuar...")

    print()
    print(VERMELHO + BOLD + "[2] - Prata" + RESET)
    print(BRANCO + BOLD + "Valor: R$19,90" + RESET)
    print(BRANCO + BOLD + "Desconto em ingresso: 20%" + RESET)
    print(BRANCO + BOLD + "Pré-venda nos ingressos" + RESET)
    input("Pressione ENTER para continuar...")

    print()
    print(VERMELHO + BOLD + "[3] - Ouro" + RESET)
    print(BRANCO + BOLD + "Valor: R$79,90" + RESET)
    print(BRANCO + BOLD + "Desconto em ingresso: 30%" + RESET)
    print(BRANCO + BOLD + "Pré-venda nos ingressos" + RESET)
    print(BRANCO + BOLD + "Descontos em itens oficiais: 20%" + RESET)
    input("Pressione ENTER para continuar...")

    print()
    print(VERMELHO + BOLD + "[4] - Diamante" + RESET)
    print(BRANCO + BOLD + "Valor: R$99,90" + RESET)
    print(BRANCO + BOLD + "Desconto em ingresso: 50%" + RESET)
    print(BRANCO + BOLD + "Pré-venda nos ingressos" + RESET)
    print(BRANCO + BOLD + "Descontos em itens oficiais: 40%" + RESET)
    print(BRANCO + BOLD + "Participação em sorteios do clube" + RESET)
    input("Pressione ENTER para continuar...")

    print()
    print(VERMELHO + BOLD + "[5] - Social(PCD)" + RESET)
    print(BRANCO + BOLD + "Valor: R$9,99" + RESET)
    print(BRANCO + BOLD + "Desconto em ingresso: 50%" + RESET)
    print(BRANCO + BOLD + "Pré-venda nos ingressos" + RESET)
    input("Pressione ENTER para continuar...")

def mostrar_ingressos():
    """
    => Função responsável para mostrar as opções de ingressos que podem ser
    adiquiros pelo torcedor.
    Não retorna nada, apenas apresenta as informações na tela
    """
    ingressos = [
        ("[1] - NORTE", 80.00),
        ("[2] - SUL", 130.00),
        ("[3] - LESTE SUPERIOR CORNER", 115.00),
        ("[4] - LESTE SUPERIOR LATERAL", 125.00),
        ("[5] - LESTE SUPERIOR CENTRAL", 140.00),
        ("[6] - LESTE INFERIOR CORNER", 140.00),
        ("[7] - LESTE INFERIOR CENTRAL", 190.00),
        ("[8] - LESTE INFERIOR CENTRAL", 190.00),
        ("[9] - OESTE INFERIOR", 200.00),
        ("[10] - OESTE INFERIOR CENTRAL", 250.00),
        ("[11] - OESTE INFERIOR LATERAL", 290.00),
    ]

    print(VERMELHO + BOLD + "_" * 48 + RESET)
    print(VERMELHO + BOLD + "INGRESSOS DISPONIVEIS".center(48) + RESET)
    print(VERMELHO + BOLD + "_" * 48 + RESET)

    for ingresso, valor in ingressos:
        valor = f"{valor:.2f}"
        print(BRANCO + BOLD + f"{ingresso:.<32}R${valor:>0}" + RESET)
    print(VERMELHO + BOLD + "[0] - MENU PRINCIPAL" + RESET)


def definir_ingresso():
    """
    Possbilita a escolha do ingresso por parte do usuario após a apresentação
    dos mesmo na tela
    """
    while True:
        try:
            op_ingresso = int(input("Opção: "))

            if op_ingresso < 0 or op_ingresso > 11:
                print(BRANCO + BOLD + "-" * 48 + RESET)
                print(VERMELHO + BOLD + "Escolha uma opção válida!" + RESET)
                continue

            elif op_ingresso == 0:
                limpar_tela.limpar_tela()
                return

            return op_ingresso

        except ValueError:
            print(BRANCO + BOLD + "-" * 48 + RESET)
            print(VERMELHO + BOLD + "Digite o número correspondente ao ingresso!" + RESET)


def calcular_valor_final(escolha):
    """
    Mostra o valor original do ingresso e o valor com desconto com base no
    plano do usuário
    """
    ingressos = [
        ("[1] - NORTE", 80.00),
        ("[2] - SUL", 130.00),
        ("[3] - LESTE SUPERIOR CORNER", 115.00),
        ("[4] - LESTE SUPERIOR LATERAL", 125.00),
        ("[5] - LESTE SUPERIOR CENTRAL", 140.00),
        ("[6] - LESTE INFERIOR CORNER", 140.00),
        ("[7] - LESTE INFERIOR CENTRAL", 190.00),
        ("[8] - LESTE INFERIOR CENTRAL", 190.00),
        ("[9] - OESTE INFERIOR", 200.00),
        ("[10] - OESTE INFERIOR CENTRAL", 250.00),
        ("[11] - OESTE INFERIOR LATERAL", 290.00),
    ]

    if escolha == 0:
        return
    else:
        ingresso = ingressos[escolha - 1][1]
        print(BRANCO + BOLD + f"Valor total do ingresso R${ingresso:.2f}" + RESET)
        return ingresso
