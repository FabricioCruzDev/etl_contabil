from models.conta_banco import Conta_Banco
from conn import connection
import pandas as pd

class Conta_Contabil():
    def __init__(self, conta_id: Conta_Banco, descricao: str, conta_contabil: int):
        self.conta_id = conta_id
        self.descricao = descricao
        self.conta_contabil = conta_contabil

    def salva_conta_contabil(df):
        cur = None
        try:
            with connection:
                for row in df.itertuples(index=False):
                    cur = connection.cursor()
                    cur.execute(
                        "INSERT INTO conta_contabil (conta_id, descricao, conta_contabil) VALUES (?, ?, ?);",
                        (row[0], row[1], row[2])
                    )
        except Exception as e:
            print(f"Erro na transação: {e}")
            raise e
        finally:
            if cur:
                cur.close()
