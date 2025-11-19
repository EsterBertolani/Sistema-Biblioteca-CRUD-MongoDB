from bson import ObjectId

# precisa instalar o pacote 'bson' se não estiver usando o pymongo diretamente

class Leitor:
    def __init__(self,
                _id: ObjectId = None, #  no Mongo o _id padrão é um ObjectId. Usar ObjectId() garante IDs únicos e compatibilidade direta com drivers (pymongo).
                 nome: str = "",
                 cpf: str = "",
                 telefone: str = "",
                 email: str = ""):
        
        self._id = _id if _id else ObjectId()
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email

    # ----------------------------------------
    def to_dict(self): # converte o objeto em um dicionário para facilitar a inserção
        return {
            "_id": self._id,
            "nome": self.nome,
            "cpf": self.cpf,
            "telefone": self.telefone,
            "email": self.email
        }

    # ----------------------------------------
    @staticmethod
    def from_dict(dados: dict): # cria um objeto leitor a partir de um dicionário recebido do banco
        return Leitor(
            _id=dados.get("_id"),
            nome=dados.get("nome"),
            cpf=dados.get("cpf"),
            telefone=dados.get("telefone"),
            email=dados.get("email")
        )

    # ----------------------------------------
    def to_string(self):
        return (
            f"ID Leitor: {self._id} | "
            f"Nome: {self.nome} | "
            f"CPF: {self.cpf} | "
            f"Telefone: {self.telefone} | "
            f"Email: {self.email}"
        )
