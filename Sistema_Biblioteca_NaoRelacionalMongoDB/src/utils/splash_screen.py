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
        l = str(self.get_total_leitores()).rjust(5)
        b = str(self.get_total_livros()).rjust(5)
        e = str(self.get_total_emprestimos()).rjust(5)

        line_created = f"  CRIADO POR: {self.created_by}"
        line_disc = f"  DISCIPLINA: {self.disciplina}"
        line_prof = f"  PROFESSOR:   {self.professor}"

        return f"""
###########################################################################
#                    SISTEMA DE BIBLIOTECA - MONGODB                      #
#                                                                         #
#  TOTAL DE REGISTROS:                                                    #
#     1 - LEITORES:     {l}                                             #
#     2 - LIVROS:       {b}                                             #
#     3 - EMPRÉSTIMOS:  {e}                                             #
#                                                                         #
#{line_created.ljust(73)}#
#{line_disc.ljust(73)}#
#{line_prof.ljust(73)}#
###########################################################################
"""

    def show(self):
        print(self.get_updated_screen())
        config.clear_console(4)
