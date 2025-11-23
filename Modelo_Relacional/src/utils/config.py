# ===============================
# MENUS DO SISTEMA
# ===============================

MENU_PRINCIPAL = """
=== MENU PRINCIPAL ===
1 - Relatórios
2 - Inserir Registros
3 - Atualizar Registros
4 - Remover Registros
0 - SAIR
"""

MENU_RELATORIOS = """
=== RELATÓRIOS ===
1 - Relatório de Empréstimos Detalhados
2 - Relatório de Total de Empréstimos por Livro
0 - SAIR
"""

MENU_ENTIDADES = """
=== ENTIDADES ===
1 - Leitores
2 - Livros
3 - Empréstimos
0 - SAIR
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
