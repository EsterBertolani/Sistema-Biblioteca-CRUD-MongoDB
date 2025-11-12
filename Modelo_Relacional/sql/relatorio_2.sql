SELECT li.titulo AS livro,
       COUNT(em.id_emprestimo) AS total_emprestimos
FROM emprestimo em
JOIN livro li ON em.id_livro = li.id_livro
GROUP BY li.titulo
ORDER BY total_emprestimos DESC;
