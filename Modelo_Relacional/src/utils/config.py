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
2 - Relatório de Total de Empréstimos por Livros
0 - SAIR
"""

MENU_ENTIDADES = """
=== ENTIDADES ===
1 - Leitores
2 - Livros
3 - Empréstimos
0 - SAIR
"""

QUERY_COUNT = 'select count(1) as total_{tabela} from {tabela}'


def clear_console(wait_time: int = 2):
    '''
    Limpa a tela após alguns segundos.
    '''
    import os
    from time import sleep
    sleep(wait_time)
    os.system('cls' if os.name == 'nt' else 'clear')