# Sistema de Gerenciamento de Biblioteca Escolar - Python integrado com MongoDB

### Informações:

**Integrantes:** Alexsander Borchardt, Ester Bertolani, João Paulo Poubel, Marcelo Mindas, Vanderson de Almeida

**Disciplina:** Banco de Dados

**Professor:** Howard Roatti Cruz

**Turma:** 4HC1A

**Vídeo de apresentação:** https://www.youtube.com/watch?v=94U1pQSlAb8 <-- video antigo (atualizar)


## Descrição do Projeto

O **Sistema de Biblioteca** tem como objetivo gerenciar o cadastro de leitores, livros e empréstimos, permitindo o controle completo das operações de uma biblioteca acadêmica.

O sistema foi desenvolvido em **Python**, com integração ao **banco de dados MongoDB**, simulando um sistema real de CRUD completo com persistência de dados, relatórios e controle de registros.

O sistema implementa:

   * **CRUD completo** (Create, Read, Update, Delete) para:
      * *Leitores*
      * *Livros*
      * *Empréstimos*

   * **Relatórios automatizados**, como:
      1. *Relatório de empréstimos detalhados (JOIN entre tabelas)*
      2. *Relatório de livros mais emprestados (GROUP BY)*

## Estrutura do Projeto_

   ```
   .
   ├── src/
   │   ├── conexion/                               # Conexão com o banco de dados
   │   │   ├── mysql_queries.py
   │   │   └── passphrase/
   │   │       ├── authentication.mysql            # Credenciais do MySQL
   │   │       └── authentication.mongo            # Credenciais do Mongo
   │   ├── controller/                             # Controladores CRUD
   │   │   ├── controller_leitor.py
   │   │   ├── controller_livro.py
   │   │   └── controller_emprestimo.py
   │   ├── model/                                  # Classes de domínio (OOP)
   │   │   ├── leitor.py
   │   │   ├── livro.py
   │   │   └── emprestimo.py
   │   ├── reports/                                # Relatórios e exibição
   │   │   └── relatorios.py
   │   ├── utils/                                  # Funções auxiliares
   │   │   ├── config.py
   │   │   └── splash_screen.py
   │   ├── createCollectionsAndData.py             # Cria as coleções de dados do banco não relacional
   │   ├── principal.py                            # Menu principal da aplicação
   │   └── requirements.txt                        # Dependências Python
   ├── .gitignore
   ├── LICENSE
   └── README.md
   ```

## Requisitos do Ambiente

   ### Software Necessário:

   * **Python 3.10+** instalado no sistema
   * **MySQL Server** configurado e rodando localmente
   * **VS Code**


   Dependências listadas em:


      src/requirements.txt
   
   
   Instale as dependências com:


      pip install -r src/requirements.txt



## Execução do Projeto no Linux

   #### 1. Clonar o repositório

      git clone https://github.com/MarceloMindas/sistema_biblioteca.git
      cd sistema_biblioteca

   #### 2. Criar e ativar ambiente virtual

      python3 -m venv venv
      source venv/bin/activate


   #### 3. Instalar dependências

      pip install -r src/requirements.txt


   #### 4. Configurar autenticação com o MySQL

   * Edite o arquivo:
      ```  
      nano src/conexion/passphrase/authentication.mysql
      ```

   * Adicione suas credenciais no formato:
      ```
      usuario,senha
      ```
   
   > Exemplo:

      root,minhasenha123


   #### 5. Criar tabelas e inserir dados iniciais

      python3 src/create_tables_and_records.py


   #### 6. Executar o sistema principal

      python3 src/principal.py


   O menu principal será exibido no terminal:

      === MENU PRINCIPAL ===
      1 - Relatórios
      2 - Inserir Registros
      3 - Atualizar Registros
      4 - Remover Registros
      0 - Sair


   #### 7. Encerrar o ambiente virtual

      deactivate


## Relatórios Implementados

1. **Relatório de Empréstimos Detalhados (JOIN):**
   Exibe leitor, livro, data de empréstimo e devolução.

2. **Relatório de Livros Mais Emprestados (GROUP BY):**
   Mostra a contagem total de empréstimos por livro.


## Dicas Extras

* **Rodar o MySQL manualmente:**

  ```bash
  sudo service mysql start
  ```
* **Verificar status do banco:**

  ```bash
  sudo service mysql status
  ```
* **Encerrar banco:**

  ```bash
  sudo service mysql stop
  ```

## Solução de Problemas Comuns

* *Erro:* mysql.connector.errors.ProgrammingError: 1045 (28000)

   > As credenciais no arquivo authentication.mysql estão incorretas.

* *Erro:* Table 'sistema_biblioteca.leitor' doesn't exist

   > Execute novamente:

      python3 src/create_tables_and_records.py

