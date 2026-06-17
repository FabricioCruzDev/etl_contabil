import pandas as pd
from datetime import datetime

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from conn import con
import re


cur = con.cursor()

for row in cur.execute('''SELECT * FROM stocks'''):
    print(row)

cur.close()