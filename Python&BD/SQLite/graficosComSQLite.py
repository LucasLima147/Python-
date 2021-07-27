"""IMPORTS"""
import random, datetime
import matplotlib.pyplot as plt
import sqlite3

from setuptools.command.install import install
from setuptools.command.upload_docs import upload_docs

conn = sqlite3.connect("dsh.db")
cur = conn.cursor()

""" FUCTIONS """
# criar tabela
def create_Table(name_table):
    try:
        cur.execute("CREATE TABLE IF NOT EXISTS "+name_table+"("\
                    "id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"\
                    "date TEXT,"\
                    "prod_name TEXT,"\
                    "valor REAL)")
    except:
        print("Erro ao Criar a tabela")
    else:
        print("Tabela criada com sucesso")

# Inserir dados
def insert():
    try:
        new_date = datetime.datetime.now()
        new_produ_nome = "monitor"
        new_valor = random.randrange(50,70)
        cur.execute("INSERT INTO produtos(date, prod_name, valor) VALUES (?, ?, ?)", (new_date, new_produ_nome, new_valor))
        conn.commit()
    except:
        print("Erro de Inserção")
    else:
        print("Inserção realizada com sucesso")

# gerando um gráfico
def gerarGrafico():
    cur.execute("SELECT id, valor FROM produtos")
    ids = []
    valores = []
    dados = cur.fetchall()
    for linha in dados:
        ids.append(linha[0])
        valores.append(linha[1])

    plt.bar(ids, valores)
    plt.show()
# =======================

create_Table("produtos")
insert()
gerarGrafico()

cur.close()
conn.close()