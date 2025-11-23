from conexion.mongo_queries import MongoQueries
from utils import config

class SplashScreen:

    def __init__(self):
        self.created_by = "Alexsander, Ester, João Paulo, Marcelo e Vanderson"
        self.disciplina = "Banco de Dados Não Relacional"
        self.professor = "Prof. M.Sc. Howard Roatti"

    # --------------------------------------------------------------
    # Métodos de contagem usando MongoDB
    # --------------------------------------------------------------
    def get_total_leitores(self):
        mongo = MongoQueries()
        mongo.connect()
        total = mongo.db["leitor"].count_documents({})
        mongo.close()
        return total

    def get_total_livros(self):
        mongo = MongoQueries()
        mongo.connect()
        total = mongo.db["livro"].count_documents({})
        mongo.close()
        return total

    def get_total_emprestimos(self):
        mongo = MongoQueries()
        mongo.connect()
        total = mongo.db["emprestimo"].count_documents({})
        mongo.close()
        return total

    # --------------------------------------------------------------
    # Template da Splash Screen
    # --------------------------------------------------------------
    def get_updated_screen(self):
        return f"""
###################################################################
#              SISTEMA DE BIBLIOTECA - MONGODB                    #
#                                                                 #
#  TOTAL DE REGISTROS:                                            #
#     1 - LEITORES:     {str(self.get_total_leitores()).rjust(5)} #
#     2 - LIVROS:       {str(self.get_total_livros()).rjust(5)}   #
#     3 - EMPRÉSTIMOS:  {str(self.get_total_emprestimos()).rjust(5)} #
#                                                                 #
#  CRIADO POR: {self.created_by}
#  DISCIPLINA: {self.disciplina}
#  PROFESSOR:   {self.professor}
###################################################################
"""

    def show(self):
        print(self.get_updated_screen())
        config.clear_console(4)
