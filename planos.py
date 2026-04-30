import arquivospim
from time import sleep


def mostrar_planos():
    """
    -> Função responsável por mostrar planos e seus benificios ao usuário
    """

    print("_" * 40)
    print("PLANOS DISPONÍVEIS".center(40))
    print("_" * 40)

    print("[1] - Bronze")
    print("Valor: R$9,90")
    print("Pré-venda nos ingressos")
    input("\nPressione Enter para continuar...\n")

    print("[2] - Prata")
    print("Valor: R$19,90")
    print("Desconto em ingresso: 20%")
    print("Pré-venda nos ingressos")
    input("\nPressione Enter para continuar...\n")

    print("[3] - Ouro")
    print("Valor: R$79,90")
    print("Desconto em ingresso: 30%")
    print("Pré-venda nos ingressos")
    print("Descontos em itens oficiais: 20%")
    input("\nPressione Enter para continuar...\n")

    print("[4] - Diamante")
    print("Valor: R$99,90")
    print("Desconto em ingresso: 50%")
    print("Pré-venda nos ingressos")
    print("Descontos em itens oficiais: 40%")
    print("Participação em sorteios do clube")
    input("\nPressione Enter para continuar...\n")


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

    print("_" * 40)
    print("INGRESSOS DISPONIVEIS".center(40))
    print("_" * 40)

    for ingresso, valor in ingressos:
        valor = f"{valor:.2f}"
        print(f"{ingresso:.<32}R${valor:>0}")
    print("[0] - MENU PRINCIPAL")


def definir_ingresso():
    while True:
        try:
            op_ingresso = int(input("Opção: "))

            if op_ingresso < 0 or op_ingresso > 11:
                print("Escolha uma opção válida!")
                continue

            elif op_ingresso == 0:
                arquivospim.limpar_tela()
                return

            return op_ingresso

        except ValueError:
            print("Digite o número correspondente ao ingresso!")


def calcular_valor_final(escolha):
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
        print(f"Valor total do ingresso R${ingresso:.2f}")
        return ingresso
