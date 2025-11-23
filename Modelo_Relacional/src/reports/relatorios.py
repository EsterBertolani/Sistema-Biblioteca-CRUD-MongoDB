from conexion.mongo_queries import MongoQueries

class Relatorios:
    def __init__(self):
        pass

    # ------------------------------------------------------------
    def get_relatorio_emprestimos_detalhados(self):
        mongo = MongoQueries()
        mongo.connect()

        print("\n=== RELATÓRIO DE EMPRÉSTIMOS DETALHADOS ===\n")

        pipeline = [
            {"$lookup": {
                "from": "leitor",
                "localField": "id_leitor",
                "foreignField": "id_leitor",
                "as": "leitor"
            }},
            {"$unwind": "$leitor"},

            {"$lookup": {
                "from": "livro",
                "localField": "id_livro",
                "foreignField": "id_livro",
                "as": "livro"
            }},
            {"$unwind": "$livro"},

            {"$project": {
                "_id": 0,
                "id_emprestimo": 1,
                "leitor": "$leitor.nome",
                "livro": "$livro.titulo",
                "data_emprestimo": 1,
                "data_devolucao_prevista": 1,
                "data_devolucao_realizada": 1
            }}
        ]

        resultado = list(mongo.db["emprestimo"].aggregate(pipeline))

        if not resultado:
            print("Nenhum empréstimo encontrado.")
        else:
            for r in resultado:
                print(
                    f"ID: {r['id_emprestimo']} | "
                    f"Leitor: {r['leitor']} | "
                    f"Livro: {r['livro']} | "
                    f"Empréstimo: {r['data_emprestimo']} | "
                    f"Prevista: {r['data_devolucao_prevista']} | "
                    f"Devolução: {r['data_devolucao_realizada']}"
                )

        mongo.close()

    def get_relatorio_total_emprestimos_por_livro(self):
        mongo = MongoQueries()
        mongo.connect()

        print("\n=== RELATÓRIO DE LIVROS MAIS EMPRESTADOS ===\n")

        pipeline = [
            {"$group": {
                "_id": "$id_livro",
                "total": {"$sum": 1}
            }},
            {"$lookup": {
                "from": "livro",
                "localField": "_id",
                "foreignField": "id_livro",
                "as": "livro"
            }},
            {"$unwind": "$livro"},
            {"$project": {
                "_id": 0,
                "livro": "$livro.titulo",
                "total": 1
            }},
            {"$sort": {"total": -1}}
        ]

        resultado = list(mongo.db["emprestimo"].aggregate(pipeline))

        if not resultado:
            print("Nenhum registro encontrado.")
        else:
            for r in resultado:
                print(f"Livro: {r['livro']} | Total de Empréstimos: {r['total']}")

        mongo.close()
