import sqlite3
from pathlib import Path
from sqlalchemy import create_engine, text, MetaData, Table



DB = 'dw/gold/contas.db'

connection = sqlite3.connect(DB)

engine = create_engine(f"sqlite+pysqlite:///{DB}")

metadata = MetaData()