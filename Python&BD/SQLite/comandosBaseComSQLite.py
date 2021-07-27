"""IMPORTS"""
import os, random, datetime
import sqlite3

from setuptools.command.install import install
from setuptools.command.upload_docs import upload_docs

os.remove("dsh.db") if os.path.exists("dsh.db") else None

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

# Consultar dados
def select(query = "", columns = "*"):
    query = "SELECT "+columns+" FROM produtos " + query

    try:
        cur.execute(query)
        for linha in cur.fetchall():
            print(linha)
    except:
        print("Erro na consulta de dados")
    else:
        print("Leitura feita com sucesso!\n ")

# Atualiza dados
def update(coluna, valor, condicao):
    query = "UPDATE produtos SET {0} = {1} WHERE {2}".format(coluna, valor, condicao)
    try:
        cur.execute(query)
        conn.commit()
    except:
        print("Erro na atualização de dado(s)")
    else:
        print("Atualização feita com sucesso!\n ")

# deleta dados
def delete(condicao):
    try:
        cur.execute("DELETE FROM produtos WHERE "+ condicao)
        conn.commit()
    except:
        print("Erro ao apagar dado(s)")
    else:
        print("apagado(s) com sucesso!\n ")


# =======================
create_Table("produtos")
for i in range(10):
    insert()

# Consultando TODOS os registros
select("")
# Consultando registros ESPECÍFICOS
select("WHERE valor > 65.0")
select("", "valor")

#Atualizando dados no BD
update("valor", 70.00, "valor < 57.0")
select("")   # --> para verificar a alteração no prompt

# exclusão de registros
delete(" valor > 68")
select("")   # --> para verificar a alteração no prompt

cur.close()
conn.close()