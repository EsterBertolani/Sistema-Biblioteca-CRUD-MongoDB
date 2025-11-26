# Sistema de Gerenciamento de Biblioteca Escolar - Python integrado com MongoDB

### Informações:

**Integrantes:** Alexsander Borchardt, Ester Bertolani, João Paulo Poubel, Marcelo Mindas, Vanderson de Almeida

**Disciplina:** Banco de Dados Não Relacional

**Professor:** Howard Roatti Cruz

**Turma:** 4HC1A

**Vídeo de apresentação:** (https://youtu.be/DoS1OmE0yO8)

## Descrição do Projeto

O **Sistema de Biblioteca** tem como objetivo gerenciar o cadastro de leitores, livros e empréstimos, permitindo o controle completo das operações de uma biblioteca acadêmica.

O sistema foi refatorado para utilizar **Python** com integração ao banco de dados **MongoDB**, substituindo o modelo relacional rígido por uma abordagem baseada em documentos. Isso permite maior flexibilidade na manipulação dos dados.

O sistema implementa:

* **CRUD completo** (Create, Read, Update, Delete) para:
    * *Leitores*
    * *Livros*
    * *Empréstimos*
* **Relatórios automatizados** utilizando *Aggregation Framework* do Mongo:
    1. *Relatório de empréstimos detalhados (usando $lookup para simular JOIN)*
    2. *Relatório de livros mais emprestados (usando $group e $sum)*

## Estrutura do Projeto

````
.
├── src/
│   ├── conexion/                           # Conexão com o Banco de Dados
│   │   ├── mongo_queries.py
│   │   └── passphrase/
│   │       └── authentication.mongo        # Configuração de Acesso (Local ou Auth)
│   ├── controller/                         # Controladores (Regras de Negócio)
│   │   ├── controller_leitor.py
│   │   ├── controller_livro.py
│   │   └── controller_emprestimo.py
│   ├── model/                              # Classes de Domínio (Objetos)
│   │   ├── leitor.py
│   │   ├── livro.py
│   │   └── emprestimo.py
│   ├── reports/                            # Relatórios (Aggregation Pipelines)
│   │   └── relatorios.py
│   ├── utils/                              # Utilitários
│   │   ├── config.py                       # Menus e limpeza de tela
│   │   └── splash_screen.py                # Tela inicial com contadores
│   ├── createCollectionsAndData.py         # Script para criar coleções e dados iniciais
│   ├── principal.py                        # Interface principal (Menu)
│   └── requirements.txt                    # Dependências do projeto
├── .gitignore
├── LICENSE
└── README.md

````

## Requisitos do Ambiente

### Software Necessário:

* **Python 3.10+** instalado no sistema
* **MongoDB** (Serviço local ou Docker container)
* **VS Code** (ou editor de preferência)

### Dependências

Listadas em `src/requirements.txt`. A principal biblioteca utilizada é o `pymongo`.

## Execução do Projeto no Linux

Siga os passos abaixo para rodar o projeto no terminal do Linux ou WSL.

#### 1. Clonar o repositório

```bash
git clone https://github.com/EsterBertolani/Sistema-Biblioteca-CRUD-MongoDB.git

cd Sistema-Biblioteca-CRUD-MongoDB
````

#### 2. Criar e ativar o ambiente virtual

```bash
python3 -m venv venv

source venv/bin/activate
```

#### 3. Instalar dependências

```bash
pip install -r src/requirements.txt
```

#### 4. Configurar a Conexão com o MongoDB

O sistema utiliza uma **Connection String (URI)** padrão para se conectar ao banco. Isso permite flexibilidade para conectar localmente, em containers Docker ou na nuvem (Atlas).

Edite o arquivo de configuração:
```bash
nano src/conexion/passphrase/authentication.mongo
````

Você deve colar a **URL de conexão completa** dentro deste arquivo.

  * **Opção A - MongoDB Local (Padrão):**
    Se você está rodando o Mongo na sua própria máquina (sem senha), use:

    ```text
    mongodb://localhost:27017/
    ```

  * **Opção B - MongoDB com Autenticação (Docker):**
    Se estiver usando um banco com senha, o formato deve ser:
    `mongodb://usuario:senha@host:porta/`

    Exemplo (para usuário `root` e senha `minhasenha123`):

    ```text
    mongodb://root:minhasenha123@localhost:27017/
    ```


#### 5. Criar coleções e inserir dados iniciais

Antes de rodar o sistema, execute o script que popula o banco, criando as coleções e inserindo dados de exemplo.

```bash
python3 src/createCollectionsAndData.py
```

> *Mensagem esperada: "Dados iniciais inseridos com sucesso\!"*

#### 6. Executar o sistema principal

```bash
python3 src/principal.py
```

O menu principal será exibido após a splash screen:

```text
############################################################
#                     MENU PRINCIPAL                       #
############################################################
#                                                          #
#    1 - RELATÓRIOS                                        #
#    2 - INSERIR REGISTROS                                 #
#    3 - ATUALIZAR REGISTROS                               #
#    4 - REMOVER REGISTROS                                 #
#    0 - SAIR                                              #
#                                                          #
############################################################
```

## Relatórios Implementados

1.  **Relatório de Empréstimos Detalhados:**
    Utiliza o pipeline `$lookup` para buscar dados das coleções `leitor` e `livro` e exibir os nomes em vez dos IDs nos empréstimos.

2.  **Relatório de Livros Mais Emprestados:**
    Utiliza o pipeline `$group` para contar quantas vezes cada livro aparece na coleção de empréstimos e ordena de forma decrescente.

## Solução de Problemas Comuns

  * **Erro:** `pymongo.errors.ServerSelectionTimeoutError`

    > **Causa:** O MongoDB não está rodando ou o endereço/porta está errado.
    > **Solução:** Verifique se o serviço do Mongo está ativo (`sudo service mongod status` ou `docker ps`).

  * **Erro:** `ModuleNotFoundError: No module named 'conexion'`

    > **Causa:** Você está tentando rodar o script de dentro da pasta `src` sem configurar o path, ou da raiz incorretamente.
    > **Solução:** Execute sempre a partir da raiz do projeto usando `python3 src/principal.py`.

-----
