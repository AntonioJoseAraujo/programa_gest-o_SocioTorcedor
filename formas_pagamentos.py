"""Módulo responsável pelos pagamentos"""

import random
import string
from time import sleep
from cores import AZUL, BOLD, BRANCO, RESET, VERDE, VERMELHO

# --- Formas de pagamento -----------------------------------------


def pagamentos():
    """
    Dá ao usuário a opção de escolher a forma de pagamento ao selecionar um
    plano no ato do cadastro
    """

    print(BRANCO + BOLD + "" + RESET)
    pagamento = input(BRANCO + BOLD + """Qual método de pagamento?
    1 - PIX
    2 - Cartão
    3 - Boleto
    Selecione uma das opções: """ + RESET)

    while pagamento not in "123" or pagamento == "":
        print(VERMELHO + BOLD + "Opção inválida!" + RESET)
        print("-" * 40)
        print("")
        pagamento = input(BRANCO + BOLD + """Qual método de pagamento?
        1 - PIX
        2 - Cartão
        3 - Boleto
        Selecione uma das opções: """ + RESET)

    sleep(1)
    if pagamento == "1":
        print(BRANCO + BOLD + "Copie o código e cole no banco de sua escolha." + RESET)
        print("")
        chave_pix()

    elif pagamento == "2":
        pag_cartao()
        print(VERDE + BOLD + "\nPagamento concluido com Sucesso !" + RESET)

    elif pagamento == "3":
        print(BRANCO + BOLD + "Estamos gerando seu Boleto..." + RESET)
        print()
        sleep(3)
        gera_boleto()
        print()


def pag_cartao():
    """
    Simula o pagamento do plano via cartão de crédito
    """
    while True:
        num_cartao = input(
            BRANCO + BOLD + "Digite os dados do seu cartão: " + RESET
        ).strip()
        if len(num_cartao) == 16 and num_cartao.isdigit():
            break
        print(
            VERMELHO
            + BOLD
            + "\nNúmero do cartão inválido! Digite corretamente os números."
            + RESET
        )
        print(VERMELHO + BOLD + "-" * 48 + RESET)

    while True:
        cv = input(BRANCO + BOLD + "Cód. Segurança: " + RESET).strip()
        if len(cv) == 3 and cv.isdigit():
            break
        print(
            VERMELHO
            + BOLD
            + "\nCódigo de Segurança inválido! Digite novamente."
            + RESET
        )
        print(VERMELHO + BOLD + "-" * 48 + RESET)

    print(BRANCO + BOLD + "\nProcessando o pagamento!" + RESET)
    for i in range(1, 10):
        sleep(0.75)
        print(AZUL + BOLD + str(i) + RESET, end=" ")


def chave_pix():
    """
    Simula o pagamento do plano via pix
    """
    caracteres = string.ascii_letters + string.digits
    tamanho = 30
    pix = "".join(random.choices(caracteres, k=tamanho))
    print(BRANCO + BOLD + pix + RESET)
    print(BRANCO + BOLD + "" + RESET)


def gera_boleto():
    """
    Simula o pagamento do plano via boleto
    """
    for _ in range(
        30
    ):  # _ usado no lugar de i para indicar que a variável não será utilizada
        print(random.randint(1, 99), end="")
    print("")
    sleep(5)
