# Inportar Bliblioteca SQLITE3
import sqlite3 as sql

# Conectar ao Banco de Dados (ou criar se não existir)


nome_banco_default = ("Estoque_papelaria.db")
nome_tabela_default = ("itens_estoque")

def conectar_banco_dados(nome_banco= nome_banco_default):
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
def criar_tabela_exemplo(conexao, nome_tabela=nome_tabela_default):
    try:
        cursor = conexao.cursor()
        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {nome_tabela} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_produto TEXT NOT NULL,
                preco_produto REAL NOT NULL,
                quantidade_estoque INTEGER NOT NULL,
                codigo_interno_produto TEXT NOT NULL
            )
        '''
        )
        conexao.commit()
        print(f"Tabela {nome_tabela} criada com sucesso.")
   
    except sql.Error as e:
        print(f"Erro ao criar a tabela: {e}")

    finally:
        cursor.close()



# Adicionar dados a Tabela de Exemplo
def adicionar_dado_exemplo(conexao, nome_produto, preco_produto, quantidade_estoque, codigo_interno_produto, nome_tabela = nome_tabela_default):
    try:
        with conexao:
            cursor = conexao.cursor()
            cursor.execute(f'''
                INSERT INTO {nome_tabela} (nome_produto, preco_produto, quantidade_estoque, codigo_interno_produto) VALUES (?, ?, ?, ?)
            ''', (nome_produto, preco_produto, quantidade_estoque, codigo_interno_produto))
    
            return print(f"Dado adicionado com sucesso à tabela {nome_tabela}.")
    
    except sql.Error as e:
         return print(f"Erro ao adicionar dado: {e}")

    finally:
        cursor.close()


# Verificar dados na Tabela de Exemplo
def verificar_dados_exemplo(conexao, nome_tabela=nome_tabela_default):
    try:
        with conexao:
            cursor = conexao.cursor()
            cursor.execute(f'SELECT * FROM {nome_tabela}')
            linhas = cursor.fetchall()
            return linhas
   
    except sql.Error as e:
        return print(f"Erro ao verificar dados: {e}")

    finally:
        cursor.close()



# Atualizar dado na tabela de exmplo
def atualizar_dado_exemplo(conexao, novo_nome_produto, novo_preco_produto, nova_quantidade_estoque, novo_codigo_interno_produto, nome_tabela=nome_tabela_default):
    try:
        with conexao:
            cursor = conexao.cursor()
            cursor.execute(f'''
                UPDATE {nome_tabela} SET nome_produto = ?, preco_produto = ?, quantidade_estoque = ?, codigo_interno_produto = ? WHERE id = ?
            ''', (novo_nome_produto, novo_preco_produto, nova_quantidade_estoque, novo_codigo_interno_produto, ))
            conexao.commit()
            return print(f"Dado atualizado com sucesso na tabela {nome_tabela}.")
   
    except sql.Error as e:
        print(f"Erro ao atualizar dado: {e}")

    finally:
        cursor.close()

# Excluir dado na tabela de exemplo
def excluir_dado_exemplo(conexao,id, nome_tabela=nome_tabela_default):
    try:
        with conexao:

            cursor = conexao.cursor()
            cursor.execute(f'''
                DELETE FROM {nome_tabela} WHERE id = ?
            ''', (id,))
            conexao.commit()
            print(f"Dado excluído com sucesso da tabela {nome_tabela}.")
   
    except sql.Error as e:
        print(f"Erro ao excluir dado: {e}")

    finally:
        cursor.close()



#