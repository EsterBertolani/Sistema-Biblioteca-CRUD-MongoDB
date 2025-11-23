from conexion.mongo_queries import MongoQueries

class CreateCollectionsAndData:
    def __init__(self):
        self.mongo = MongoQueries()
        self.mongo.connect()

        # Coleções que serão criadas (no singular)
        self.collections = ["leitor", "livro", "emprestimo"]

    # ---------------------------------------------------------
    def create_collections(self, drop_if_exists: bool = False):
        """
        Cria as coleções no MongoDB.
        Se drop_if_exists=True, apaga a coleção antiga e recria.
        """
        existing = self.mongo.db.list_collection_names()

        for col in self.collections:
            if col in existing:
                if drop_if_exists:
                    self.mongo.db.drop_collection(col)
                    print(f"Collection '{col}' removida.")
                    self.mongo.db.create_collection(col)
                    print(f"Collection '{col}' recriada.")
                else:
                    print(f"Collection '{col}' já existe. (sem alterações)")
            else:
                self.mongo.db.create_collection(col)
                print(f"Collection '{col}' criada.")

    # ---------------------------------------------------------
    def insert_initial_data(self):
        """
        Insere dados iniciais nas coleções.
        Esses dados imitam as tabelas originais do projeto relacional.
        """

        # ---- Dados de Leitor ----
        leitores = [
            {
                "nome": "Maria Silva",
                "cpf": "123.456.789-00",
                "telefone": "(27) 99999-1111",
                "email": "maria.silva@example.com"
            },
            {
                "nome": "João Pedro",
                "cpf": "987.654.321-00",
                "telefone": "(27) 98888-2222",
                "email": "joao.pedro@example.com"
            },
            {
                "nome": "Ana Oliveira",
                "cpf": "111.222.333-44",
                "telefone": "(27) 97777-3333",
                "email": "ana.oliveira@example.com"
            }
        ]

        # ---- Dados de Livro ----
        livros = [
            {
                "titulo": "Dom Casmurro",
                "autor": "Machado de Assis",
                "editora": "Globo",
                "categoria": "Romance",
                "quantidade": 3
            },
            {
                "titulo": "O Hobbit",
                "autor": "J. R. R. Tolkien",
                "editora": "Harper",
                "categoria": "Fantasia",
                "quantidade": 2
            },
            {
                "titulo": "1984",
                "autor": "George Orwell",
                "editora": "Companhia das Letras",
                "categoria": "Distopia",
                "quantidade": 4
            }
        ]

        # ---- Dados de Emprestimo (referências simples) ----
        # OBS: normalmente inclui o ObjectId real do leitor/livro
        # mas aqui deixamos para o CRUD gerar corretamente
        emprestimos = [
            {
                "id_leitor_fake": "Maria Silva",
                "id_livro_fake": "Dom Casmurro",
                "data_emprestimo": "2024-11-01",
                "data_devolucao_prevista": "2024-11-10",
                "data_devolucao_realizada": None
            }
        ]

        # Inserção nas coleções
        self.mongo.db["leitor"].insert_many(leitores)
        self.mongo.db["livro"].insert_many(livros)
        self.mongo.db["emprestimo"].insert_many(emprestimos)

        print("Dados iniciais inseridos com sucesso.")

    # ---------------------------------------------------------
    def run(self):
        """Executa todo o processo de criação e inserção."""
        print("Criando coleções...")
        self.create_collections(drop_if_exists=True)

        print("\nInserindo dados iniciais...")
        self.insert_initial_data()

        self.mongo.close()
        print("\nProcesso concluído!")


# Execução direta
if __name__ == "__main__":
    CreateCollectionsAndData().run()
