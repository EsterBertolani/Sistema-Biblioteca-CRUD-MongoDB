from controller.controller_leitor import ControllerLeitor
from controller.controller_livro import ControllerLivro
from controller.controller_emprestimo import ControllerEmprestimo

def menu_principal():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Gerenciar Leitores")
        print("2 - Gerenciar Livros")
        print("3 - Gerenciar Empréstimos")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            menu_leitor()
        elif opcao == "2":
            menu_livro()
        elif opcao == "3":
            menu_emprestimo()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("⚠️ Opção inválida, tente novamente.")

# ---------------------------------------------------------------
def menu_leitor():
    ctrl = ControllerLeitor()
    while True:
        print("\n=== MENU LEITOR ===")
        print("1 - Cadastrar leitor")
        print("2 - Atualizar leitor")
        print("3 - Excluir leitor")
        print("4 - Listar leitores")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            ctrl.cadastrar_leitor()
        elif opcao == "2":
            ctrl.atualizar_leitor()
        elif opcao == "3":
            ctrl.excluir_leitor()
        elif opcao == "4":
            ctrl.listar_leitores()
        elif opcao == "0":
            break
        else:
            print("⚠️ Opção inválida, tente novamente.")

# ---------------------------------------------------------------
def menu_livro():
    ctrl = ControllerLivro()
    while True:
        print("\n=== MENU LIVRO ===")
        print("1 - Cadastrar livro")
        print("2 - Atualizar livro")
        print("3 - Excluir livro")
        print("4 - Listar livros")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            ctrl.cadastrar_livro()
        elif opcao == "2":
            ctrl.atualizar_livro()
        elif opcao == "3":
            ctrl.excluir_livro()
        elif opcao == "4":
            ctrl.listar_livros()
        elif opcao == "0":
            break
        else:
            print("⚠️ Opção inválida, tente novamente.")

# ---------------------------------------------------------------
def menu_emprestimo():
    ctrl = ControllerEmprestimo()
    while True:
        print("\n=== MENU EMPRÉSTIMO ===")
        print("1 - Cadastrar empréstimo")
        print("2 - Atualizar empréstimo")
        print("3 - Excluir empréstimo")
        print("4 - Listar empréstimos")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            ctrl.registrar_emprestimo()
        elif opcao == "2":
            ctrl.devolver_livro()
        elif opcao == "3":
            ctrl.excluir_emprestimo()
        elif opcao == "0":
            break
        else:
            print("⚠️ Opção inválida, tente novamente.")

# ---------------------------------------------------------------
if __name__ == "__main__":
    menu_principal()
