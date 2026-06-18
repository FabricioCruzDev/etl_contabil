import pandas as pd
from datetime import datetime

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from models.conta_banco import Conta_Banco
from models.conta_contabil import Conta_Contabil
import pandas as pd

import re


# LER BANCO DE DADOS - CONTAS BANCÁRIAS
df_contas_banco = Conta_Banco.get_contas()

# LER EXCEL - CONTAS CONTÁBEIS
ARQUIVO_PLANO = 'dw/silver/Contas_consolidado.xlsx'
df_contas_contabeis = pd.read_excel(ARQUIVO_PLANO, index_col='id', dtype='str')

# MERGE DF
df_merged = df_contas_contabeis.merge(df_contas_banco, how='left', left_on='conta_bancaria', right_on='conta')
#TODO - REVISAR 
df_merged = df_merged[['id', 'descricao', 'conta_contabil']]


Conta_Contabil.salva_conta_contabil(df_merged)

 


