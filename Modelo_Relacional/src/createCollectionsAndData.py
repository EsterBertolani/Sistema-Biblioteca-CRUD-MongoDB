from conexion.mongo_queries import MongoQueries

class CreateCollectionsAndData:
    def __init__(self):
        self.collections = ["leitor", "livro", "emprestimo"]
        self.mongo = MongoQueries()

    def create_collections(self, drop_if_exists=True):
        self.mongo.connect()
        existing = self.mongo.db.list_collection_names()

        for col in self.collections:
            if col in existing and drop_if_exists:
                self.mongo.db.drop_collection(col)
                print(f"Collection '{col}' apagada.")
            if col not in existing or drop_if_exists:
                self.mongo.db.create_collection(col)
                print(f"Collection '{col}' criada.")

        self.mongo.close()

    def insert_initial_data(self):
        self.mongo.connect()

        # -----------------------------------------------------------
        # SEED DE LEITORES
        leitores = [
            {
                "id_leitor": 1,
                "nome": "João Silva",
                "cpf": "111.111.111-11",
                "telefone": "(27) 99999-1111",
                "email": "joao@example.com"
            },
            {
                "id_leitor": 2,
                "nome": "Maria Souza",
                "cpf": "222.222.222-22",
                "telefone": "(27) 98888-2222",
                "email": "maria@example.com"
            }
        ]

        # -----------------------------------------------------------
        # SEED DE LIVROS
        livros = [
            {
                "id_livro": 1,
                "titulo": "Dom Casmurro",
                "autor": "Machado de Assis",
                "editora": "Editora A",
                "categoria": "Romance",
                "quantidade": 5
            },
            {
                "id_livro": 2,
                "titulo": "Harry Potter",
                "autor": "J.K. Rowling",
                "editora": "Rocco",
                "categoria": "Fantasia",
                "quantidade": 3
            }
        ]

        # -----------------------------------------------------------
        # SEED DE EMPRÉSTIMOS
        emprestimos = [
            {
                "id_emprestimo": 1,
                "id_leitor": 1,
                "id_livro": 2,
                "data_emprestimo": "2025-01-10",
                "data_devolucao_prevista": "2025-01-20",
                "data_devolucao_realizada": "-"
            }
        ]

        self.mongo.db["leitor"].insert_many(leitores)
        self.mongo.db["livro"].insert_many(livros)
        self.mongo.db["emprestimo"].insert_many(emprestimos)

        print("\nDados iniciais inseridos com sucesso!")

        self.mongo.close()

    def run(self):
        print("Criando coleções...")
        self.create_collections()
        print("\nInserindo dados...")
        self.insert_initial_data()
        print("\nProcesso concluído com sucesso!")

if __name__ == "__main__":
    CreateCollectionsAndData().run()
