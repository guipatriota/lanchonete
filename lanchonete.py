'''Executa software LANCHONETE em tela cheia'''
import os
import os.path
import platform


def run_script_in_new_terminal(script_name):
    """Executa um script em uma nova janela de terminal com base no sistema operacional."""
    python_path = os.path.join(".", ".conda","python.exe")
    os_type = platform.system()

    if os_type == "Windows":
        os.system(f'mode 800 && start cmd /k "{python_path} {script_name}"')
    elif os_type == "Linux":
        os.system(f'gnome-terminal --full-screen -- {python_path} {script_name}')
    elif os_type == "Darwin":  # macOS
        os.system('osascript -e \'tell application "Terminal" to activate do'+
                  f'script "{python_path} {script_name}"\'')
    else:
        print("Não foi possível executar o script em um novo "+
              f"terminal para o sistema operacional {os_type}")

# Exemplo de uso
if __name__ == "__main__":
    main_path = os.path.join(".", "src","main.py")
    run_script_in_new_terminal(main_path)
    