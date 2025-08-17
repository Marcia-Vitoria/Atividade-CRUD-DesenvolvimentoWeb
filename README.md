# 🛒 Supermercado - CRUD com Flask e SQLite

Este projeto é uma aplicação web simples de um supermercado, desenvolvida em Python utilizando Flask e SQLite, além de HTML, CSS e Jinja. Ele implementa o CRUD completo (Create, Read, Update, Delete) para produtos e categorias, permitindo gerenciar os itens do mercado e suas categorias correspondentes.

---

## 1. Entidades

#### 1.1 📂 Categoria

A entidade **Categoria** representa os grupos de produtos no supermercado.

**Atributos:**

* `id` – Identificador único (inteiro, autoincremento)
* `nome` – Nome da categoria (ex.: Padaria, Hortifruti)
* `descricao` – Breve descrição da categoria
* `corredor` – Localização no supermercado

---

#### 1.2 🛍️ Produto

A entidade **Produto** representa os itens disponíveis para venda.

**Atributos:**

* `id` – Identificador único (inteiro, autoincremento)
* `nome` – Nome do produto (ex.: Pão, Maçã)
* `preco` – Preço do produto
* `categoria_id` – Referência à categoria à qual o produto pertence (relacionamento **Produto → Categoria**)

---

## 2. 🔗 Relacionamento

O produto e a categoria possuem um relacionamento muitos-para-um (N:1):
* Cada produto pertence a uma única categoria.
* Cada categoria pode ter vários produtos associados.

No banco de dados, a tabela produtos possui a coluna categoria_id, que é uma chave estrangeira referenciando o id da tabela categorias.

---

## 3. ⚙️ Pré-requisitos

* Python 3.x
* Flask (`pip install flask`)
* SQLite3 (geralmente já instalado com Python)

---

## 4. 🚀 Como executar o projeto

#### Passo 1 – Clonar o repositório

```bash
git clone https://github.com/Marcia-Vitoria/Atividade-CRUD-DesenvolvimentoWeb.git
cd Atividade-CRUD-DesenvolvimentoWeb
```

#### Passo 2 – Criar e ativar ambiente virtual (opcional, mas recomendado)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / Mac
python3 -m venv venv
source venv/bin/activate
```

#### Passo 3 – Instalar dependências

*Caso precise instalar ou atualizar o pip:*
```bash
# Windows / Linux / Mac
python -m ensurepip --upgrade
python -m pip install --upgrade pip
```
*Com o pip atualizado, instale o Flask:*
```bash
pip install flask
```
*Caso já tenha o Flask instalado e queira atualizar:*
```bash
pip install --upgrade flask
```

#### Passo 4 – Executar a aplicação

```bash
python run.py
```

#### Passo 5 – Acessar no navegador

* Home: `http://127.0.0.1:5000/`
* Lista de categorias: `http://127.0.0.1:5000/categorias`
* Lista de produtos: `http://127.0.0.1:5000/produtos`

## 5. 🗂️ Estrutura do projeto

```
crud-supermercado/
│── app.py                  # Arquivo principal para rodar a aplicação
│── banco.db                # Banco SQLite (criado com base.sql)
│── database/
│   ├── base.sql
│   └── connection.py
│── models/
│   ├── categoria_model.py
│   └── produto_model.py
│── repository/
│   ├── categoria_repository.py
│   └── produto_repository.py
│── services/
│   ├── categoria_service.py
│   └── produto_service.py
│── static/
│   └── style.css
│── templates/
    ├── base.html
    ├── home.html
    ├── categorias.html
    ├── produtos.html
    ├── categoria_form.html
    └── produto_form.html

```
---
#### 👩‍💻 Autora: Márcia Vitória
---