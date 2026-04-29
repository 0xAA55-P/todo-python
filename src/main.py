from rich import print
from utils import (
    ler_opcao,
    mostrar_menu,
)

from task_operations import (
    adicionar_tarefa,
    remover_tarefa,
    listar_tarefas,
    atualizar_tarefa,
    criar_tabela
)

OPCOES_PRINCIPAIS_VALIDAS = {0, 1, 2, 3, 4}

def main():
    criar_tabela()

    while True:
        try:
            mostrar_menu(1)
            escolha = ler_opcao()

            if escolha not in OPCOES_PRINCIPAIS_VALIDAS:
                print("\n[ERRO] Valor inválido/Fora do alcance.")
                continue

            if escolha == 0:
                print("\n[SAÍDA] Adeus!")
                break

            match escolha:
                case 1:
                    adicionar_tarefa()
                case 2:
                    remover_tarefa()
                case 3:
                    atualizar_tarefa()
                case 4:
                    listar_tarefas()

        except ValueError:
            print("\n[ERRO] Valor inválido.")

        except KeyboardInterrupt:
            print("\n[SAÍDA] Adeus!")
            break

if __name__ == "__main__":
    main()
