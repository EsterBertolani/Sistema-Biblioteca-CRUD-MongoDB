SELECT em.id_emprestimo,
       le.nome AS nome_leitor,
       li.titulo AS titulo_livro,
       em.data_emprestimo,
       em.data_devolucao_realizada
FROM emprestimo em
JOIN leitor le ON em.id_leitor = le.id_leitor
JOIN livro li ON em.id_livro = li.id_livro
ORDER BY em.data_emprestimo;
