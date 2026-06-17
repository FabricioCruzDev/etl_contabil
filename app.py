import pandas as pd
from datetime import datetime

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from models.conta_banco import Conta_Banco

import re



df_contas_banco = Conta_Banco.get_contas()
print(df_contas_banco)





