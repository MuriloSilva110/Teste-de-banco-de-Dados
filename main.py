#Implementar um sistema CRUD (Create, Read, Update, Delete) via terminal, integrado ao banco de dados SQLite. 
# O sistema deve permitir ao usuário adicionar, visualizar, atualizar e excluir itens do estoque, com cada item possuindo atributos como ID, nome, quantidade e preço.


# Impoorta Funcoes de Configuracoes_Banco_Dados.py
import database as cbd

# Menu de opcoes
def menu():
    print("|1|Adicionar Item")
    print("|2|Visualizar Itens")
    print("|3|Atualizar Item")
    print("|4|Excluir Item")
    print("|5|Sair")
    # Loop para garantir que a escolha seja válida
    while True:
        try:
            escolha = int(input("Escolha uma opção: "))
            if escolha not in [ 1, 2, 3, 4, 5 ]:
                print("Opção inválida. Tente novamente.")
        except ValueError as e:
            print(f"Opção inválida. Tente novamente.")
        else:
            break
    return escolha

# conexao inicial com o banco de dados e criacao da tabela
conexao = cbd.conectar_banco_dados()
cbd.criar_tabela_exemplo(conexao)
# Mnu simples de inicio do Gerenciador de Estoque
print("---------------------------------------")

print("Bem-vindo ao Gerenciador de Estoque!")

print("---------------------------------------")


while True: 
    match menu():
        case 1:
            usuario_nome = input("Digite o nome do produto a ser adicionado: ")
            usuario_preco = float(input("Digite o preço do produto: "))
            usuario_quantidade = int(input("Digite a quantidade do produto: "))
            usuario_codigo = input("Digite o código interno do produto: ")
            conexao = cbd.conectar_banco_dados()
            cbd.adicionar_dado_exemplo(conexao, usuario_nome, usuario_preco, usuario_quantidade, usuario_codigo)
            
        case 2: 
            conexao = cbd.conectar_banco_dados()
            print("---------------------------------------")
            for linha in cbd.verificar_dados_exemplo(conexao):
                print(linha)
            print("---------------------------------------")
        
        case 3:
            novo_nome_produto = input("Digite o novo nome do produto: ")
            novo_preco_produto = float(input("Digite o novo preço do produto: "))
            nova_quantidade_estoque = int(input("Digite a nova quantidade do produto: "))
            novo_codigo_interno_produto = input("Digite o novo código interno do produto: ")
            conexao = cbd.conectar_banco_dados()
            cbd.atualizar_dado_exemplo(conexao,novo_nome_produto, novo_preco_produto, nova_quantidade_estoque, novo_codigo_interno_produto)
        case 4:
            id_produto = int(input("Digite o ID do produto a ser excluído: "))
            conexao = cbd.conectar_banco_dados()
            cbd.excluir_dado_exemplo(conexao,id=id_produto)
        case 5:
            print("Saindo do Gerenciador de Estoque.")
            conexao = cbd.conectar_banco_dados()
            cbd.fechar_conexao(conexao)
            break