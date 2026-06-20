# ETL Contábil: Reconciliação de Extratos

Este é um pipeline de ETL (Extract, Transform, Load) desenvolvido para automatizar o cruzamento de dados financeiros. O sistema extrai informações de extratos bancários enviados em formato Excel pelo cliente e realiza a reconciliação (*matching*) com os dados oficiais extraídos do sistema contábil da empresa. 

Após as etapas de transformação e validação, os dados estruturados das contas contábeis são atualizados no banco de dados.

## 🚀 Funcionalidades

- **Extração (Extract):** Leitura automatizada de arquivos Excel (`.xlsx` ou `.xls`) enviados por clientes.
- **Transformação (Transform):** Limpeza de dados, padronização de tipos de campos (tratamento de inconsistências de texto/inteiro) e cruzamento inteligente (reconciliação) de informações financeiras.
- **Modelagem Avançada:** Integração com bibliotecas de *Machine Learning* e análise estatística para agrupamento ou validação das contas.
- **Carga Eficiente (Load):** Persistência e atualização do plano de contas via **SQLAlchemy**, utilizando a estratégia de *Upsert* (`INSERT OR REPLACE`) nativa para evitar duplicidade de registros.

## 🛠️ Tecnologias e Dependências

O projeto utiliza as seguintes especificações técnicas e bibliotecas atualizadas:

* **Linguagem:** Python 3.12.x
* **Manipulação de Dados:** Pandas 3.0.x
* **Persistência & ORM:** SQLAlchemy (com dialeto nativo para SQLite)
* **Algoritmos / Inteligência:** Scikit-Learn 1.9.x
* **Banco de Dados:** SQLite (Camada analítica local)

## 📁 Estrutura do Projeto

O projeto foi modularizado para separar as configurações de conexão, modelos de dados e execução do pipeline:

```text
etl_contabil/
├── dw/                  # Arquitetura de dados (Raw, Bronze, Silver, Gold) contendo dados de teste fictícios (.db, .xlsx)
├── models/              # Scripts de regras de negócio, classes de entidade e rotinas de persistência
│   ├── conta_banco.py   # Modelo de dados da conta bancária
│   └── conta_contabil.py# Modelo e métodos de Upsert da conta contábil
├── app.py               # Script principal que executa o fluxo completo do pipeline de ETL
├── conn.py              # Centralização da conexão, Engine e Metadados do SQLAlchemy
├── .gitignore           # Filtro de arquivos protegidos (venv, caches, DBs locais de prod)
├── README.md            # Documentação do projeto
└── requirements.txt     # Listagem de dependências do projeto
```

## 📌 Principais Imports Utilizados

A aplicação utiliza pacotes modernos para garantir performance e segurança nas transações com o banco de dados:

```python
import pandas as pd                       # Estruturação, manipulação de tipos e junção (merge) de DataFrames
from sqlalchemy import create_engine      # Gerenciamento de conexões robusto e Pythônico
from sqlalchemy.dialects.sqlite import insert  # Execução de Upsert (ON CONFLICT DO UPDATE) nativo
import sklearn                            # Processamento contábil inteligente e modelagem
```

## ⚙️ Como Executar com os Dados de Teste

1. **Configurar o Ambiente Virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Linux/Mac
   # venv\Scripts\activate   # No Windows
   pip install -r requirements.txt
   ```

2. **Dados de Teste:**
   A pasta `dw/` já conta com arquivos e bancos de dados fictícios configurados para validar o pipeline sem expor dados reais de clientes.

3. **Rodar o Pipeline:**
   ```bash
   python app.py
   ```
