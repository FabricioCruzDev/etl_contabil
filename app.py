import pandas as pd
from datetime import datetime

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import conta_contabil
import pandas as pd
import numpy as np

import re


# LER BANCO DE DADOS - CONTAS BANCÁRIAS
#df_contas_banco = Conta_Banco.get_contas()

# LER EXCEL - CONTAS CONTÁBEIS
ARQUIVO_PLANO = 'dw/silver/pilot_test.xlsx'
df = pd.read_excel(ARQUIVO_PLANO, dtype='str')


# CONTAS BANCÁRIAS
df_contas_banco = df[['conta_bancaria', 'conta']]
df_contas_banco.drop_duplicates(subset=['conta_bancaria', 'conta'], inplace=True)

print(df_contas_banco)

#TODO CORRIGIR DUPLICAÇÃO
#conta_contabil.update_conta_banco(df_contas_banco)

#ATUALIZA DF
bancos = conta_contabil.consulta_bancos()

df['conta_bancaria'] = df['conta_bancaria'].astype(int)
bancos['conta_bancaria'] = bancos['conta_bancaria'].astype(int)

# Realiza o merge normalmente
df_merged = df.merge(bancos, how='left', on='conta_bancaria')

print(df_merged)

df_contas = df_merged[['id_x', 'id_y', 'descricao', 'conta_descricao']]
df_contas.rename(columns={'id_x': 'c_id', 'id_y': 'id_banco'}, inplace=True)

conta_contabil.update_conta_descricao(df_contas)
 
#TODO conferir atualizações

