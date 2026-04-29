from rich import print
import sqlite3

def ler_nome():
    # caso não digite nada, nome = "Sem nome"
    return input("Nome da tarefa: ").strip() or "Sem nome"

def ler_status():
    # caso nao digite nada, status = "TODO"
    return input("Status (TODO/IN_PROGRESS/DONE): ").strip().upper() or "TODO"

def ler_id():
    while True:
        try:
            return int(input("ID Da tarefa: "))
        except ValueError:
            print("\nID Invalido.")

def ler_opcao():
    return int(input("Digite o numero da opção: "))
    
# menu_a_exibir:
# 1. Principal
# 2. O que alterar na tarefa (nome, status)
def mostrar_menu(menu_a_exibir):
    opcoes_principais = [
        "\n0. Sair",
        "1. Adicionar Tarefa",
        "2. Remover Tarefa",
        "3. Editar Tarefa",
        "4. Mostrar Tarefas\n"
    ]

    opcoes_alterar = [
        "\n1. Alterar nome",
        "2. Alterar status\n"
    ]

    match menu_a_exibir:
        case 1:
            for opcao in opcoes_principais:
                print(opcao)

        case 2:
            for opcao in opcoes_alterar:
                print(opcao)        
