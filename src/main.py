'''
Software Lanchonete para gestão de clientes e vendas de um 
estabelecimento comercial do tipo lanchonete (ERP).
'''
import time
import pyautogui
from menu import Menu
from funcoes_apoio import clear, show_welcome_screen, animacao_de_saida, set_terminal_size


if __name__ == "__main__":
    pyautogui.hotkey('alt', 'enter')
    clear()
    set_terminal_size()
    clear()
    show_welcome_screen()
    menu = Menu()
    time.sleep(3)
    clear()
    menu.exibir_menu()
    clear()
    animacao_de_saida()
    pyautogui.hotkey('alt', 'enter')
