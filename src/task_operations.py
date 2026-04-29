from rich import print
from utils import (
    ler_nome,
    ler_status,
    ler_id,
    mostrar_menu
)

import sqlite3

NOME_BANCO = "../database/tarefas.db"
OPCOES_ALTERAR_VALIDAS = {1, 2}

def criar_tabela():
    with sqlite3.connect(NOME_BANCO) as conexao:
        cursor = conexao.cursor()

        # status como TODO por padrão
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tarefas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                status TEXT DEFAULT 'TODO'
            )
        """)

# manipulação de tarefas
def adicionar_tarefa():
    nome = ler_nome()
    status = ler_status()

    with sqlite3.connect(NOME_BANCO) as conexao:
        cursor = conexao.cursor()

        cursor.execute("""
            INSERT OR IGNORE INTO tarefas (nome, status)
            VALUES(?, ?)
        """, (nome, status))

def remover_tarefa():
    listar_tarefas()

    id = ler_id()

    with sqlite3.connect(NOME_BANCO) as conexao:
        cursor = conexao.cursor()

        cursor.execute("""
            DELETE FROM tarefas
            WHERE id = ?
        """, (id,))

def atualizar_tarefa():
    listar_tarefas()
    mostrar_menu(2)

    while True:
        escolha = ler_opcao()

        if escolha not in OPCOES_ALTERAR_VALIDAS:
            print("\nValor inválido/Fora de alcance.")
            continue
        else:
            break

    id_para_atualizar = ler_id()

    match escolha:
        case 1:
            novo_nome = ler_nome()
    
            with sqlite3.connect(NOME_BANCO) as conexao:
                cursor = conexao.cursor()

                cursor.execute("""
                    UPDATE tarefas
                    SET nome = ?
                    WHERE id = ?
                """, (novo_nome, id_para_atualizar))

        case 2:
            novo_status = ler_status()

            with sqlite3.connect(NOME_BANCO) as conexao:
                cursor = conexao.cursor()

                cursor.execute("""
                    UPDATE tarefas
                    SET status = ?
                    WHERE id = ?
                """, (novo_status, id_para_atualizar))
    
def listar_tarefas():
    with sqlite3.connect(NOME_BANCO) as conexao:
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM tarefas")
        for line in cursor.fetchall():
            print(f"ID: {line[0]} | Nome: {line[1]} | Status: {line[2]}")
