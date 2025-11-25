from conexion.mongo_queries import MongoQueries
from model.livro import Livro


class ControllerLivro:
    def __init__(self):
        self.mongo = MongoQueries()

    # ---------------------------------------
    # AUXILIAR — verificar existência por título
    # ---------------------------------------
    def existe_livro(self, titulo: str) -> bool:
        self.mongo.connect()
        result = self.mongo.db["livro"].find_one({"titulo": titulo})
        self.mongo.close()
        return result is not None

    # ---------------------------------------
    # CREATE
    # ---------------------------------------
    def cadastrar_livro(self) -> Livro:
        try:
            titulo = input("Digite o título do livro: ")

            if not self.existe_livro(titulo):
                autor = input("Autor: ")
                editora = input("Editora: ")
                categoria = input("Categoria: ")
                quantidade = int(input("Quantidade disponível: "))

                # Gerando id_livro igual ao AUTO_INCREMENT
                self.mongo.connect()
                ultimo = self.mongo.db["livro"].find_one(
                    sort=[("id_livro", -1)])
                novo_id = 1 if ultimo is None else ultimo["id_livro"] + 1

                self.mongo.db["livro"].insert_one({
                    "id_livro": novo_id,
                    "titulo": titulo,
                    "autor": autor,
                    "editora": editora,
                    "categoria": categoria,
                    "quantidade": quantidade
                })
                self.mongo.close()

                livro = Livro(novo_id, titulo, autor,
                              editora, categoria, quantidade)
                print("\nLivro cadastrado com sucesso!")
                print(livro.to_string())
                return livro

            else:
                print("Livro já cadastrado.")
                return None

        except Exception as e:
            print(f"Erro ao cadastrar livro: {e}")

    # ---------------------------------------
    # UPDATE
    # ---------------------------------------
    def atualizar_livro(self) -> Livro:
        try:
            titulo = input("Digite o título do livro para atualizar: ")

            if self.existe_livro(titulo):
                autor = input("Novo autor: ")
                editora = input("Nova editora: ")
                categoria = input("Nova categoria: ")
                quantidade = int(input("Nova quantidade: "))

                self.mongo.connect()
                self.mongo.db["livro"].update_one(
                    {"titulo": titulo},
                    {"$set": {
                        "autor": autor,
                        "editora": editora,
                        "categoria": categoria,
                        "quantidade": quantidade
                    }}
                )
                livro_atualizado = self.mongo.db["livro"].find_one(
                    {"titulo": titulo})
                self.mongo.close()

                livro = Livro(
                    livro_atualizado["id_livro"],
                    livro_atualizado["titulo"],
                    livro_atualizado["autor"],
                    livro_atualizado["editora"],
                    livro_atualizado["categoria"],
                    livro_atualizado["quantidade"]
                )

                print("\nLivro atualizado com sucesso!")
                print(livro.to_string())
                return livro

            else:
                print("Livro não encontrado.")
                return None

        except Exception as e:
            print(f"Erro ao atualizar livro: {e}")

    # ---------------------------------------
    # DELETE
    # ---------------------------------------
    def excluir_livro(self):
        try:
            titulo = input("Digite o título do livro a ser excluído: ")

            if self.existe_livro(titulo):
                self.mongo.connect()
                self.mongo.db["livro"].delete_one({"titulo": titulo})
                self.mongo.close()

                print("\nLivro excluído com sucesso!")

            else:
                print("Livro não encontrado.")

        except Exception as e:
            print(f"Erro ao excluir livro: {e}")
