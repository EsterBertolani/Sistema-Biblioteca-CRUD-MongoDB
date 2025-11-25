from utils import config
from utils.splash_screen import SplashScreen
from reports.relatorios import Relatorios
from controller.controller_leitor import ControllerLeitor
from controller.controller_livro import ControllerLivro
from controller.controller_emprestimo import ControllerEmprestimo

# Instâncias principais do sistema
tela_inicial = SplashScreen()
relatorio = Relatorios()
ctrl_leitor = ControllerLeitor()
ctrl_livro = ControllerLivro()
ctrl_emprestimo = ControllerEmprestimo()


# ============================================================
# Função para leitura de opção com validação
# ============================================================
def pedir_opcao(menu_text: str) -> int:
    while True:
        print(menu_text)
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite um número válido.\n")


# ============================================================
# RELATÓRIOS
# ============================================================
def reports(opcaoRelatorio: int):
    match opcaoRelatorio:
        case 1:
            relatorio.get_relatorio_emprestimos_detalhados()

        case 2:
            relatorio.get_relatorio_total_emprestimos_por_livro()

        case _:
            print("Opção inválida.")


# ============================================================
# INSERIR
# ============================================================
def insert(opcaoInsert: int):
    match opcaoInsert:
        case 1:
            ctrl_leitor.cadastrar_leitor()

        case 2:
            ctrl_livro.cadastrar_livro()

        case 3:
            ctrl_emprestimo.cadastrar_emprestimo()

        case _:
            print("Opção inválida.")


# ============================================================
# ATUALIZAR
# ============================================================
def update(opcaoUpdate: int):
    match opcaoUpdate:
        case 1:
            ctrl_leitor.atualizar_leitor()

        case 2:
            ctrl_livro.atualizar_livro()

        case 3:
            ctrl_emprestimo.atualizar_emprestimo()

        case _:
            print("Opção inválida.")


# ============================================================
# REMOVER
# ============================================================
def delete(opcaoDelete: int):
    match opcaoDelete:
        case 1:
            ctrl_leitor.excluir_leitor()

        case 2:
            ctrl_livro.excluir_livro()

        case 3:
            ctrl_emprestimo.excluir_emprestimo()

        case _:
            print("Opção inválida.")


# ============================================================
# EXECUÇÃO PRINCIPAL DO SISTEMA
# ============================================================
def run():
    print(tela_inicial.get_updated_screen())
    print("Iniciando o sistema...")
    config.clear_console(3)

    while True:
        opcao = pedir_opcao(config.MENU_PRINCIPAL)

        match opcao:
            case 1:
                opRelatorios = pedir_opcao(config.MENU_RELATORIOS)
                if opRelatorios == 0:
                    print(tela_inicial.get_updated_screen())
                    config.clear_console()
                else:
                    reports(opRelatorios)

            case 2:
                opInsert = pedir_opcao(config.MENU_ENTIDADES)
                if opInsert == 0:
                    print(tela_inicial.get_updated_screen())
                    config.clear_console()
                else:
                    insert(opInsert)

            case 3:
                opUpdate = pedir_opcao(config.MENU_ENTIDADES)
                if opUpdate == 0:
                    print(tela_inicial.get_updated_screen())
                    config.clear_console()
                else:
                    update(opUpdate)

            case 4:
                opDelete = pedir_opcao(config.MENU_ENTIDADES)
                if opDelete == 0:
                    print(tela_inicial.get_updated_screen())
                    config.clear_console()
                else:
                    delete(opDelete)

            case 0:
                print(tela_inicial.get_updated_screen())
                config.clear_console()
                print(config.EXIT)
                break

            case _:
                print("Opção inválida. Tente novamente.")
                continue

        input("\nPressione Enter para continuar...")
        print(tela_inicial.get_updated_screen())
        config.clear_console()


if __name__ == "__main__":
    run()
