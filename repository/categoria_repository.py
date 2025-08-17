from database.connection import get_db

class CategoriaRepository:
    def get_all(self):
        conecta = get_db()
        categorias = conecta.execute("SELECT * FROM categorias").fetchall()
        conecta.close()
        return categorias

    def get_by_id(self, id):
        conecta = get_db()
        categoria = conecta.execute("SELECT * FROM categorias WHERE id=?", (id,)).fetchone()
        conecta.close()
        return categoria

    def create(self, categoria):
        conecta = get_db()
        conecta.execute("INSERT INTO categorias (nome, descricao, corredor) VALUES (?, ?, ?)",
                     (categoria.get_nome(), categoria.get_descricao(), categoria.get_corredor()))
        conecta.commit()
        conecta.close()

    def update(self, categoria):
        conecta = get_db()
        conecta.execute("UPDATE categorias SET nome=?, descricao=?, corredor=? WHERE id=?",
                     (categoria.get_nome(), categoria.get_descricao(), categoria.get_corredor(), categoria.get_id()))
        conecta.commit()
        conecta.close()

    def delete(self, id):
        conecta = get_db()
        conecta.execute("DELETE FROM categorias WHERE id=?", (id,))
        conecta.commit()
        conecta.close()