from conexion.mysql_queries import MySQLQueries
from utils import config

class SplashScreen:
    
    def __init__(self):
        self.qry_total_leitores = config.QUERY_COUNT.format(tabela="leitor")
        self.qry_total_livros = config.QUERY_COUNT.format(tabela="livro")
        self.qry_total_emprestimos = config.QUERY_COUNT.format(tabela="emprestimo")

        self.created_by = "Seu Nome"
        self.disciplina = "Banco de Dados"
        self.semestre = "2025/2"

    def get_total_leitores(self):
        mysql = MySQLQueries()
        mysql.connect()
        return mysql.sqlToDataFrame(self.qry_total_leitores)["total_leitor"].values[0]

    def get_total_livros(self):
        mysql = MySQLQueries()
        mysql.connect()
        return mysql.sqlToDataFrame(self.qry_total_livros)["total_livro"].values[0]

    def get_total_emprestimos(self):
        mysql = MySQLQueries()
        mysql.connect()
        return mysql.sqlToDataFrame(self.qry_total_emprestimos)["total_emprestimo"].values[0]

    def get_updated_screen(self):
        return f"""
########################################################
#              SISTEMA DE BIBLIOTECA                   #
#                                                     #
#  TOTAL DE REGISTROS:                                #
#     1 - LEITORES:     {str(self.get_total_leitores()).rjust(5)}             #
#     2 - LIVROS:       {str(self.get_total_livros()).rjust(5)}             #
#     3 - EMPRÉSTIMOS:  {str(self.get_total_emprestimos()).rjust(5)}             #
#                                                     #
#  CRIADO POR: {self.created_by}                      #
#  DISCIPLINA: {self.disciplina}                      #
#  SEMESTRE:   {self.semestre}                        #
########################################################
"""