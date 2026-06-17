# ETL Contábil: Reconciliação de Extratos

Este é um pipeline de ETL (Extract, Transform, Load) desenvolvido para automatizar o cruzamento de dados financeiros. O sistema extrai informações de extratos bancários enviados em formato Excel pelo cliente e realiza a reconciliação (*matching*) com os dados oficiais extraídos do sistema contábil da empresa. 

Após as etapas de transformação e validação, os dados estruturados das contas contábeis são exportados para o sistema oficial.

## 🚀 Funcionalidades

- **Extração (Extract):** Leitura automatizada de arquivos Excel (`.xlsx` ou `.xls`) enviados por clientes.
- **Transformação (Transform):** Limpeza de dados, padronização de campos e cruzamento inteligente (reconciliação) de informações financeiras.
- **Modelagem Avançada:** Integração com bibliotecas de *Machine Learning* e análise estatística para agrupamento ou validação das contas.
- **Carga (Load):** Persistência e atualização do plano de contas no banco de dados relacional leve SQLite.

## 🛠️ Tecnologias e Dependências

O projeto está em fase de construção a partir de modelos previamente validados em notebooks (`.ipynb`), utilizando as seguintes especificações técnicas:

* **Linguagem:** Python 3.12.12
* **Manipulação de Dados:** Pandas 3.0.3
* **Algoritmos / Inteligência:** Scikit-Learn 1.9.0
* **Banco de Dados:** SQLite3 (Nativo do Python)

## 📁 Estrutura do Projeto

```text
etl_contabil/
├── dw/                  # Banco de dados SQLite (.db), arquivos CSV e Excel organizados na arquitetura Raw, Bronze, Silver e Gold
├── models/              # Scripts de regras de negócio e rotinas de persistência
├── app                  # Script principal
├── .gitignore           # Filtro de arquivos protegidos (venv, caches)
├── README.md            # Documentação do projeto
└── requirements.txt     # Listagem de dependências do projeto
```

              

## 📌 Principais Imports Utilizados

A aplicação utiliza os seguintes pacotes para execução do fluxo:

```python
import pandas as pd             # Estruturação, manipulação e junção de DataFrames
import sklearn                  # Processamento contábil inteligente e modelagem
import sqlite3                  # Conexão e inserção no banco de dados SQL local
```
