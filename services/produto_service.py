from database.connection import get_db

def listar_produtos():
    conecta = get_db()
    produtos = conecta.execute("""
        SELECT p.id, p.nome, p.preco, c.nome as categoria, c.corredor
        FROM produtos p
        LEFT JOIN categorias c ON p.categoria_id = c.id
    """).fetchall()
    conecta.close()
    return produtos

def criar_produto(nome, preco, categoria_id):
    conecta = get_db()
    conecta.execute("INSERT INTO produtos (nome, preco, categoria_id) VALUES (?, ?, ?)",
                 (nome, preco, categoria_id))
    conecta.commit()
    conecta.close()

def atualizar_produto(id, nome, preco, categoria_id):
    conecta = get_db()
    conecta.execute("UPDATE produtos SET nome=?, preco=?, categoria_id=? WHERE id=?",
                 (nome, preco, categoria_id, id))
    conecta.commit()
    conecta.close()

def remover_produto(id):
    conecta = get_db()
    conecta.execute("DELETE FROM produtos WHERE id=?", (id,))
    conecta.commit()
    conecta.close()

def buscar_produto(id):
    conecta = get_db()
    produto = conecta.execute("SELECT * FROM produtos WHERE id=?", (id,)).fetchone()
    conecta.close()
    return produto