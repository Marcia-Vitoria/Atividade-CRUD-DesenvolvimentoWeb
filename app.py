from database.connection import init_db, get_db
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
init_db()

# Rota para a página inicial
@app.route("/")
def home():
    return render_template("home.html")

# Rotas para categorias
@app.route("/categorias")
def listar_categorias():
    conecta = get_db()
    categorias = conecta.execute("SELECT * FROM categorias").fetchall()
    conecta.close()
    return render_template("categorias.html", categorias=categorias)

@app.route("/categorias/novo", methods=["GET", "POST"])
def nova_categoria():
    if request.method == "POST":
        nome = request.form["nome"]
        descricao = request.form["descricao"]
        corredor = request.form["corredor"]
        conecta = get_db()
        conecta.execute("INSERT INTO categorias (nome, descricao, corredor) VALUES (?, ?, ?)", (nome, descricao, corredor))
        conecta.commit()
        conecta.close()
        return redirect(url_for("listar_categorias"))
    return render_template("categoria_form.html")

@app.route("/categorias/editar/<int:id>", methods=["GET", "POST"])
def editar_categoria(id):
    conecta = get_db()
    if request.method == "POST":
        nome = request.form["nome"]
        descricao = request.form["descricao"]
        corredor = request.form["corredor"]
        conecta.execute("UPDATE categorias SET nome=?, descricao=?, corredor=? WHERE id=?", (nome, descricao, corredor, id))
        conecta.commit()
        conecta.close()
        return redirect(url_for("listar_categorias"))
    categoria = conecta.execute("SELECT * FROM categorias WHERE id=?", (id,)).fetchone()
    conecta.close()
    return render_template("categoria_form.html", categoria=categoria)

@app.route("/categorias/excluir/<int:id>")
def excluir_categoria(id):
    conecta = get_db()
    conecta.execute("DELETE FROM categorias WHERE id=?", (id,))
    conecta.commit()
    conecta.close()
    return redirect(url_for("listar_categorias"))

# Rotas para produtos
@app.route("/")
@app.route("/produtos")
def listar_produtos():
    conecta = get_db()
    produtos = conecta.execute("""
        SELECT p.id, p.nome, p.preco, c.nome as categoria
        FROM produtos p
        LEFT JOIN categorias c ON p.categoria_id = c.id
    """).fetchall()
    conecta.close()
    return render_template("produtos.html", produtos=produtos)

@app.route("/produtos/novo", methods=["GET", "POST"])
def novo_produto():
    conecta = get_db()
    categorias = conecta.execute("SELECT * FROM categorias").fetchall()
    if request.method == "POST":
        nome = request.form["nome"]
        preco = request.form["preco"]
        categoria_id = request.form["categoria_id"] or None
        conecta.execute("INSERT INTO produtos (nome, preco, categoria_id) VALUES (?, ?, ?)", (nome, preco, categoria_id))
        conecta.commit()
        conecta.close()
        return redirect(url_for("listar_produtos"))
    conecta.close()
    return render_template("produto_form.html", categorias=categorias)

@app.route("/produtos/editar/<int:id>", methods=["GET", "POST"])
def editar_produto(id):
    conecta = get_db()
    categorias = conecta.execute("SELECT * FROM categorias").fetchall()
    if request.method == "POST":
        nome = request.form["nome"]
        preco = request.form["preco"]
        categoria_id = request.form["categoria_id"] or None
        conecta.execute("UPDATE produtos SET nome=?, preco=?, categoria_id=? WHERE id=?", (nome, preco, categoria_id, id))
        conecta.commit()
        conecta.close()
        return redirect(url_for("listar_produtos"))
    produto = conecta.execute("SELECT * FROM produtos WHERE id=?", (id,)).fetchone()
    conecta.close()
    return render_template("produto_form.html", produto=produto, categorias=categorias)

@app.route("/produtos/excluir/<int:id>")
def excluir_produto(id):
    conecta = get_db()
    conecta.execute("DELETE FROM produtos WHERE id=?", (id,))
    conecta.commit()
    conecta.close()
    return redirect(url_for("listar_produtos"))

if __name__ == "__main__":
    init_db()
    app.run(debug=True)