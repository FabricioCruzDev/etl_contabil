from conn import connection
import pandas as pd

class Conta_Banco():
      
    def __init__(self, conta: str, conta_contabil: int):
        self.conta = conta
        self.conta_contabil = conta_contabil

    def get_contas():
        with connection:
            cur = connection.cursor()
            stm = "SELECT * FROM conta_banco"
            result = cur.execute(stm)
            #Capturando o nome das colunas
            columns = [col[0] for col in result.description]
            #Capturando os dados
            return pd.DataFrame.from_records(result.fetchall(), columns=columns)
            
      
    def salva_conta(self):
        print('Salvando a conta....', self.conta, self.conta_contabil) 
        with connection:
            cur = connection.cursor()
            cur.execute("INSERT INTO conta_banco" \
            "(conta, conta_contabil) VALUES (?, ?)",
            (self.conta, self.conta_contabil)
            )
            connection.commit()


    