class ProdutoModel:
    def __init__(self, id=None, nome=None, preco=None, categoria_id=None):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.categoria_id = categoria_id

    def get_id(self):
        return self.id

    def get_nome(self):
        return self.nome

    def get_preco(self):
        return self.preco

    def get_categoria_id(self):
        return self.categoria_id