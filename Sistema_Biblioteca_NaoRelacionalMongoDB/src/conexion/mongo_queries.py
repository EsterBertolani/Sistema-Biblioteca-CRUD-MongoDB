import pymongo
import os
# from urllib.parse import quote_plus

class MongoQueries:

    def __init__(self):
        """
        Classe de conexão com o MongoDB local ou na VM Linux.
        A URL vem do arquivo authentication.mongo, para permitir trocar
        facilmente entre ambientes.
        """
        self.client = None
        self.db = None

        base_path = os.path.dirname(__file__)
        auth_path = os.path.join(
            base_path, "passphrase", "authentication_mongo")

        try:
            with open(auth_path, "r") as f:
                self.mongo_url = f.read().strip()

        except FileNotFoundError:
            self.mongo_url = "mongodb://localhost:27017"

        # Nome da base que vamos sempre usar
        self.database = "sistema_biblioteca"

    # ------------------------------------------

    def connect(self):
        self.client = pymongo.MongoClient(self.mongo_url)
        self.db = self.client[self.database]
        return self.client

    # ------------------------------------------
    def close(self):
        if self.client:
            self.client.close()

    # ------------------------------------------
    def get_collection(self, name: str):
        return self.db[name]


# def __init__(self):
    #     """
    #     Versão híbrida: funciona no Windows (sem auth)
    #     e no Linux com Docker do professor (com auth).
    #     """
    #     base_path = os.path.dirname(__file__)
    #     auth_path = os.path.join(base_path, "passphrase", "authentication.mongo")

    #     with open(auth_path, "r") as f:
    #         content = f.read().strip()

    #     self.host = "localhost"
    #     self.port = 27017
    #     self.database = "sistema_biblioteca"

    #     # -------------------------------
    #     # WINDOWS → SEM autenticação
    #     # arquivo contém apenas:  local
    #     # -------------------------------
    #     if content.lower() == "local":
    #         self.mode = "local"
    #         self.mongo_url = f"mongodb://{self.host}:{self.port}/"

    #     else:
    #         # ---------------------------------
    #         # LINUX / DOCKER → COM autenticação
    #         # Formato: usuario,senha
    #         # ---------------------------------
    #         self.mode = "auth"
    #         self.user, self.password = content.split(",")
    #         self.user = self.user.strip()
    #         self.password = self.password.strip()

    #         self.mongo_url = (
    #             f"mongodb://{self.user}:{quote_plus(self.password)}"
    #             f"@{self.host}:{self.port}/"
    #         )

    #     self.client = None
    #     self.db = None
