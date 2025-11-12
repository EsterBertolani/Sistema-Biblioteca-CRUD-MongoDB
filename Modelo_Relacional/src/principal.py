from utils import config
# from utils.splash_screen import SplashScreen
from reports.relatorios import Relatorios
from controller.controller_leitor import ControllerLeitor
from controller.controller_livro import ControllerLivro
from controller.controller_emprestimo import ControllerEmprestimo

# tela_inicial = SplashScreen()
relatorio = Relatorios()
ctrl_leitor = ControllerLeitor()
ctrl_livro = ControllerLivro()
ctrl_emprestimo = ControllerEmprestimo()

def pedir_opcao(menu_text: str) -> int:
    """vai mostrar o tipo de menu que passar por parâmetro e pedir a opção dele (tratamento de erro)"""
    while True:
        print(menu_text)
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite um número válido.")
            continue


def reports(opcaoRelatorio: int):
    match opcaoRelatorio:
        case 1:
            relatorio.get_relatorio_emprestimos_detalhados()

        case 2:
            relatorio.get_relatorio_total_emprestimos_por_livro()

        case _:
            print("Inválido. Tente novamente.")
            return


def insert(opcaoInsert: int):
    match opcaoInsert:
        case 1:
            ctrl_leitor.cadastrar_leitor()

        case 2:
            ctrl_livro.cadastrar_livro()

        case 3:
            ctrl_emprestimo.registrar_emprestimo()

        case _:
            print("Inválido. Tente novamente.")
            return


def update(opcaoUpdate: int):
    match opcaoUpdate:
        case 1:
            ctrl_leitor.atualizar_leitor()

        case 2:
            ctrl_livro.atualizar_livro()

        case 3:
            ctrl_emprestimo.devolver_livro()

        case _:
            print("Inválido. Tente novamente.")
            return


def delete(opcaoDelete: int):
    match opcaoDelete:
        case 1:
            ctrl_leitor.excluir_leitor()

        case 2:
            ctrl_livro.excluir_livro()

        case 3:
            ctrl_emprestimo.excluir_emprestimo()

        case _:
            print("Inválido. Tente novamente.")
            return


def run():
    # print(tela_inicial.get_updated_screen())
    # print(tela_inicial.get_updated_screen())
    config.clear_console(3)

    while True:
        print(config.MENU_PRINCIPAL)
        try:
            opcao = int(input("Escolha uma opção: "))

            opcao = int(input("Escolha uma opção: "))

        except ValueError:
            print("Digite um número válido.")
            continue

        match opcao:
            case 1:
                opRelatorios = pedir_opcao(config.MENU_RELATORIOS)
                if opRelatorios == 0:
                    continue
                reports(opRelatorios)

            case 2:
                opInsert = pedir_opcao(config.MENU_ENTIDADES)
                if opInsert == 0:
                    continue
                insert(opInsert)

            case 3:
                opUpdate = pedir_opcao(config.MENU_ENTIDADES)
                if opUpdate == 0:
                    continue
                update(opUpdate)

            case 4:
                opDelete = pedir_opcao(config.MENU_ENTIDADES)
                if opDelete == 0:
                    continue
                delete(opDelete)

            case 0:
                print("Saindo...")
                break

            case _:
                print("Inválido. Tente novamente.")
        match opcao:
            case 1:
                opRelatorios = pedir_opcao(config.MENU_RELATORIOS)
                if opRelatorios == 0:
                    continue
                reports(opRelatorios)

            case 2:
                opInsert = pedir_opcao(config.MENU_ENTIDADES)
                if opInsert == 0:
                    continue
                insert(opInsert)

            case 3:
                opUpdate = pedir_opcao(config.MENU_ENTIDADES)
                if opUpdate == 0:
                    continue
                update(opUpdate)

            case 4:
                opDelete = pedir_opcao(config.MENU_ENTIDADES)
                if opDelete == 0:
                    continue
                delete(opDelete)

            case 0:
                print("Saindo...")
                break

            case _:
                print("Inválido. Tente novamente.")
                continue

        input("Pressione Enter para continuar...")
        config.clear_console()



if __name__ == "__main__":
    run()