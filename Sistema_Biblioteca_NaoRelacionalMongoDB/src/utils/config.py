# ===============================
# MENUS DO SISTEMA
# ===============================

MENU_PRINCIPAL = """
############################################################
#                     MENU PRINCIPAL                       #
############################################################
#                                                          #
#    1 - RELATÓRIOS                                        #
#    2 - INSERIR REGISTROS                                 #
#    3 - ATUALIZAR REGISTROS                               #
#    4 - REMOVER REGISTROS                                 #
#    0 - SAIR                                              #
#                                                          #
############################################################
"""

MENU_RELATORIOS = """
############################################################
#                       RELATÓRIOS                         #
############################################################
#                                                          #
#    1 - RELATÓRIO DE EMPRÉSTIMOS DETALHADOS               #
#    2 - RELATÓRIO DE TOTAL DE EMPRÉSTIMOS POR LIVRO       #
#    0 - SAIR                                              #
#                                                          #
############################################################
"""

MENU_ENTIDADES = """
############################################################
#                        ENTIDADES                         #
############################################################
#                                                          #
#    1 - LEITORES                                          #
#    2 - LIVROS                                            #
#    3 - EMPRÉSTIMOS                                       #
#    0 - SAIR                                              #
#                                                          #
############################################################
"""

EXIT = """
############################################################
#          OBRIGADO POR UTILIZAR O NOSSO SISTEMA!          #
############################################################
"""

# ===============================
# FUNÇÃO UTILITÁRIA
# ===============================


def clear_console(wait_time: int = 2):
    """
    Limpa a tela após alguns segundos.
    Compatível com Windows (cls) e Linux/Mac (clear).
    """
    import os
    from time import sleep
    sleep(wait_time)
    os.system('cls' if os.name == 'nt' else 'clear')
