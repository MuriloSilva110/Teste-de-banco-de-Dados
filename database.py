# Inportar Bliblioteca SQLITE3
import sqlite3 as sql

# Conectar ao Banco de Dados (ou criar se não existir)
def conectar_banco_dados(nome_banco):
    try:
        conexao = sql.connect(nome_banco)
        return conexao
    except sql.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None
    
# Fechar a Conexão com o Banco de Dados
def fechar_conexao(conexao):
    try:
        conexao.close()
        print("Conexão ao banco de dados fechada.")
    except sql.Error as e:
        print(f"Erro ao fechar a conexão: {e}")



# cRIAR TABELA DE EXEMPLO
def criar_tabela_exemplo(conexao):
    try:
        cursor = conexao.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS exemplo (
                id INTEGER PRIMARY KEY,
                nome TEXT NOT NULL,
                idade INTEGER NOT NULL
            )
        ''')
        conexao.commit()
        print("Tabela 'exemplo' criada com sucesso.")
   
    except sql.Error as e:
        print(f"Erro ao criar a tabela: {e}")

    finally:
        cursor.close()



# Adicionar dados a Tabela de Exemplo
def adicionar_dado_exemplo(conexao, nome, idade):
    try:
        cursor = conexao.cursor()
        cursor.execute('''
            INSERT INTO exemplo (nome, idade) VALUES (?, ?)
        ''', (nome, idade))
        conexao.commit()
        print("Dado adicionado com sucesso à tabela 'exemplo'.")
   
    except sql.Error as e:
        print(f"Erro ao adicionar dado: {e}")

    finally:
        cursor.close()


# Verificar dados na Tabela de Exemplo
def verificar_dados_exemplo(conexao):
    try:
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM exemplo')
        linhas = cursor.fetchall()
        return linhas
   
    except sql.Error as e:
        print(f"Erro ao verificar dados: {e}")

    finally:
        cursor.close()



# Atualizar dado na tabela de exmplo
def atualizar_dado_exemplo(conexao, id, novo_nome, nova_idade):
    try:
        cursor = conexao.cursor()
        cursor.execute('''
            UPDATE exemplo SET nome = ?, idade = ? WHERE id = ?
        ''', (novo_nome, nova_idade, id))
        conexao.commit()
        print("Dado atualizado com sucesso na tabela 'exemplo'.")
   
    except sql.Error as e:
        print(f"Erro ao atualizar dado: {e}")

    finally:
        cursor.close()

# Excluir dado na tabela de exemplo
def excluir_dado_exemplo(conexao, id):
    try:
        cursor = conexao.cursor()
        cursor.execute('''
            DELETE FROM exemplo WHERE id = ?
        ''', (id,))
        conexao.commit()
        print("Dado excluído com sucesso da tabela 'exemplo'.")
   
    except sql.Error as e:
        print(f"Erro ao excluir dado: {e}")

    finally:
        cursor.close()