"""Módulo responsável por limpar a tela"""

import os

def limpar_tela():
    """
    Limpa a tela do terminal
    Usada para melhorar a estética do programa
    """
    os.system("cls" if os.name == "nt" else "clear")
