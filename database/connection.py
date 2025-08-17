import sqlite3
import os

DATABASE = os.path.join(os.path.dirname("base.sql"), "banco.db")

def get_db():
    conecta = sqlite3.connect(DATABASE)
    conecta.row_factory = sqlite3.Row
    return conecta

def init_db(): # cria as tabelas se não existirem usando execução direta do SQL
    if not os.path.exists(DATABASE):
        conecta = get_db()
        with open(os.path.join(os.path.dirname("base.sql")), "r", encoding="utf-8") as f:
            conecta.executescript(f.read())
        conecta.commit()
        conecta.close()