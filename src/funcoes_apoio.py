'''
funcoes_apoio.py

Este módulo contém diversas funções auxiliares usadas ao longo do projeto.

Funções disponíveis:
- animacao_de_saida: Exibe uma animação de contagem regressiva ao encerrar o programa.

Exemplo de uso:
>>> from funcoes_apoio import animacao_de_saida
>>> animacao_de_saida()
'''
import time
from os import getenv, system, name
import platform
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

ROWS_TERMINAL_SIZE = getenv("ROWS_TERMINAL_SIZE")
COLUMNS_TERMINAL_SIZE = getenv("COLUMNS_TERMINAL_SIZE")

def set_terminal_size(rows=ROWS_TERMINAL_SIZE, columns=COLUMNS_TERMINAL_SIZE):
    """Altera o tamanho do terminal com base no sistema operacional."""
    print("Atenção! Este software é melhor visualizado em tela cheia",
          f"ou no mínimo {rows} linhas por {columns} colunas.\n")
    print("Caso queira retornar à tela normal, pressione CTRL+ALT.")
    input("Pressione enter para iniciar")

def animacao_de_saida():
    '''
    Exibe uma animação de contagem regressiva quando o programa está prestes a
    ser encerrado.

    Esta função imprime uma contagem regressiva de 3 para 1 e em seguida exibe
    a mensagem "Programa encerrado".
    Utiliza a biblioteca time para criar um intervalo de 1 segundo entre cada
    número da contagem.
    '''
    print("Encerrando o programa em:")

    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)

    print("Programa encerrado.")

def show_welcome_screen(logo_file="img/logo.txt", name_file="img/nome_ascii_art.txt"):
    """
    Exibe a tela inicial do aplicativo, mostrando o logo e o nome do aplicativo em ASCII Art.
    """
    # Lê o arquivo contendo o logo e imprime seu conteúdo
    try:
        with open(logo_file, 'r', encoding='utf-8') as file:
            print("\033[93m" + file.read() + "\033[0m")  # Amarelo
    except FileNotFoundError:
        print("Arquivo de logo não encontrado.")

    print("\n")  # Adiciona uma linha em branco entre o logo e o nome

    # Lê o arquivo contendo o nome do aplicativo em ASCII Art e imprime seu conteúdo
    try:
        with open(name_file, 'r', encoding='utf-8') as file:
            print("\033[93m" + file.read() + "\033[0m")  # Amarelo
    except FileNotFoundError:
        print("Arquivo de nome em ASCII Art não encontrado.")

def close_terminal():
    """Fecha a janela do terminal com base no sistema operacional."""
    
    os_type = platform.system()
    
    if os_type == "Windows":
        system('exit')
    elif os_type == "Linux" or os_type == "Darwin":
        system('kill -9 $$')
    else:
        print(f"Não foi possível fechar o terminal para o sistema operacional {os_type}")

def clear():
    '''Limpar a tela'''
    # para Windows
    if name == 'nt':
        _ = system('cls')

    # Para Mac e Linux
    else:
        _ = system('clear')

# Exemplo de uso
if __name__ == "__main__":
    show_welcome_screen()
