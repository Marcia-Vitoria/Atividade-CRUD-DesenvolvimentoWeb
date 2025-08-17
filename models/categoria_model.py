class CategoriaModel:
    def __init__(self, id=None, nome=None, descricao=None, corredor=None):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.corredor = corredor

    def get_id(self):
        return self.id

    def get_nome(self):
        return self.nome

    def get_descricao(self):
        return self.descricao

    def get_corredor(self):
        return self.corredor