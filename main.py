#Implementar um sistema CRUD (Create, Read, Update, Delete) via terminal, integrado ao banco de dados SQLite. 
# O sistema deve permitir ao usuário adicionar, visualizar, atualizar e excluir itens do estoque, com cada item possuindo atributos como ID, nome, quantidade e preço.


# Impoorta Funcoes de Configuracoes_Banco_Dados.py
import database as cbd

# Menu de opcoes
def menu():
    print("\nGERENCIADOR DE ESTOQUE")
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


# Mnu simples de inicio do Gerenciador de Estoque
print("Bem-vindo ao Gerenciador de Estoque!")
print("---------------------------------------")


while True: 
    match menu():
        case 1:
            usuario_nome = input("Digite o nome do usuario a ser adicionado: ")
            usuario_idade = int(input("Digite a idade do usuario: "))
            conexao = cbd.conectar_banco_dados("meu_banco_de_dados_DE_TESTE.db")
            cbd.adicionar_dado_exemplo(conexao, usuario_nome, usuario_idade)
            
        case 2: 
            conexao = cbd.conectar_banco_dados("meu_banco_de_dados_DE_TESTE.db")
            print("---------------------------------------")
            for linha in cbd.verificar_dados_exemplo(conexao):
                print(linha)
            print("---------------------------------------")
        
        case 3:
            novo_nome = input("Digite o novo nome do usuario: ")
            nova_idade = int(input("Digite a nova idade do usuario: "))
            id_usuario = int(input("Digite o ID do usuario a ser atualizado: "))
            conexao = cbd.conectar_banco_dados("meu_banco_de_dados_DE_TESTE.db")
            cbd.atualizar_dado_exemplo(conexao, id_usuario, novo_nome, nova_idade)

        case 4:
            id_usuario = int(input("Digite o ID do usuario a ser excluído: "))
            conexao = cbd.conectar_banco_dados("meu_banco_de_dados_DE_TESTE.db")
            cbd.excluir_dado_exemplo(conexao, id_usuario)
        case 5:
            print("Saindo do Gerenciador de Estoque.")
            conexao = cbd.conectar_banco_dados("meu_banco_de_dados_DE_TESTE.db")
            cbd.fechar_conexao(conexao)
            break