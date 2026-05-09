"""Módulo responsável pelos pagamentos"""

import random
import string
from time import sleep

# --- Formas de pagamento -----------------------------------------


def pagamentos():
    """
    Dá ao usuário a opção de escolher a forma de pagamento ao selecionar um 
    plano no ato do cadastro
    """

    print("")
    pagamento = input("""Qual método de pagamento?
    1 - PIX
    2 - Cartão
    3 - Boleto
    Selecione uma das opções: """)

    while pagamento not in "123" or pagamento == "":
        print("Opção inválida!")
        print("-" * 40)
        print("")
        pagamento = input("""Qual método de pagamento?
        1 - PIX
        2 - Cartão
        3 - Boleto
        Selecione uma das opções: """)


    sleep(1)
    if pagamento == "1":
        print("Copie o código e cole no banco de sua escolha.")
        print("")
        chave_pix()

    elif pagamento == "2":
        pag_cartao()
        print("\nPagamento concluido com Sucesso !")

    elif pagamento == "3":
        print("Estamos gerando seu Boleto...")
        print()
        sleep(3)
        gera_boleto()
        print()


def pag_cartao():
    """
    Simula o pagamento do plano via cartão de crédito
    """
    while True:
        num_cartao = input("Digite os dados do seu cartão: ").strip()
        if len(num_cartao) == 16 and num_cartao.isdigit():
            break
        print("\nNúmero do cartão inválido! Digite corretamente os números.")

    while True:
        cv = input("Cód. Segurança: ").strip()
        if len(cv) == 3 and cv.isdigit():
            break
        print("\nCódigo de Segurança inválido! Digite novamente.")

    print("Processando o pagamento!")
    for i in range(1, 10):
        sleep(1)
        print(i)


def chave_pix():
    """
    Simula o pagamento do plano via pix
    """
    caracteres = string.ascii_letters + string.digits
    tamanho = 30
    pix = "".join(random.choices(caracteres, k=tamanho))
    print(pix)
    print("")


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
