# 📦 Gerenciador de Estoque de Papelaria (CRUD CLI)

Este é um projeto simples, desenvolvido em Python, que simula um sistema de **Gerenciamento de Estoque** via interface de linha de comando (CLI). Utiliza o banco de dados **SQLite** para persistir os dados do estoque de uma papelaria.

O objetivo do projeto é demonstrar a aplicação das operações **CRUD** (Create, Read, Update, Delete) em um contexto prático.

## ⚙️ Funcionalidades Implementadas

O sistema permite realizar as seguintes operações no estoque:

1.  **Adicionar Item (Create):** Insere um novo produto no estoque (Nome, Preço, Quantidade e Código Interno).
2.  **Visualizar Itens (Read):** Lista todos os produtos cadastrados.
3.  **Atualizar Item (Update):** Modifica os dados de um produto existente pelo seu ID.
4.  **Excluir Item (Delete):** Remove um produto do banco de dados pelo ID.

## 🛠️ Tecnologias

* **Linguagem:** Python 3.10+ (Utiliza a sintaxe `match/case`)
* **Banco de Dados:** SQLite3 (Embutido no Python)

## 📦 Como rodar o projeto

1.  **Pré-requisitos:** Certifique-se de ter o Python 3 instalado.
2.  **Estrutura:** Garanta que os arquivos `main.py` (código principal) e `database.py` (manipulação do banco) estão na mesma pasta.
3.  **Execução:** Abra o terminal na pasta do projeto e execute:
    ```bash
    python main.py
    ```
    O arquivo do banco de dados (`Estoque_papelaria.db`) será criado automaticamente na primeira execução.