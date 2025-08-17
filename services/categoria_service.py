from database.connection import get_db

def listar_categorias():
    conecta = get_db()
    categorias = conecta.execute("SELECT * FROM categorias").fetchall()
    conecta.close()
    return categorias

def criar_categoria(nome, descricao, corredor):
    conecta = get_db()
    conecta.execute("INSERT INTO categorias (nome, descricao, corredor) VALUES (?, ?, ?)",
                 (nome, descricao, corredor))
    conecta.commit()
    conecta.close()

def atualizar_categoria(id, nome, descricao, corredor):
    conecta = get_db()
    conecta.execute("UPDATE categorias SET nome=?, descricao=?, corredor=? WHERE id=?",
                 (nome, descricao, corredor, id))
    conecta.commit()
    conecta.close()

def remover_categoria(id):
    conecta = get_db()
    conecta.execute("DELETE FROM categorias WHERE id=?", (id,))
    conecta.commit()
    conecta.close()

def buscar_categoria(id):
    conecta = get_db()
    categoria = conecta.execute("SELECT * FROM categorias WHERE id=?", (id,)).fetchone()
    conecta.close()
    return categoria