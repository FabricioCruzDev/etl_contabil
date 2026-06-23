from sqlalchemy import text
from conn import engine

import pandas as pd
import numpy as np




def get_bancos()-> pd.DataFrame: 
    query = text("SELECT * FROM conta_banco") 
    df_resultado = pd.read_sql_query(query, con=engine, dtype='str')  
    return df_resultado

def get_contas(file)-> pd.DataFrame:
    df_resultado = pd.read_excel(file, dtype='str')
    return df_resultado