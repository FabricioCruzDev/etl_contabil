import pandas as pd
from tkinter import filedialog as fd
from datetime import datetime

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import load
import extract

import re

# LER EXCEL - CONTAS CONTÁBEIS
def selecionar_arquivo():
    # Abre a caixa de diálogo para escolher um arquivo
    caminho_arquivo = fd.askopenfilename(
        title="Selecione um arquivo",
        filetypes=[("Todos os arquivos", "*.xlsx")],
        initialdir="dw/silver"
    )
    return caminho_arquivo

# RECEBE DICIONÁRIO DE CONTAS
df_contas_contabeis = extract.get_contas(selecionar_arquivo())


#ATUALIZA BANCO DE CONTAS BANCÁRIAS
df_contas_banco_atual = df_contas_contabeis[['conta_bancaria', 'conta']]
df_contas_banco_atual.drop_duplicates(subset=['conta_bancaria', 'conta'], inplace=True)
df_contas_banco_atual.insert(0, 'id', range(1, len(df_contas_banco_atual) + 1))
print('Atualizando tabelas')
load.update_conta_banco(df_contas_banco_atual)


# MERGE
df_merged = df_contas_contabeis.merge(df_contas_banco_atual, how='left', on='conta_bancaria')


#ATUALIZA BANCO DAS CONTAS CONTÁBEIS (CONTA_DESCRICAO)
df_conta_descricao = df_merged[['id_x', 'id_y', 'descricao', 'conta_descricao']]
df_conta_descricao.rename(columns={'id_x': 'c_id', 'id_y': 'id_banco'}, inplace=True)
load.update_conta_descricao(df_conta_descricao)
