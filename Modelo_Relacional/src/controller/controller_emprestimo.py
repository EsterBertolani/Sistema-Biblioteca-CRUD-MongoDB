from datetime import datetime, date
from conexion.mongo_queries import MongoQueries
from model.leitor import Leitor
from model.livro import Livro
from model.emprestimo import Emprestimo

class ControllerEmprestimo:
    def __init__(self):
        self.mongo = MongoQueries()

    # ---------------------------------------
    # AUXILIAR — verifica existência por ID
    # ---------------------------------------
    def existe_emprestimo(self, id_emprestimo: int) -> bool:
        self.mongo.connect()
        result = self.mongo.db["emprestimo"].find_one({"id_emprestimo": id_emprestimo})
        self.mongo.close()
        return result is not None

    def existe_leitor(self, id_leitor: int) -> dict:
        self.mongo.connect()
        leitor = self.mongo.db["leitor"].find_one({"id_leitor": id_leitor})
        self.mongo.close()
        return leitor

    def existe_livro(self, id_livro: int) -> dict:
        self.mongo.connect()
        livro = self.mongo.db["livro"].find_one({"id_livro": id_livro})
        self.mongo.close()
        return livro

    # ---------------------------------------
    # CREATE — CADASTRAR EMPRÉSTIMO
    # ---------------------------------------
    def cadastrar_emprestimo(self) -> Emprestimo:
        try:
            id_leitor = int(input("ID do leitor: "))
            id_livro = int(input("ID do livro: "))

            leitor_db = self.existe_leitor(id_leitor)
            livro_db = self.existe_livro(id_livro)

            if leitor_db is None:
                print("Leitor não encontrado.")
                return None
            if livro_db is None:
                print("Livro não encontrado.")
                return None

            # Gerar id_emprestimo igual ao AUTO_INCREMENT do MySQL
            self.mongo.connect()
            ultimo = self.mongo.db["emprestimo"].find_one(sort=[("id_emprestimo", -1)])
            novo_id = 1 if ultimo is None else ultimo["id_emprestimo"] + 1

            data_emprestimo = date.today()
            data_prevista = date.fromisoformat(
                input("Data prevista de devolução (AAAA-MM-DD): ")
            )

            self.mongo.db["emprestimo"].insert_one({
                "id_emprestimo": novo_id,
                "id_leitor": id_leitor,
                "id_livro": id_livro,
                "data_emprestimo": str(data_emprestimo),
                "data_devolucao_prevista": str(data_prevista),
                "data_devolucao_realizada": None
            })
            self.mongo.close()

            # Criar objetos para retorno
            leitor_obj = Leitor(
                leitor_db["id_leitor"],
                leitor_db["nome"],
                leitor_db["cpf"],
                leitor_db["telefone"],
                leitor_db["email"]
            )

            livro_obj = Livro(
                livro_db["id_livro"],
                livro_db["titulo"],
                livro_db["autor"],
                livro_db["editora"],
                livro_db["categoria"],
                livro_db["quantidade"]
            )

            emprestimo = Emprestimo(
                novo_id,
                leitor_obj,
                livro_obj,
                data_emprestimo,
                data_prevista,
                None
            )

            print("\nEmpréstimo cadastrado com sucesso!")
            print(emprestimo.to_string())
            return emprestimo

        except Exception as e:
            print(f"Erro ao cadastrar empréstimo: {e}")

    # ---------------------------------------
    # UPDATE — Registrar devolução
    # ---------------------------------------
    def atualizar_emprestimo(self) -> Emprestimo:
        try:
            id_emprestimo = int(input("ID do empréstimo para atualizar: "))

            if not self.existe_emprestimo(id_emprestimo):
                print("Empréstimo não encontrado.")
                return None

            data_devolucao = date.fromisoformat(
                input("Data de devolução REALIZADA (AAAA-MM-DD): ")
            )

            self.mongo.connect()
            self.mongo.db["emprestimo"].update_one(
                {"id_emprestimo": id_emprestimo},
                {"$set": {"data_devolucao_realizada": str(data_devolucao)}}
            )
            emp = self.mongo.db["emprestimo"].find_one({"id_emprestimo": id_emprestimo})
            self.mongo.close()

            # Buscar dados do leitor e livro
            leitor_db = self.existe_leitor(emp["id_leitor"])
            livro_db = self.existe_livro(emp["id_livro"])

            leitor_obj = Leitor(
                leitor_db["id_leitor"],
                leitor_db["nome"],
                leitor_db["cpf"],
                leitor_db["telefone"],
                leitor_db["email"]
            )

            livro_obj = Livro(
                livro_db["id_livro"],
                livro_db["titulo"],
                livro_db["autor"],
                livro_db["editora"],
                livro_db["categoria"],
                livro_db["quantidade"]
            )

            emprestimo = Emprestimo(
                emp["id_emprestimo"],
                leitor_obj,
                livro_obj,
                date.fromisoformat(emp["data_emprestimo"]),
                date.fromisoformat(emp["data_devolucao_prevista"]),
                data_devolucao
            )

            print("\nEmpréstimo atualizado com sucesso!")
            print(emprestimo.to_string())
            return emprestimo

        except Exception as e:
            print(f"Erro ao atualizar empréstimo: {e}")

    # ---------------------------------------
    # DELETE — Remover empréstimo
    # ---------------------------------------
    def excluir_emprestimo(self):
        try:
            id_emprestimo = int(input("ID do empréstimo para excluir: "))

            if not self.existe_emprestimo(id_emprestimo):
                print("Empréstimo não encontrado.")
                return

            self.mongo.connect()
            self.mongo.db["emprestimo"].delete_one({"id_emprestimo": id_emprestimo})
            self.mongo.close()

            print("\nEmpréstimo excluído com sucesso!")

        except Exception as e:
            print(f"Erro ao excluir empréstimo: {e}")
