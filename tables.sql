CREATE TABLE conta_banco (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    conta INTEGER NOT NULL,
    conta_contabil INTEGER NOT NULL
);

CREATE TABLE conta_contabil (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    conta_id INTEGER NOT NULL,
    descricao VARCHAR(255) NOT NULL,
    conta_contabil INTEGER NOT NULL,
    FOREIGN KEY (conta_id) REFERENCES conta_banco(id)
)