import pymongo

class MongoQueries:
    def __init__(self):
        """
        Classe de conexão com o MongoDB local ou na VM Linux.
        A URL vem do arquivo authentication.mongo, para permitir trocar
        facilmente entre ambientes.
        """
        self.client = None
        self.db = None

        # Lê a URL do arquivo de autenticação
        with open("src/conexion/passphrase/authentication.mongo", "r") as f:
            self.mongo_url = f.read().strip()

        # Nome da base que vamos sempre usar
        self.database = "sistema_biblioteca"

    # -------------------------
    def connect(self):
        """Conecta no MongoDB usando a URL do arquivo."""
        self.client = pymongo.MongoClient(self.mongo_url)
        self.db = self.client[self.database]
        return self.client

    # -------------------------
    def close(self):
        """Fecha a conexão com o MongoDB."""
        if self.client:
            self.client.close()

    # -------------------------
    def get_collection(self, collection_name: str):
        """Retorna uma coleção específica."""
        return self.db[collection_name]
