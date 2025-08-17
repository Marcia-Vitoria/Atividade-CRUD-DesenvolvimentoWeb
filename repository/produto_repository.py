from database.connection import get_db

class ProdutoRepository:
    def get_all(self):
        conecta = get_db()
        produtos = conecta.execute("""
            SELECT p.id, p.nome, p.preco, c.nome AS categoria, c.corredor
            FROM produtos p
            LEFT JOIN categorias c ON p.categoria_id = c.id
        """).fetchall()
        conecta.close()
        return produtos

    def get_by_id(self, id):
        conecta = get_db()
        produto = conecta.execute("SELECT * FROM produtos WHERE id=?", (id,)).fetchone()
        conecta.close()
        return produto

    def create(self, produto):
        conecta = get_db()
        conecta.execute("INSERT INTO produtos (nome, preco, categoria_id) VALUES (?, ?, ?)",
                     (produto.get_nome(), produto.get_preco(), produto.get_categoria_id()))
        conecta.commit()
        conecta.close()

    def update(self, produto):
        conecta = get_db()
        conecta.execute("UPDATE produtos SET nome=?, preco=?, categoria_id=? WHERE id=?",
                     (produto.get_nome(), produto.get_preco(), produto.get_categoria_id(), produto.get_id()))
        conecta.commit()
        conecta.close()

    def delete(self, id):
        conecta = get_db()
        conecta.execute("DELETE FROM produtos WHERE id=?", (id,))
        conecta.commit()
        conecta.close()