from conexion.mongo_queries import MongoQueries
from model.leitor import Leitor

class ControllerLeitor:
    def __init__(self):
        self.mongo = MongoQueries()

    # ---------------------------------------
    # AUXILIAR — verifica existência por CPF
    # ---------------------------------------
    def existe_leitor(self, cpf: str) -> bool:
        self.mongo.connect()
        result = self.mongo.db["leitor"].find_one({"cpf": cpf})
        self.mongo.close()
        return result is not None

    # ---------------------------------------
    # CREATE
    # ---------------------------------------
    def cadastrar_leitor(self) -> Leitor:
        try:
            cpf = input("Digite o CPF do leitor: ")

            if not self.existe_leitor(cpf):
                nome = input("Digite o nome do leitor: ")
                telefone = input("Digite o telefone do leitor: ")
                email = input("Digite o email do leitor: ")

                # Gerando ID igual ao AUTO_INCREMENT do MySQL
                self.mongo.connect()
                ultimo = self.mongo.db["leitor"].find_one(sort=[("id_leitor", -1)])
                novo_id = 1 if ultimo is None else ultimo["id_leitor"] + 1

                self.mongo.db["leitor"].insert_one({
                    "id_leitor": novo_id,
                    "nome": nome,
                    "cpf": cpf,
                    "telefone": telefone,
                    "email": email
                })
                self.mongo.close()

                novo_leitor = Leitor(
                    id_leitor=novo_id,
                    nome=nome,
                    cpf=cpf,
                    telefone=telefone,
                    email=email
                )

                print("\nLeitor cadastrado com sucesso!")
                print(novo_leitor.to_string())
                return novo_leitor

            else:
                print("Leitor já cadastrado.")
                return None

        except Exception as e:
            print(f"Erro ao cadastrar leitor: {e}")

    # ---------------------------------------
    # UPDATE
    # ---------------------------------------
    def atualizar_leitor(self) -> Leitor:
        try:
            cpf = input("Digite o CPF do leitor a ser atualizado: ")

            if self.existe_leitor(cpf):
                nome = input("Novo nome: ")
                telefone = input("Novo telefone: ")
                email = input("Novo email: ")

                self.mongo.connect()
                self.mongo.db["leitor"].update_one(
                    {"cpf": cpf},
                    {"$set": {
                        "nome": nome,
                        "telefone": telefone,
                        "email": email
                    }}
                )
                leitor_atualizado = self.mongo.db["leitor"].find_one({"cpf": cpf})
                self.mongo.close()

                leitor = Leitor(
                    leitor_atualizado["id_leitor"],
                    leitor_atualizado["nome"],
                    leitor_atualizado["cpf"],
                    leitor_atualizado["telefone"],
                    leitor_atualizado["email"]
                )

                print("\nLeitor atualizado com sucesso!")
                print(leitor.to_string())
                return leitor

            else:
                print("Leitor não encontrado.")
                return None

        except Exception as e:
            print(f"Erro ao atualizar leitor: {e}")

    # ---------------------------------------
    # DELETE
    # ---------------------------------------
    def excluir_leitor(self):
        try:
            cpf = input("Digite o CPF do leitor a ser excluído: ")

            if self.existe_leitor(cpf):
                self.mongo.connect()
                self.mongo.db["leitor"].delete_one({"cpf": cpf})
                self.mongo.close()

                print("\nLeitor excluído com sucesso!")

            else:
                print("Leitor não encontrado.")

        except Exception as e:
            print(f"Erro ao excluir leitor: {e}")
