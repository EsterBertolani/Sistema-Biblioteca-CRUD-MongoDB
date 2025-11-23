from conexion.mysql_queries import MySQLQueries

def create_tables(query: str):
    """
    Cria as tabelas no banco de dados MySQL a partir de um arquivo SQL.
    """
    list_of_commands = query.split(";")

    mysql = MySQLQueries(can_write=True)
    mysql.connect()

    for command in list_of_commands:
        command = command.strip()
        if len(command) > 0:
            print(f"\nExecutando comando:\n{command}")
            try:
                mysql.executeDDL(command)
                print("Comando executado com sucesso.")
            except Exception as e:
                print(f"Erro ao executar: {e}")

def generate_records(query: str, sep: str = ';'):
    """
    Insere registros de exemplo no banco de dados MySQL.
    """
    list_of_commands = query.split(sep)

    mysql = MySQLQueries(can_write=True)
    mysql.connect()

    for command in list_of_commands:
        command = command.strip()
        if len(command) > 0:
            print(f"\nInserindo registro:\n{command}")
            try:
                mysql.write(command)
                print("Registro inserido com sucesso.")
            except Exception as e:
                print(f"Erro ao inserir: {e}")

def run():
    """
    Executa todo o processo de configuração:
    - Cria as tabelas
    - Insere os dados de exemplo
    - Insere dados relacionados (se existirem)
    """

    # Caminho relativo para os scripts SQL
    with open("src/sql/create_tables_biblioteca.sql", encoding="utf-8") as f:
        query_create = f.read()

    print("\nCriando tabelas...")
    create_tables(query=query_create)
    print("Tabelas criadas com sucesso!\n")

    with open("src/sql/inserting_sample_records.sql", encoding="utf-8") as f:
        query_generate_records = f.read()

    print("\n📥 Inserindo registros de exemplo...")
    generate_records(query=query_generate_records)
    print("Registros inseridos com sucesso!\n")

    # Se tiver dados com dependências (tipo empréstimos com FK)
    try:
        with open("src/sql/inserting_related_records.sql", encoding="utf-8") as f:
            query_generate_related_records = f.read()

        print("\nInserindo registros relacionados...")
        generate_records(query=query_generate_related_records, sep='--')
        print("Registros relacionados inseridos com sucesso!\n")
    except FileNotFoundError:
        print("Nenhum arquivo de registros relacionados encontrado, continuando...\n")

if __name__ == '__main__':
    run()
