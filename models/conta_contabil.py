from conta_banco import Conta_Banco

class Conta_Contabil():
    def __init__(self, conta_id: Conta_Banco, descricao: str, conta_contabil: int):
        self.conta_id = conta_id
        self.descricao = descricao
        self.conta_contabil = conta_contabil