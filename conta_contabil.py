#VOU ALTERAR O NOME DESSE MÓDULO

import pandas as pd
from conn import engine, metadata
from sqlalchemy import Table, text
from sqlalchemy.dialects.sqlite import insert


def update_conta_descricao(df : pd.DataFrame):
    tbl = Table('conta_descricao', metadata, autoload_with=engine)
    new_data = df.to_dict(orient='records')
    stmt = insert(tbl).values(new_data)
    upsert_stmt = stmt.on_conflict_do_update(
        index_elements=['c_id'],
        set_={
            'id_banco': stmt.excluded.id_banco,
            'descricao': stmt.excluded.descricao,
            'conta_descricao': stmt.excluded.conta_descricao
        }
    )

    with engine.begin() as _conn:
        _conn.execute(upsert_stmt)

    print('Tabela aualizada com sucesso')


def update_conta_banco(df : pd.DataFrame):
    tbl = Table('conta_banco', metadata, autoload_with=engine)
    new_data = df.to_dict(orient='records')
    stmt = insert(tbl).values(new_data)
    upsert_stmt = stmt.on_conflict_do_update(
        index_elements=['id'],
        set_={
            'conta_bancaria': stmt.excluded.conta_bancaria,
            'conta': stmt.excluded.conta
        }
    )

    with engine.begin() as _conn:
        _conn.execute(upsert_stmt)

    print('Tabela conta_banco aualizada com sucesso')

def consulta_bancos():
    query = text("SELECT * FROM conta_banco")
    
    df_resultado = pd.read_sql_query(query, con=engine)
    
    return df_resultado


    

